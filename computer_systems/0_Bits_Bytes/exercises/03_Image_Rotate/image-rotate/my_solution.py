from tqdm import tqdm
FILE = 'teapot.bmp'

with open(FILE, 'rb') as f:
    data = f.read()

def _le_to_int(le: bytes) -> int:
    n = 0
    for i, b in enumerate(le):
        n += (b << (i * 8))
    return n


START_HEADER = data[:2]
FILE_SIZE = data[2:4]
PIXEL_ARRAY_ADDRESS = data[10:14]
BITMAP_WIDTH = data[18:22]
BITMAP_HEIGHT = data[22:26]
COLOR_PANES = data[26:28]
BITS_PER_PIXEL = data[28:30]

HEADER = data[:138]
PIXEL_ARRAY = data[138:]

with open('black.bmp','wb') as f:
    f.write(HEADER)
    f.write(bytes(0x00 for _ in PIXEL_ARRAY))


