import time
from statistics import mean, stdev

from bencoding import encode, decode
from examples import (
	Example,
	EXAMPLES,
	encoded,
	decoded,
)


def test_encode():
	for example in EXAMPLES:
		assert encode(example.decoded) == example.encoded


def test_encode_speed():
	times = []
	for i in range(100000):
		start = time.time()
		encode(decoded)
		end = time.time()
		times.append(end - start)

	agg = mean(times)
	dev = stdev(times)

	assert agg < 3.0e-05
	assert dev < 7.0e-06


def test_decode():
	for example in EXAMPLES:
		assert decode(example.encoded) == example.decoded


def test_decode_speed():
	times = []
	for i in range(10000):
		start = time.time()
		decode(encoded)
		end = time.time()
		times.append(end - start)

	agg = mean(times)
	dev = stdev(times)

	# assert agg < 2.1e-05
	# assert dev < 3.3e-06