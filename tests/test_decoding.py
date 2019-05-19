from bencoding.decode import decode
from examples import (
	Example,
	EXAMPLES,
)


def test_decode():
	for example in EXAMPLES:
		assert decode(example.encoded) == example.decoded
