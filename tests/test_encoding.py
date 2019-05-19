from bencoding.encode import encode
from examples import (
	Example,
	EXAMPLES,
)


def test_encode():
	for example in EXAMPLES:
		assert encode(example.decoded) == example.encoded
