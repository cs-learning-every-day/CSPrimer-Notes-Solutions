def le(bs):
    n = 0
    for i, b in enumerate(bs):
        n += (b << (i * 8))
    return n


with open('teapot.bmp', 'rb') as f:
    data = f.read()

assert data[:2] == b'BM'

offset, width, height = le(data[10:14]), le(data[18:22]), le(data[22:26])
print(offset, width, height)

pixels = []
# TODO - iterate in the expected order for rotated pixels
# Look up corresponding *source* pixel and append to `pixels`
for ty in range(width):
    for tx in range(width):
        import pdb;pdb.set_trace()
        sy = tx
        sx = width - ty - 1
        n = offset + 3 * (sy * width + sx)
        pixels.append(
            data[n:n+3]
        )



with open('out.bmp', 'wb') as f:
    f.write(data[:offset])
    f.write(
        b''.join(
            pixels
        )
    )
