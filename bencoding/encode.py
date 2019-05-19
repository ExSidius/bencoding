def encode_string(value: str) -> bytes:
	"""
	Return a bencoded string.
	"""
	return f'{len(value)}:{value}'.encode()


def encode_integer(value: int) -> bytes:
	"""
	Return a bencoded integer.
	"""
	return f'i{value}e'.encode()
