"""
A Lark Transformer for transforming a Lark parse tree into a Python OrderedDict.
Based on https://github.com/amplify-education/python-hcl2/blob/86c12442dd6ea5410632fd9f8698c8d270ee6262/hcl2/transformer.py
"""
import re
import sys
from collections import OrderedDict
from typing import Any, Dict, List

from lark import Discard, Transformer

HEREDOC_PATTERN = re.compile(r"<<([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1", re.S)
HEREDOC_TRIM_PATTERN = re.compile(
    r"<<-([a-zA-Z][a-zA-Z0-9._-]+)\n((.|\n)*?)\n\s*\1", re.S
)


# pylint: disable=missing-docstring,unused-argument
class OrderedDictTransformer(Transformer):
    def float_lit(self, args: List) -> float:
        return float("".join([str(arg) for arg in args]))

    def int_lit(self, args: List) -> int:
        return int("".join([str(arg) for arg in args]))

    def expr_term(self, args: List) -> Any:
        args = self.strip_new_line_tokens(args)

        #
        if args[0] == "true":
            return True
        if args[0] == "false":
            return False
        if args[0] == "null":
            return None

        # if the expression starts with a paren then unwrap it
        if args[0] == "(":
            return args[1]
        # otherwise return the value itself
        return args[0]

    def index_expr_term(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "%s%s" % (str(args[0]), str(args[1]))

    def index(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "[%s]" % (str(args[0]))

    def get_attr_expr_term(self, args: List) -> str:
        return "%s.%s" % (str(args[0]), str(args[1]))

    def attr_splat_expr_term(self, args: List) -> str:
        return "%s.*.%s" % (args[0], args[1])

    def tuple(self, args: List) -> List:
        return [self.to_string_dollar(arg) for arg in self.strip_new_line_tokens(args)]

    def object_elem(self, args: List) -> Dict:
        # This returns a dict with a single key/value pair to make it easier to merge these
        # into a bigger dict that is returned by the "object" function
        key = self.strip_quotes(args[0])
        value = self.to_string_dollar(args[1])

        return OrderedDict({key: value})

    def object(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = OrderedDict()
        for arg in args:
            result.update(arg)
        return result

    def function_call(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        args_str = ""
        if len(args) > 1:
            args_str = ",".join([str(arg) for arg in args[1]])
        return "%s(%s)" % (str(args[0]), args_str)

    def arguments(self, args: List) -> List:
        return args

    def new_line_and_or_comma(self, args: List) -> Discard:
        return Discard()

    def block(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)

        # if the last token is a string instead of an object then the block is empty
        # such as 'foo "bar" "baz" {}'
        # in that case append an empty object
        if isinstance(args[-1], str):
            args.append(OrderedDict())

        result: Dict[str, Any] = OrderedDict()
        current_level = result
        for arg in args[0:-2]:
            current_level[self.strip_quotes(arg)] = {}
            current_level = current_level[self.strip_quotes(arg)]

        current_level[self.strip_quotes(args[-2])] = args[-1]

        return result

    def one_line_block(self, args: List) -> Dict:
        return self.block(args)

    def attribute(self, args: List) -> Dict:
        key = str(args[0])
        if key.startswith('"') and key.endswith('"'):
            key = key[1:-1]
        value = self.to_string_dollar(args[1])

        return OrderedDict({key: value})

    def conditional(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return "%s ? %s : %s" % (args[0], args[1], args[2])

    def binary_op(self, args: List) -> str:
        return " ".join([str(arg) for arg in args])

    def unary_op(self, args: List) -> str:
        return "".join([str(arg) for arg in args])

    def binary_term(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def body(self, args: List) -> Dict[str, List]:
        # A body can have multiple attributes with the same name
        # For example multiple Statement attributes in a IAM resource body
        # So This returns a dict of attribute names to lists
        # The attribute values will always be lists even if they aren't repeated
        # and only contain a single entry
        args = self.strip_new_line_tokens(args)
        result: Dict[str, Any] = OrderedDict()
        for arg in args:
            for key, value in arg.items():
                key = str(key)
                if key not in result:
                    result[key] = value
                else:
                    if isinstance(result[key], list):
                        if isinstance(value, list):
                            result[key].extend(value)
                        else:
                            result[key].append(value)
                    else:
                        result[key] = [result[key], value]
        return result

    def start(self, args: List) -> Dict:
        args = self.strip_new_line_tokens(args)
        return args[0]

    def binary_operator(self, args: List) -> str:
        return str(args[0])

    def heredoc_template(self, args: List) -> str:
        match = HEREDOC_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])
        return '"%s"' % match.group(2)

    def heredoc_template_trim(self, args: List) -> str:
        # See https://github.com/hashicorp/hcl2/blob/master/hcl/hclsyntax/spec.md#template-expressions
        # This is a special version of heredocs that are declared with "<<-"
        # This will calculate the minimum number of leading spaces in each line of a heredoc
        # and then remove that number of spaces from each line
        match = HEREDOC_TRIM_PATTERN.match(str(args[0]))
        if not match:
            raise RuntimeError("Invalid Heredoc token: %s" % args[0])

        text = match.group(2)
        lines = text.split("\n")

        # calculate the min number of leading spaces in each line
        min_spaces = sys.maxsize
        for line in lines:
            leading_spaces = len(line) - len(line.lstrip(" "))
            min_spaces = min(min_spaces, leading_spaces)

        # trim off that number of leading spaces from each line
        lines = [line[min_spaces:] for line in lines]

        return '"%s"' % "\n".join(lines)

    def new_line_or_comment(self, args: List) -> Discard:
        return Discard()

    def for_tuple_expr(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        for_expr = " ".join([str(arg) for arg in args[1:-1]])
        return "[%s]" % for_expr

    def for_intro(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def for_cond(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        return " ".join([str(arg) for arg in args])

    def for_object_expr(self, args: List) -> str:
        args = self.strip_new_line_tokens(args)
        for_expr = " ".join([str(arg) for arg in args[1:-1]])
        return "{%s}" % for_expr

    def strip_new_line_tokens(self, args: List) -> List:
        """
        Remove new line and Discard tokens.
        The parser will sometimes include these in the tree so we need to strip them out here
        """
        return [arg for arg in args if arg != "\n" and not isinstance(arg, Discard)]

    def to_string_dollar(self, value: Any) -> Any:
        """Wrap a string in ${ and }"""
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
            return "${%s}" % value
        return value

    def strip_quotes(self, value: Any) -> Any:
        """Remove quote characters from the start and end of a string"""
        if isinstance(value, str):
            if value.startswith('"') and value.endswith('"'):
                return str(value)[1:-1]
        return value

    def identifier(self, value: Any) -> Any:
        # Making identifier a token by capitalizing it to IDENTIFIER
        # seems to return a token object instead of the str
        # So treat it like a regular rule
        # In this case we just convert the whole thing to a string
        return str(value[0])
