from bencoding.encode import encode
from examples import (
	Example,
	STRING_EXAMPLES,
	INTEGER_EXAMPLES,
	LIST_EXAMPLES,
	DICT_EXAMPLES
)


def test_encode_string():
	for example in STRING_EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_encode_integer():
	for example in INTEGER_EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_encode_list():
	for example in INTEGER_EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_encode_dict():
	for example in INTEGER_EXAMPLES:
		assert encode(example.decoded) == example.encoded
