from dataclasses import dataclass
FILE = 'teapot.bmp'


@dataclass
class BMPHeader:
    raw: bytes
    start: bytes
    file_size: bytes
    pixel_array_address: bytes
    width: bytes
    height: bytes
    color_panes: bytes
    bits_per_pixel: bytes


@dataclass
class Pixel:
    R: int
    G: int
    B: int

    def to_bytes(self) -> bytes:
        return (
            self.B.to_bytes() + self.G.to_bytes() + self.R.to_bytes() 
        )


@dataclass
class PixelMatrix:
    data: list[list[Pixel]]

    @classmethod
    def from_pixel_array(cls, pixel_array: list[Pixel]) -> "PixelMatrix":
        pixel_matrix = []
        for idx, p in enumerate(pixel_array):
            if idx % 420 == 0:
                pixel_matrix.append([])
            pixel_matrix[-1].append(p)
        return cls(data=pixel_matrix)

    @classmethod
    def create_empty_matrix(cls) -> list[list[Pixel | None]]:
        data = []
        for idx in range(420**2):
            if idx % 420 == 0:
                data.append([])
            data[-1].append(None)
        return data

    def get_pixel(self, x: int, y: int) -> Pixel:
        assert 0 <= x <= 419 and 0 <= y <= 419
        return self.data[x][y]

    def rotate_90_degrees(self) -> "PixelMatrix":
        empty_matrix = self.create_empty_matrix()
        for i in range(420):
            for j in range(420):
                x, y = translate_matrix_position(i, j)
                empty_matrix[x][y] = self.data[i][j]
        self.data = empty_matrix
        return self

    def to_bytes(self) -> bytes:
        byte_str = b''
        for row in self.data:
            for p in row:
                byte_str += p.to_bytes()
        return bytes(byte_str)


def translate_matrix_position(i: int, j: int) -> tuple[int, int]:
    return 419 - j, i


@dataclass
class PixelArray:
    data: list[Pixel]
    raw: bytes

    @classmethod
    def build(cls, data: bytes) -> "PixelArray":
        return cls(
            data=[
                Pixel(R=data[i+2], G=data[i+1], B=data[i])
                for i in range(0, len(data), 3)
            ],
            raw=data
        )

    def get_nth_pixel(self, n: int) -> Pixel:
        assert n < (len(self.data))
        return self.data[n]

    def as_matrix(self) -> "PixelMatrix":
        return PixelMatrix.from_pixel_array(self.data)


@dataclass
class BMP:
    header: BMPHeader
    pixels: PixelArray

    @classmethod
    def build(cls, data: bytes) -> "BMP":
        header = BMPHeader(
            raw=data[:138],
            start=data[:2],
            file_size=data[2:4],
            pixel_array_address=data[10:14],
            width=data[18:22],
            height=data[22:26],
            color_panes=data[26:28],
            bits_per_pixel=data[28:30],
        )
        pixels = PixelArray.build(data[138:])
        return cls(header=header, pixels=pixels)


def get_bmp(file: str) -> BMP:
    with open(file, 'rb') as f:
        data = f.read()
    return BMP.build(data)


def write_bmp_to_file(bmp: BMP, file_name='out.bmp'):
    with open(file_name, 'wb') as f:
        f.write(bmp.header.raw)
        f.write(bmp.pixels.raw)
    print(f'Wrote bitmap to file {file_name}')


def le_to_int(le: bytes) -> int:
    n = 0
    for i, b in enumerate(le):
        n += (b << (i * 8))
    return n


def rotate_bmp(bmp: BMP) -> BMP:
    x = bmp.pixels.as_matrix()
    x.rotate_90_degrees()
    return BMP(
        header=bmp.header,
        pixels=PixelArray.build(x.to_bytes())
    )


def main():
    bmp = get_bmp(FILE)

    rotated_bmp = rotate_bmp(bmp)

    write_bmp_to_file(rotated_bmp)


if __name__ == '__main__':
    main()
