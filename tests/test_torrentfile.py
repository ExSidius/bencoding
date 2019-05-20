from bencoding import encode, decode
from examples import TORRENT_EXAMPLES


def test_encode():
	for example in TORRENT_EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_decode():
	for example in TORRENT_EXAMPLES:
		assert decode(example.encoded) == example.decoded
