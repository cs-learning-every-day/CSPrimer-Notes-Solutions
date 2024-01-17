#include <assert.h>
#include <math.h>
#include <stdio.h>

#define float_near(a, b) fabsf((a) - (b)) < 0.01

extern float volume(float radius, float height);

int main(void) {
  assert(float_near(0.0f, volume(0.0f, 0.0f)));
  // Stored in xmm0 & xmm1, in little endian format
  // Need to be reversed to be encoded 
  assert(float_near(5.89f, volume(1.5f, 2.5f)));
  assert(float_near(174.23f, volume(5.5f, 5.5f)));
  assert(float_near(9.05f, volume(1.234f, 5.678f)));
  printf("OK\n");
}
