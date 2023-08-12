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
for ty in range(width):
    for tx in range(height):
        new_coordinates = (sy, sx) = tx, width - ty - 1
        # This translates the 2D coordinate on the x,y plane
        # to an index in a 1-D array
        # This can also be computed as follows: new_idx = sy + sx * height
        #new_idx = sy * width + sx
        new_idx = sy + sx * height
        n = offset + 3 * new_idx
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
