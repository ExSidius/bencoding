from typing import NamedTuple, Union


class Example(NamedTuple):
	encoded: bytes
	decoded: Union[str, int]


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
