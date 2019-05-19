from typing import Union, List, Dict, Tuple
import re


def decode_first_string(value: bytes) -> Tuple[str, bytes]:
	pass


STRING_REGEX = re.compile(r'^(\d+):(.*)$')


def decode_string(value: bytes) -> str:
	value = value.decode()
	length, value = re.match(STRING_REGEX, value).groups()

	assert int(length) == len(value)

	return value


def decode_integer(value: bytes) -> int:
	pass


def decode_list(value: bytes) -> List[Union[str, int, List, Dict]]:
	pass


def decode_dict(value: bytes) -> Dict[str, Union[str, int, List, Dict]]:
	assert value[0] == b'd'
	assert value[-1] == b'e'


def decode(value: bytes) -> Union[str, int, List, Dict]:
	if value[0] == b'd' and value[-1] == b'e':
		return decode_dict(value)
	elif value[0] == b'l' and value[-1] == b'e':
		return decode_list(value)
	elif value[0] == b'i' and value[-1] == b'e':
		return decode_integer(value)
	else:
		return decode_string(value)
