# bencoding - A One Stop Shop for All Your Bencoding Needs

[![Build Status](https://travis-ci.com/ExSidius/bencoding.svg?branch=master)](https://travis-ci.com/ExSidius/bencoding)
[![Coverage Status](https://coveralls.io/repos/github/ExSidius/bencoding/badge.svg)](https://coveralls.io/github/ExSidius/bencoding)

## What is Bencoding?

The BitTorrent protocol uses an efficient file format that allows you to 
transmit strings, integers, lists, and dictionaries. This is a library
that makes doing that easy while affording you luxuries from Python3.7
(such as typing).

## Installation

You can install this package using pip.

```bash
python -m pip install bencoding
```

## Tests

This library is exceedingly well tested - tests come straight from the [BitTorrent Specification]
(https://wiki.theory.org/index
.php/BitTorrentSpecification#Bencoding)
 and also from other [Bencoding libraries](https://github.com/fuzeman/bencode
 .py/blob/master/tests/bencode_tests.py).
 