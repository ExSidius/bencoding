from examples import TORRENT_EXAMPLES

from bencoding import encode, decode


def test_encode():
	for example in TORRENT_EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_decode():
	for example in TORRENT_EXAMPLES:
		assert decode(example.encoded) == example.decoded
