HEX_TO_INT_MAP = {
    **{str(i): i for i in range(0, 10)},
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

PATH_TO_INT_MAP = {
    '150.uint64': 150,
    '1.uint64': 1,
}


def main() -> None:
    for path, _int in PATH_TO_INT_MAP.items():
        res = get_integer_from_binary_file(path)
        assert _int == res, f"{_int} != {res}"


def get_integer_from_binary_file(path: str) -> int:
    hex_integer = read_integer_from_file(path)
    hex_string = hex_integer.hex()
    return _interpret_hex_string_as_int(hex_string)


def _interpret_hex_string_as_int(hex: str) -> int:
    val = 0
    len_str = len(hex)
    for i, v in enumerate(hex):
        val += HEX_TO_INT_MAP[v] * 16**(len_str-i-1)
    return val


def read_integer_from_file(file: str) -> bytes:
    with open(file, 'rb') as f:
        return f.read()


if __name__ == '__main__':
    main()
