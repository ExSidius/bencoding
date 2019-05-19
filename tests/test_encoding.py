from examples import Example, STRING_EXAMPLES, INTEGER_EXAMPLES
from bencoding.encode import encode_string, encode_integer


def test_encode_string():
	for example in STRING_EXAMPLES:
		assert encode_string(example.decoded) == example.encoded


def test_encode_integer():
	for example in INTEGER_EXAMPLES:
		assert encode_integer(example.decoded) == example.encoded