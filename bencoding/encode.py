def encode_string(value: str) -> bytes:
	"""
	Return a bencoded string.
	"""
	return f'{len(value)}:{value}'.encode()

