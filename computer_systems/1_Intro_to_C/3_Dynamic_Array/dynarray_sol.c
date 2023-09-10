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
  //How to get around knowing what type each value is
  //Here it's based on context: we're just passing ints and floats
  //In practice -> You may define an "Object" struct which contains
  //a field specifying the type of the value contained in the struct
  void **items;
  int length; // number of items
  int capacity; // 8
} DA;

DA *DA_new(void) {
  DA* da = malloc(sizeof(DA));
  da->length = 0; //not technically necessary, initial value is 0
  da->capacity = STARTING_CAPACITY;
  da->items = malloc(sizeof(void*) * STARTING_CAPACITY);
  return da;
}

void DA_free(DA *da) {
  free(da->items);
  free(da);
}


int DA_size(DA *da) { 
  return da->length;
}

void DA_push(DA *da, void *x) {
  if (da->length == da->capacity){
    da-> capacity <<= 1;
    da->items = realloc(da->items, da->capacity * sizeof(void*));
  }
  da->items[da->length++] = x;
}

void *DA_pop(DA *da) {
  if (da->length <= 0) return NULL;
  return da->items[--da->length];
}

void DA_set(DA *da, void *x, int i) {
  da->items[i] = x;
}

void *DA_get(DA *da, int i) {
  return da->items[i];
}



int main() {
  DA *da = DA_new();

  int size = DA_size(da);
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

  int test = 100;
  DA_set(da, &test, 799);
  assert(DA_get(da, 799) == &test);

  DA_free(da);
  DA_free(da2);
  printf("OK\n");
}
