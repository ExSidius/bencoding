from typing import Union, List, Dict, Tuple
import re


START_STRING_REGEX = re.compile(r'^(\d+):(.*)')


def decode_start_string(value: str) -> Tuple[str, str]:
	(length, remainder) = re.match(START_STRING_REGEX, value).groups()
	length = int(length)
	return remainder[:length], remainder[length:]


STRING_REGEX = re.compile(r'^(\d+):(.*)$')


def decode_string(value: str) -> str:
	length, value = re.match(STRING_REGEX, value).groups()
	assert int(length) == len(value)
	return value


START_INTEGER_REGEX = re.compile(r'^(i-?[0-9]+e).*')


def decode_start_integer(value: str) -> Tuple[int, str]:
	(integer, ) = re.match(START_INTEGER_REGEX, value).groups()
	length = len(integer)
	integer = decode_integer(integer)
	return integer, value[length:]


def decode_integer(value: str) -> int:
	assert value[0] == 'i'
	assert value[-1] == 'e'
	return int(value[1:-1])


def decode_start_list(value: str) -> Tuple[List, str]:
	assert value[0] == 'l'

	decoded_list = []

	remainder = value[1:]
	while remainder[0] != 'e':
		el, remainder = decode_start(remainder)
		decoded_list.append(el)

	return decoded_list, remainder[1:]


def decode_list(value: str) -> List[Union[str, int, List, Dict]]:
	assert value[0] == 'l'
	assert value[-1] == 'e'

	decoded_list = []

	remainder = value[1:-1]
	while remainder != '':
		el, remainder = decode_start(remainder)
		decoded_list.append(el)

	return decoded_list


def decode_start_dict(value: str) -> Tuple[Dict, str]:
	assert value[0] == 'd'

	decoded_dict = {}

	remainder = value[1:]
	while remainder[0] != 'e':
		key, remainder = decode_start_string(remainder)
		value, remainder = decode_start(remainder)
		decoded_dict[key] = value

	return decoded_dict, remainder[1:]


def decode_dict(value: str) -> Dict[str, Union[str, int, List, Dict]]:
	assert value[0] == 'd'
	assert value[-1] == 'e'

	decoded_dict = {}

	remainder = value[1:-1]
	while remainder != '':
		key, remainder = decode_start_string(remainder)
		value, remainder = decode_start(remainder)
		decoded_dict[key] = value

	return decoded_dict


def decode_start(value: str) -> Tuple[Union[str, int, List, Dict], str]:
	if value[0] == 'd':
		return decode_start_dict(value)
	elif value[0] == 'l':
		return decode_start_list(value)
	if value[0] == 'i':
		return decode_start_integer(value)
	else:
		return decode_start_string(value)


def decode(value: bytes) -> Union[str, int, List, Dict]:
	value = value.decode()

	if value[0] == 'd' and value[-1] == 'e':
		return decode_dict(value)
	elif value[0] == 'l' and value[-1] == 'e':
		return decode_list(value)
	elif value[0] == 'i' and value[-1] == 'e':
		return decode_integer(value)
	else:
		return decode_string(value)
