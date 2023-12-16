#include <assert.h>
#include <stdio.h>

extern int index(int *matrix, int rows, int cols, int rindex, int cindex);

int main(void) {

  int matrix1[1][4] = {{1, 2, 3, 4}};
  assert(index((int *)matrix1, 1, 4, 0, 2) == 3);

  int matrix2[4][1] = {{1}, {2}, {3}, {4}};
  assert(index((int *)matrix2, 4, 1, 1, 0) == 2);

  int matrix3[2][3] = {{1, 2, 3}, {4, 5, 6}};
  assert(index((int *)matrix3, 2, 3, 1, 2) == 6);

  int matrix4[5][6] = {
    {1, 2, 3, 4, 5, 6}, 
    {7, 8, 9, 10, 11, 12},
    {13, 14, 15, 16, 17, 18},
    {19, 20, 21, 22, 23, 24},
    {25, 26, 27, 28, 29, 30},
  };
  assert(index((int *)matrix4, 5, 6, 3, 4) == 23);

  printf("OK\n");
}
