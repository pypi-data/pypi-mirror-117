# Simple Hexdump

A simple hexdump module for Python.

## Installation

The preferred installation method is:

```
pip install simple-hexdump
```

But you can also simply copy-paste the `hexdump` class.

## Usage

```python
# Python 2
data = "".join([chr(x) for x in range(256)])
# Python 3
data = bytes(range(256))

from hexdump import hexdump
print(hexdump(data))
```

```
00000000  00 01 02 03 04 05 06 07  08 09 0a 0b 0c 0d 0e 0f  |................|
00000010  10 11 12 13 14 15 16 17  18 19 1a 1b 1c 1d 1e 1f  |................|
00000020  20 21 22 23 24 25 26 27  28 29 2a 2b 2c 2d 2e 2f  | !"#$%&'()*+,-./|
00000030  30 31 32 33 34 35 36 37  38 39 3a 3b 3c 3d 3e 3f  |0123456789:;<=>?|
00000040  40 41 42 43 44 45 46 47  48 49 4a 4b 4c 4d 4e 4f  |@ABCDEFGHIJKLMNO|
00000050  50 51 52 53 54 55 56 57  58 59 5a 5b 5c 5d 5e 5f  |PQRSTUVWXYZ[\]^_|
00000060  60 61 62 63 64 65 66 67  68 69 6a 6b 6c 6d 6e 6f  |`abcdefghijklmno|
00000070  70 71 72 73 74 75 76 77  78 79 7a 7b 7c 7d 7e 7f  |pqrstuvwxyz{|}~.|
00000080  80 81 82 83 84 85 86 87  88 89 8a 8b 8c 8d 8e 8f  |................|
00000090  90 91 92 93 94 95 96 97  98 99 9a 9b 9c 9d 9e 9f  |................|
000000a0  a0 a1 a2 a3 a4 a5 a6 a7  a8 a9 aa ab ac ad ae af  |................|
000000b0  b0 b1 b2 b3 b4 b5 b6 b7  b8 b9 ba bb bc bd be bf  |................|
000000c0  c0 c1 c2 c3 c4 c5 c6 c7  c8 c9 ca cb cc cd ce cf  |................|
000000d0  d0 d1 d2 d3 d4 d5 d6 d7  d8 d9 da db dc dd de df  |................|
000000e0  e0 e1 e2 e3 e4 e5 e6 e7  e8 e9 ea eb ec ed ee ef  |................|
000000f0  f0 f1 f2 f3 f4 f5 f6 f7  f8 f9 fa fb fc fd fe ff  |................|
00000100
```

## Examples

`hexdump()` accepts `str` for Python 2, and `bytes` / `bytearray` for Python 3.

```python
# Python 2
data = "hello world"
print(hexdump(data))
```

```
00000000  68 65 6c 6c 6f 20 77 6f  72 6c 64                 |hello world     |
0000000b
```

```python
# Python 3
data = b"hello world"
print(hexdump(data))
```

```
00000000  68 65 6c 6c 6f 20 77 6f  72 6c 64                 |hello world     |
0000000b
```

```python
# Python 3
data = bytearray(16)
print(hexdump(data))
```

```
00000000  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000010
```

Other types like `array.array` need to be converted beforehand.

```python
import array
data = array.array("I", range(8))

# Python 2
print(hexdump(data.tostring()))
# Python 3
print(hexdump(data.tobytes()))
```

```
00000000  00 00 00 00 01 00 00 00  02 00 00 00 03 00 00 00  |................|
00000010  04 00 00 00 05 00 00 00  06 00 00 00 07 00 00 00  |................|
00000020
```

Calling `str()` or `repr()` will return a `str` with new lines included.

```python
# Python 3
import sys
data = b"Hello world"
print(hexdump(data), file=sys.stderr)
```

```
00000000  48 65 6c 6c 6f 20 77 6f  72 6c 64                 |Hello world     |
0000000b
```

If the lines need to be printed separately, `hexdump()` can also be iterated.

```python
# Python 3
import logging
logging.basicConfig(level=logging.DEBUG)
for line in hexdump(data):
    logging.debug(line)
```

```
DEBUG:root:00000000  48 65 6c 6c 6f 20 77 6f  72 6c 64                 |Hello world     |
DEBUG:root:0000000b
```

Repeating lines are replaced by a single asterisk to shorten the output.

```python
# Python 3
data = b"".join([bytes([x] * 0x1000) for x in range(8)])
hexdump(data)
```

```
00000000  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00001000  01 01 01 01 01 01 01 01  01 01 01 01 01 01 01 01  |................|
*
00002000  02 02 02 02 02 02 02 02  02 02 02 02 02 02 02 02  |................|
*
00003000  03 03 03 03 03 03 03 03  03 03 03 03 03 03 03 03  |................|
*
00004000  04 04 04 04 04 04 04 04  04 04 04 04 04 04 04 04  |................|
*
00005000  05 05 05 05 05 05 05 05  05 05 05 05 05 05 05 05  |................|
*
00006000  06 06 06 06 06 06 06 06  06 06 06 06 06 06 06 06  |................|
*
00007000  07 07 07 07 07 07 07 07  07 07 07 07 07 07 07 07  |................|
*
00008000
```

Finally, if data comes from a memory dump, you can specify the start address.

```python
# Python 3
data = bytes(range(256))
hexdump(data, 0xdeadb000)
```

```
deadb000  00 01 02 03 04 05 06 07  08 09 0a 0b 0c 0d 0e 0f  |................|
deadb010  10 11 12 13 14 15 16 17  18 19 1a 1b 1c 1d 1e 1f  |................|
deadb020  20 21 22 23 24 25 26 27  28 29 2a 2b 2c 2d 2e 2f  | !"#$%&'()*+,-./|
deadb030  30 31 32 33 34 35 36 37  38 39 3a 3b 3c 3d 3e 3f  |0123456789:;<=>?|
deadb040  40 41 42 43 44 45 46 47  48 49 4a 4b 4c 4d 4e 4f  |@ABCDEFGHIJKLMNO|
deadb050  50 51 52 53 54 55 56 57  58 59 5a 5b 5c 5d 5e 5f  |PQRSTUVWXYZ[\]^_|
deadb060  60 61 62 63 64 65 66 67  68 69 6a 6b 6c 6d 6e 6f  |`abcdefghijklmno|
deadb070  70 71 72 73 74 75 76 77  78 79 7a 7b 7c 7d 7e 7f  |pqrstuvwxyz{|}~.|
deadb080  80 81 82 83 84 85 86 87  88 89 8a 8b 8c 8d 8e 8f  |................|
deadb090  90 91 92 93 94 95 96 97  98 99 9a 9b 9c 9d 9e 9f  |................|
deadb0a0  a0 a1 a2 a3 a4 a5 a6 a7  a8 a9 aa ab ac ad ae af  |................|
deadb0b0  b0 b1 b2 b3 b4 b5 b6 b7  b8 b9 ba bb bc bd be bf  |................|
deadb0c0  c0 c1 c2 c3 c4 c5 c6 c7  c8 c9 ca cb cc cd ce cf  |................|
deadb0d0  d0 d1 d2 d3 d4 d5 d6 d7  d8 d9 da db dc dd de df  |................|
deadb0e0  e0 e1 e2 e3 e4 e5 e6 e7  e8 e9 ea eb ec ed ee ef  |................|
deadb0f0  f0 f1 f2 f3 f4 f5 f6 f7  f8 f9 fa fb fc fd fe ff  |................|
deadb100
```
