from helpers import Example
from bencoding.encode import encode_string


def test_encode_string():
	examples = [Example(decoded=d, encoded=e) for d, e in [
		('', b'0:'),
		('spam', b'4:spam'),
		('parrot sketch', b'13:parrot sketch'),
	]]

	for example in examples:
		assert encode_string(example.decoded) == example.encoded
