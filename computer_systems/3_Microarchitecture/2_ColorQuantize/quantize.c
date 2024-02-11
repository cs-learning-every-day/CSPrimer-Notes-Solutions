/*
* CPU Microarchitecture involves branch prediction
* Branch misprediction creates a performance hit
* We want to write branchless code if the compiler can't find branchless version or the predictor
* is not well set up
* Objective:
* - Improve performance of code
* - Reduce branch misprediction
*
* Tips:
* - Try to extend understanding of why your improvements are improvements
*/

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

unsigned char quantize(
  unsigned char red, 
  unsigned char green,
  unsigned char blue
) {

  unsigned char out = 0;
  int red_remainder = red % 0x20;
  if (red >= 0xe0) {
    out += RED7;
  }
  else if (red - red_remainder != 0x00){
    out += red - red_remainder;
  }
  /*
  if (red < 0x20)
    out += RED0;
  else if (red < 0x40)
    out += RED1;
  else if (red < 0x60)
    out += RED2;
  else if (red < 0x80)
    out += RED3;
  else if (red < 0xa0)
    out += RED4;
  else if (red < 0xc0)
    out += RED5;
  else if (red < 0xe0)
    out += RED6;
  else
    out += RED7;
    */

  /*
  int green_remainder = green % 0x20;
  if (green - green_remainder != 0x00){
    int ng = (green - green_remainder) / 0x20;
    out += (ng-1) * 0x04;
  }
  */
  if (green < 0x20)
    out += GREEN0;
  else if (green < 0x40)
    out += GREEN1;
  else if (green < 0x60)
    out += GREEN2;
  else if (green < 0x80)
    out += GREEN3;
  else if (green < 0xa0)
    out += GREEN4;
  else if (green < 0xc0)
    out += GREEN5;
  else if (green < 0xe0)
    out += GREEN6;
  else
    out += GREEN7;

  /*
  int blue_remainder = blue % 0x20;
  if (blue - blue_remainder != 0x00){
    int nb = (blue - blue_remainder) / 0x20;
    out += (nb-1) * 0x01;
  }
  */

  if (blue < 0x40)
    out += BLUE0;
  else if (blue < 0x80)
    out += BLUE1;
  else if (blue < 0xc0)
    out += BLUE2;
  else
    out += BLUE3;

  return out;
}

