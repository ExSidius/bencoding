from bencoding.decode import decode
from examples import (
	Example,
	STRING_EXAMPLES,
	INTEGER_EXAMPLES,
	LIST_EXAMPLES,
	DICT_EXAMPLES
)


def test_decode_string():
	for example in STRING_EXAMPLES:
		assert decode(example.encoded) == example.decoded


def test_decode_integer():
	for example in INTEGER_EXAMPLES:
		assert decode(example.encoded) == example.decoded


def test_decode_list():
	for example in LIST_EXAMPLES:
		assert decode(example.encoded) == example.decoded


def test_decode_dict():
	for example in DICT_EXAMPLES:
		assert decode(example.encoded) == example.decoded
