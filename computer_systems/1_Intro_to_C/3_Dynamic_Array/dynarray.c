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
  int size;
  int capacity;
  void** values; // Pointer to an array of void pointers
} DA;

DA *DA_new(void) {
  DA *da = (DA *)malloc(sizeof(DA));
  if (!da) {
    perror("Failed to allocate memory");
    exit(1);
  }
  da->size = 0;
  da->capacity = STARTING_CAPACITY;
  da->values = malloc(sizeof(void*) * STARTING_CAPACITY);
  for (int i = 0; i < STARTING_CAPACITY; i++) {
    da->values[i] = NULL;
  }
  if (!da->values) {
    perror("Failed to allocate memory");
    exit(1);
  }
  return da;
}

int DA_size(DA *da) { return da->size; }

void DA_push(DA *da, void *x) {
  void *new_val = x;
  if (da->size >= da->capacity) {
    // Common pattern to double the array when resizing
    // Why not increase by 1?
    // If we pay the cost of copying n things, we should 
    // be able to do n subsequent pushes. This leads to an amortized
    // contant time complexity of doubling the array
    // If we increase by 1, we'll pay the cost of copying n values
    // at every push exceeding capacity
    int new_capacity = da->size * 2;
    // Increasing the size of memory allocated to da->values to the new capacity
    // to allow addition of extra element
    void **temp = realloc(da->values, sizeof(void *) * new_capacity);
    if (!temp) {
      perror("Failed to allocate memory");
      free(da->values);
      exit(1);
    }
    da->values = temp;
    da->capacity = new_capacity;
  }
  da->values[da->size] = x;
  (da->size)++;
}

void *DA_pop(DA *da) {
  if (da->size == 0)
    return NULL;
  int return_val_idx = da->size - 1;
  void *return_val = (da->values)[return_val_idx];
  da->values[return_val_idx] = NULL;
  da->size--;
  return return_val;
}

void DA_set(DA *da, void *x, int i) {
  if (i + 1 > da->capacity)
    return;
  void *initial_value = da->values[i];
  da->values[i] = x;
  // Increase size if value was previously null
  if (initial_value == NULL) {
    (da->size)++;
  };
}

void *DA_get(DA *da, int i) {
  int array_size = da->capacity;
  if (i + 1 > array_size)
    return NULL;
  return da->values[i];
}

void DA_free(DA *da) {
  // TODO deallocate anything on the heap
  free(da->values);
  free(da);
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
