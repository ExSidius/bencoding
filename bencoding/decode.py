from typing import Union, List, Dict, Tuple
import re


START_STRING_REGEX = re.compile(b'^(\d+):')


def decode_start_string(value: bytes) -> Tuple[Union[str, bytes], bytes]:
	(length, ) = re.match(START_STRING_REGEX, value).groups()
	length_len = len(length)
	remainder = value[length_len+1:]

	length = int(length)

	decoded_string = remainder[:length]
	try:
		decoded_string = decoded_string.decode()
	except UnicodeDecodeError:
		pass

	return decoded_string, remainder[length:]


STRING_REGEX = re.compile(b'^(\d+):(.*)$')


def decode_string(value: bytes) -> Union[str, bytes]:
	length, value = re.match(STRING_REGEX, value).groups()
	assert int(length) == len(value)

	try:
		value = value.decode()
	except UnicodeDecodeError:
		pass

	return value


START_INTEGER_REGEX = re.compile(b'^(i-?[0-9]+e).*')


def decode_start_integer(value: bytes) -> Tuple[int, bytes]:
	(integer, ) = re.match(START_INTEGER_REGEX, value).groups()
	length = len(integer)
	integer = decode_integer(integer)
	return integer, value[length:]


def decode_integer(value: bytes) -> int:
	assert value[0] == ord('i')
	assert value[-1] == ord('e')
	return int(value[1:-1])


def decode_start_list(value: bytes) -> Tuple[List, bytes]:
	assert value[0] == ord('l')

	decoded_list = []

	remainder = value[1:]
	while remainder[0] != ord('e'):
		el, remainder = decode_start(remainder)
		decoded_list.append(el)

	return decoded_list, remainder[1:]


def decode_list(value: bytes) -> List[Union[bytes, str, int, List, Dict]]:
	assert value[0] == ord('l')
	assert value[-1] == ord('e')

	decoded_list = []

	remainder = value[1:-1]
	while remainder != b'':
		el, remainder = decode_start(remainder)
		decoded_list.append(el)

	return decoded_list


def decode_start_dict(value: bytes) -> Tuple[Dict, bytes]:
	assert value[0] == ord('d')

	decoded_dict = {}

	remainder = value[1:]
	while remainder[0] != ord('e'):
		key, remainder = decode_start_string(remainder)
		value, remainder = decode_start(remainder)
		decoded_dict[key] = value

	return decoded_dict, remainder[1:]


def decode_dict(value: bytes) -> Dict[str, Union[bytes, str, int, List, Dict]]:
	assert value[0] == ord('d')
	assert value[-1] == ord('e')

	decoded_dict = {}

	remainder = value[1:-1]
	while remainder != b'':
		key, remainder = decode_start_string(remainder)
		value, remainder = decode_start(remainder)
		decoded_dict[key] = value

	return decoded_dict


def decode_start(value: bytes) -> Tuple[Union[bytes, str, int, List, Dict], bytes]:
	if value[0] == ord('d'):
		return decode_start_dict(value)
	elif value[0] == ord('l'):
		return decode_start_list(value)
	if value[0] == ord('i'):
		return decode_start_integer(value)
	else:
		return decode_start_string(value)


def decode(value: bytes) -> Union[bytes, str, int, List, Dict]:
	if value[0] == ord('d') and value[-1] == ord('e'):
		return decode_dict(value)
	elif value[0] == ord('l') and value[-1] == ord('e'):
		return decode_list(value)
	elif value[0] == ord('i') and value[-1] == ord('e'):
		return decode_integer(value)
	else:
		return decode_string(value)
