import struct

PATH_TO_INT_MAP = {
    "150.uint64": 150,
    #"1.uint64": 1,
    #"maxint.uint64": 18446744073709551615,
}


def main() -> None:
    #for path, _int in PATH_TO_INT_MAP.items():
    #    res = get_integer_from_binary_file(path)
    #    print(res)
    #    assert _int == res, f"{_int} != {res}"

    #    encoded_res = encode(res)
    #    print(encoded_res)

    #    decoded_res = decode(encoded_res)
    #    print(decoded_res)

    for i in range(1, int(1e9)):
        if i % 1000 == 0:
            print(f'Checking {i}')
        assert decode(encode(i)) == i

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
    decoded = []
    hex = repr.hex()
    assert len(hex) % 2 == 0
    hex_bin = hextobin(hex)
    assert len(hex_bin) % 8 == 0
    indices = _get_dropped_msb_sequence(len(hex_bin) // 8)
    dropped_msb = ''.join([
        hex_bin[i:j] for i,j in indices
    ])
    big_endian_2 = _convert_to_big_endian(dropped_msb, 7)
    return int(big_endian_2,2)

def _convert_hex_to_int(hex: str, pos: int) -> int:
    return HEX_TO_INT_MAP[hex] * 16**pos

def _get_dropped_msb_sequence(n_bytes: int):
    res = []
    for i in range(n_bytes):
        res.append([1+8*i,8+8*i]) 
    return res

def _get_big_endian_sequence(n_bytes: int):
    res = []
    for i in range(n_bytes):
        res.append([0+7*i, 7+7*i])
    return res




def _convert_to_big_endian(bin_str: str, bits: int) -> int:
    bit_sequence = _get_big_endian_sequence(len(bin_str) // bits)
    res = []
    while bit_sequence:
        begin, end = bit_sequence.pop()
        res.extend(bin_str[begin:end])
    return ''.join(res)
        



def get_integer_from_binary_file(path: str) -> int:
    hex_integer = read_integer_from_file(path)
    print(hex_integer)
    return _interpret_hex_string_as_int(hex_integer)


def _interpret_hex_string_as_int(hex: bytes) -> int:
    return struct.unpack(">Q", hex)[0]

def hextobin(hs: str):
    try:
        return bin(int(hs, 16))[2:].zfill(len(hs) *4)
    except:
        import pdb;pdb.set_trace()

def read_integer_from_file(file: str) -> bytes:
    with open(file, "rb") as f:
        return f.read()


if __name__ == "__main__":
    main()
