from typing import Union, List, Dict


def encode_bytes(value: bytes) -> bytes:
	return b'%d:%b' % (len(value), value)


def encode_string(value: str) -> bytes:
	return f'{len(value)}:{value}'.encode()


def encode_integer(value: int) -> bytes:
	return b'i%de' % value


def encode_list(value: List[Union[str, int, List, Dict]]) -> bytes:
	return b'l%be' % b''.join(encode(v) for v in value)


def encode_dict(value: Dict[str, Union[str, int, List, Dict]]) -> bytes:
	value = {k:value[k] for k in sorted(value)}
	return b'd%be' % b''.join(b'%b%b' % (encode_string(k), encode(v))
	                          for k, v in value.items())


def encode(value: Union[str, int, List, Dict]) -> bytes:
	if isinstance(value, str):
		return encode_string(value)
	elif isinstance(value, int):
		return encode_integer(value)
	elif isinstance(value, list):
		return encode_list(value)
	elif isinstance(value, dict):
		return encode_dict(value)
	elif isinstance(value, bytes):
		return encode_bytes(value)
	else:
		raise Exception(f'{type(value)} is an unsupported type.')
