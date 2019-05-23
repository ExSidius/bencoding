from typing import Union, List, Dict, Tuple


def _decode_str(value: bytes, i: int) -> Tuple[Union[str, bytes], int]:
	start = i

	while value[i] != ord(':'):
		i += 1

	length = int(value[start:i])

	i += 1
	string = value[i:i + length]
	try:
		string = string.decode()
	except UnicodeDecodeError:
		pass

	return string, i + length


def _decode_int(value: bytes, i: int) -> Tuple[int, int]:
	assert value[i] == ord('i')
	start = i

	while value[i] != ord('e'):
		i += 1

	return int(value[start + 1:i]), i + 1


def _decode_list(value: bytes, i: int) -> Tuple[List, int]:
	assert value[i] == ord('l')
	i += 1

	decoded = []
	while value[i] != ord('e'):
		item, i = _decode(value, i)
		decoded.append(item)

	return decoded, i + 1


def _decode_dict(value: bytes, i: int) -> Tuple[Dict, int]:
	assert value[i] == ord('d')
	i += 1

	decoded = {}
	while value[i] != ord('e'):
		key, i = _decode_str(value, i)
		item, i = _decode(value, i)
		decoded[key] = item

	return decoded, i + 1


def _decode(value: bytes, i: int) -> Tuple[
	Union[bytes, str, int, List, Dict], int]:
	if value[i] == ord('d'):
		return _decode_dict(value, i)
	elif value[i] == ord('l'):
		return _decode_list(value, i)
	elif value[i] == ord('i'):
		return _decode_int(value, i)
	else:
		return _decode_str(value, i)


def decode(value: bytes) -> Union[bytes, str, int, List, Dict]:
	decoded, _ = _decode(value, 0)
	return decoded
