from typing import NamedTuple, Union, List, Dict


class Example(NamedTuple):
	encoded: bytes
	decoded: Union[
				str,
				int,
				List[str, int, List, Dict],
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
		}, b'd3:bar4:spam3:fooi42ee')
	]
]