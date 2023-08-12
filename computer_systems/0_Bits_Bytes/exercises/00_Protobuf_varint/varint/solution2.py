from functools import reduce



def encode(num: int) -> bytes:
    """
    - Take each first 7 bits as a part to encode into bytes
    - If the number is > 0, then add an MSB
    """
    out = []
    while num > 0:
        part = num & 0x7f # i.e. 0111 1111
        num >>= 7
        if num > 0:
            part |= 0x80 # i.e. 1000 0000
        out.append(part)
    return bytes(out)


def decode(varn: bytes) -> int:
    """

    for each part of the byte (reversed for big endian)
        extract the first 7 bits (ignore MSB)
        add to accumulator
    """
    n = 0 
    for x in reversed(varn):
        # Get the first 7 bits
        n <<= 7
        # Or the bits into place on the accumulator
        n |= (x & 0x7f)
    return n


if __name__ == '__main__':
    print(encode(150))
    print(decode(encode(150)))
