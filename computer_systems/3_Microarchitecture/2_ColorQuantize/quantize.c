#define RED0 0x00
#define RED1 0x20
#define RED2 0x40
#define RED3 0x60
#define RED4 0x80
#define RED5 0xa0
#define RED6 0xc0
#define RED7 0xe0
#define GREEN0 0x00
#define GREEN1 0x04
#define GREEN2 0x08
#define GREEN3 0x0c
#define GREEN4 0x10
#define GREEN5 0x14
#define GREEN6 0x18
#define GREEN7 0x1c
#define BLUE0 0x00
#define BLUE1 0x01
#define BLUE2 0x02
#define BLUE3 0x03

unsigned char quantize(unsigned char red, unsigned char green,
                       unsigned char blue) {
  unsigned char out = 0;
  // This uses the trick that y % x -> y & (x-1) for divisors that are multiples of 2
  // Additionally replaces multiplication and division by powers of 2 with bit shifting

  out += red - (red & 0x1f);
  out += (green - (green & 0x1f)) >> 3;
  out += (blue - (blue & 0x3f)) >> 6;
  return out;
}

