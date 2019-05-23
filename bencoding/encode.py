from collections import deque, OrderedDict
from typing import Union, List, Dict, Deque


def _encode_bytes(encoding: Deque, value: bytes):
	encoding.extend((str(len(value)).encode(), b':', value))


def _encode_str(encoding: Deque, value: str):
	encoding.extend((str(len(value)).encode(), b':', value.encode()))


def _encode_int(encoding: Deque, value: int):
	encoding.extend((b'i', str(value).encode(), b'e'))


def _encode_list(encoding: Deque, value: List):
	encoding.append(b'l')
	for item in value:
		_encode(encoding, item)
	encoding.append(b'e')


def _encode_dict(encoding: Deque,
                 value: Dict[str, Union[str, int, bytes, List, Dict]]):
	encoding.append(b'd')
	for k in sorted(value):
		_encode_str(encoding, k)
		_encode(encoding, value[k])
	encoding.append(b'e')


encode_function = {
	int: _encode_int,
	bytes: _encode_bytes,
	str: _encode_str,
	list: _encode_list,
	tuple: _encode_list,
	dict: _encode_dict,
	OrderedDict: _encode_dict,
}


def _encode(encoding: Deque, value: Union[str, int, bytes, List, Dict]):
	return encode_function[type(value)](encoding, value)


def encode(value: Union[str, int, bytes, List, Dict]) -> bytes:
	encoding = deque()
	_encode(encoding, value)
	return b''.join(encoding)
