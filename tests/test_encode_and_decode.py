from examples import (
	EXAMPLES,
)

from bencoding import encode, decode


def test_encode():
	for example in EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_decode():
	for example in EXAMPLES:
		assert decode(example.encoded) == example.decoded
