from typing import NamedTuple, Union, List, Dict
import pickle

class Example(NamedTuple):
	encoded: bytes
	decoded: Union[
				str,
				int,
				List[Union[str, int, List, Dict]],
				Dict[str, Union[str, int, List, Dict]]
			]


STRING_EXAMPLES = [Example(decoded=d, encoded=e) for d, e in [
		('', b'0:'),
		('spam', b'4:spam'),
		('parrot sketch', b'13:parrot sketch'),
]]

INTEGER_EXAMPLES = [Example(decoded=d, encoded=e) for d, e in [
	(0, b'i0e'),
	(-0, b'i0e'),
	(1, b'i1e'),
	(10, b'i10e'),
	(42, b'i42e'),
	(-42, b'i-42e'),
	(3, b'i3e'),
	(-3, b'i-3e'),
]]

LIST_EXAMPLES = [
	Example(decoded=d, encoded=e) for d, e in [
		([], b'le'),
		(['spam', 'eggs'], b'l4:spam4:eggse'),
		(['parrot sketch', 42], b'l13:parrot sketchi42ee'),
		([[1, 2, 3], [4, 5, 6]], b'lli1ei2ei3eeli4ei5ei6eee'),
	]
]

DICT_EXAMPLES = [
	Example(decoded=d, encoded=e) for d, e in [
		({}, b'de'),
		({
			'publisher': 'bob',
			'publisher-webpage': 'www.example.com',
			'publisher.location': 'home',
		},
			b'd9:publisher3:bob17:publisher-webpage15:www.example.com'
			b'18:publisher.location4:homee'),
		({
			'spam': ['a', 'b'],
		},
			b'd4:spaml1:a1:bee'),
		({
			'cow': 'moo',
			'spam': 'eggs',
		}, b'd3:cow3:moo4:spam4:eggse'),
		({
			 'foo': 42,
			 'bar': 'spam'
		}, b'd3:bar4:spam3:fooi42ee'),
		({
			'level1': {
				'level2': 'banana',
			}
		}, b'd6:level1d6:level26:bananaee')
	]
]


with open('tests/ubuntu-18.04.2-desktop-amd64.iso.torrent.pickle', 'rb') as file:
	decoded = pickle.load(file)
with open('tests/ubuntu-18.04.2-desktop-amd64.iso.torrent', 'rb') as file:
	encoded = file.read()
TORRENT_EXAMPLES = [
	Example(decoded=decoded, encoded=encoded)
]

EXAMPLES = STRING_EXAMPLES + INTEGER_EXAMPLES + LIST_EXAMPLES + DICT_EXAMPLES
