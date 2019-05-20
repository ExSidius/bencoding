from typing import Union, List, Dict


def encode_bytes(value: bytes) -> bytes:
	return f'{len(value)}'.encode() + b':' + value


_encode_bytes = encode_bytes


def _encode_string(value: str) -> str:
	return f'{len(value)}:{value}'


def encode_string(value: str) -> bytes:
	return _encode_string(value).encode()


def _encode_integer(value: int) -> str:
	return f'i{value}e'


def encode_integer(value: int) -> bytes:
	return _encode_integer(value).encode()


def _encode_list(value: List[Union[str, int, List, Dict]]) -> str:
	return f"l{''.join([_encode(v) for v in value])}e"


def encode_list(value: List[Union[str, int, List, Dict]]) -> bytes:
	return _encode_list(value).encode()


def _encode_dict(value: Dict[str, Union[str, int, List, Dict]]) -> str:
	return f"d{''.join([f'{len(k)}:{k}{_encode(v)}' for k, v in value.items()])}e"


def encode_dict(value: Dict[str, Union[str, int, List, Dict]]) -> bytes:
	value = {k: value[k] for k in sorted(value)}
	return _encode_dict(value).encode()


def _encode(value: Union[str, int, List, Dict]) -> Union[str, bytes]:
	if isinstance(value, str):
		return _encode_string(value)
	elif isinstance(value, int):
		return _encode_integer(value)
	elif isinstance(value, list):
		return _encode_list(value)
	elif isinstance(value, dict):
		return _encode_dict(value)
	elif isinstance(value, bytes):
		return _encode_bytes(value)
	else:
		raise Exception(f'{type(value)} is an unsupported type.')


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
