#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define STARTING_CAPACITY 8

/*
* NOTES
* - Array of 3 integers
*   - Each integer will be 4 bytes long (32 bits each)
*   - To access the index 2 it needs to compute
*     - arr_address + 2 * size(byte)
*       - In many architectures this is a single instruction
*     - Allows constant time indexing
*       - As long as you have fixed size
*
*
*/

typedef struct DA {
  // TODO define our struct
  int s;
} DA;


DA* DA_new (void) {
  // TODO allocate and return a new dynamic array
  struct DA DA_new = { 0 };
  return &DA_new;
}

int DA_size(DA *da) {
  // TODO return the number of items in the dynamic array
  return (*da).s;
}

void DA_push (DA* da, void* x) {
  // TODO push to the end
}

void *DA_pop(DA *da) {
  // TODO pop from the end
}

void DA_set(DA *da, void *x, int i) {
  // TODO set at a given index, if possible
}

void *DA_get(DA *da, int i) {
  // TODO get from a given index, if possible
}


void DA_free(DA *da) {
  // TODO deallocate anything on the heap
}

int main() {
    DA* da = DA_new();
    printf("%d\n", (*da).s);

    int size = DA_size(da);
    printf("%d\n", size);
    assert(DA_size(da) == 0);

    // basic push and pop test
    int x = 5;
    float y = 12.4;
    DA_push(da, &x);
    DA_push(da, &y);
    assert(DA_size(da) == 2);

    assert(DA_pop(da) == &y);
    assert(DA_size(da) == 1);

    assert(DA_pop(da) == &x);
    assert(DA_size(da) == 0);
    assert(DA_pop(da) == NULL);

    // basic set/get test
    DA_push(da, &x);
    DA_set(da, &y, 0);
    assert(DA_get(da, 0) == &y);
    DA_pop(da);
    assert(DA_size(da) == 0);

    // expansion test
    DA *da2 = DA_new(); // use another DA to show it doesn't get overriden
    DA_push(da2, &x);
    int i, n = 100 * STARTING_CAPACITY, arr[n];
    for (i = 0; i < n; i++) {
      arr[i] = i;
      DA_push(da, &arr[i]);
    }
    assert(DA_size(da) == n);
    for (i = 0; i < n; i++) {
      assert(DA_get(da, i) == &arr[i]);
    }
    for (; n; n--)
      DA_pop(da);
    assert(DA_size(da) == 0);
    assert(DA_pop(da2) == &x); // this will fail if da doesn't expand

    DA_free(da);
    DA_free(da2);
    printf("OK\n");
}
