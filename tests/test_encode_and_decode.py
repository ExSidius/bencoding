import time
from statistics import mean, stdev

from bencoding import encode, decode
from examples import (
	Example,
	EXAMPLES,
	encoded,
	decoded,
)


def test_encode():
	for example in EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_decode():
	for example in EXAMPLES:
		assert decode(example.encoded) == example.decoded
