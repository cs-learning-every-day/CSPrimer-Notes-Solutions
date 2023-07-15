import struct

PATH_TO_INT_MAP = {
    "150.uint64": 150,
    #"1.uint64": 1,
    #"maxint.uint64": 18446744073709551615,
}


def main() -> None:
    for path, _int in PATH_TO_INT_MAP.items():
        res = get_integer_from_binary_file(path)
        print(res)
        assert _int == res, f"{_int} != {res}"

        encoded_res = encode(res)
        print(encoded_res)

        decoded_res = decode(encoded_res)
        print(decoded_res)


def encode(num: int) -> None:
    """
    while n > 0:
        take lowest order 7 bits
        add the correct msb: 1 unless final 7 bits
        push to some sequence of bytes
        reduce n by 7 bits
    return byte_sequence
    """
    out = []
    while num > 0:  # TODO - maybe aviod double checking
        # Retrieving the first 7 bits from the integer
        part = num % 128  # TODO - Bitmask for performance
        # Bit shifting (i.e. removing) 7 bits from the integer
        num >>= 7
        if num > 0:
            part |= 0x80
        out.append(part)
    return bytes(out)

HEX_TO_INT_MAP = {
    **{str(i): i for i in range(10)},
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

def decode(repr: bytes) -> int:
    hex = repr.hex()
    while hex:
        hex_part = int(hex[:2])
    return hex_part

def _convert_hex_to_int(hex: str, pos: int) -> int:
    return HEX_TO_INT_MAP[hex] * 16**pos


def get_integer_from_binary_file(path: str) -> int:
    hex_integer = read_integer_from_file(path)
    print(hex_integer)
    return _interpret_hex_string_as_int(hex_integer)


def _interpret_hex_string_as_int(hex: bytes) -> int:
    return struct.unpack(">Q", hex)[0]


def read_integer_from_file(file: str) -> bytes:
    with open(file, "rb") as f:
        return f.read()


if __name__ == "__main__":
    main()
