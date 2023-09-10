#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define STARTING_BUCKETS 8
#define MAX_KEY_SIZE 128 //TODO - THis is a random value

/*
 * Notes:
 * - Originally used to have an association list to retrieve values
 *   - A list of tuples where first value is the key
 *   - Why is this not ideal?
 *      - You have to iterate through the entire data structure
 *      - Worst case O(n)
 *   - Not terrible for small sets of data
 * - HashMap implementation
 *   - We want some key "foo" to be mapped to an integer (uint32 - doesn't really matter)
 *    - This is hashing
 *   - Properties
 *    - Integer has to be returned
 *    - Deterministic so we can look up the key reliably 
 *    - Want it to distribute well, we don't want a bunch of keys to map to the same value
 *      - At some point unavoidable, you will get hash collisions eventually
 *   - 4 billion values for Uint32
 * - Collapse the range of output values to buckets
 *   - We'll have a finite number of buckets
 *   - By hashing a key ('foo') to an integer
 *    - Then modulo on the number of buckets
 *    - Will return the value you associate with that key
 * - How many Buckets
 *    - Lots of buckets -> Reduce probability of collisions
 *    - Not so many buckets -> Waste less space
 * - Collision Resolution
 *    - Chaining
 *      - At each bucket location, instead of storing each thing
 *      - Store the beginning of a linked list
 *        - The second value is the second node in linked list
 *      - Requires:
 *        - After hashing, checking if each value 
 *      - Results in degeneration into linear time
 *        - How to address:
 *          - Increase number of buckets
 *          - Resize the linked lists
 *    - Open Addressing
 *      - As chain gets longer, it gets inefficient to traverse the linked list (b/c of memory hierarchy)
 *        - Nodes in linked lists are going to be all over memory
 *          - Won't get good cache utilization
 *      - Might be simpler if you don't want to implement LinkedLists
 *      - When you get the hash value
 *        - If there is a value, put it at the next byte
 *      - When you retrieve the value
 *        - If the value you resolve to doesn't have the right key
 *        - Look at the next byte in memory
 *      - Potential issues
 *        - What if you delete "foo" (i.e. the first value?)
 *          - You should put in a placeholder so you can still resolve to your other value in the next byte
 *        - As collisions grow, you could get a pile up on other places in memory
 *          - This leads to a massive amount of collisions
 *      - Other Schemes
 *        - Instead of putting it adjacent to the initial memory value, you put it at some other place
 *          - Stretch Goal
 *
 *
 * Plan:
 * - Requirements
 *    - Structure
 *      - buckets array where each entry is an array of void pointers size 2 (no collision handling)
 *        - void Pointer 1 -> key
 *        - void Pointer 2 -> value
 *    - Set
 *      - Take a string and convert that to uint32
 *      - Assign array of pointers to bucket where (hashed_value % n_buckets == bucket_idx)
 *    - Get
 *      - Convert string to uint32
 *      - Get bucket_idx -> (hashed_value % n_buckets)
 *      - Return pointer of value
 */



typedef struct Hashmap {
  int n_buckets;
  void **buckets;
} Hashmap;


Hashmap *Hashmap_new(){
  Hashmap *h = (Hashmap*)malloc(sizeof(Hashmap));
  h -> n_buckets = STARTING_BUCKETS;
  h -> buckets = malloc(sizeof(void*) * STARTING_BUCKETS);
  return h;
};

void Hashmap_free(Hashmap *h){
  free(h);
}

int hash_func(long x, int m){
  return x % m;
}

void Hashmap_set(Hashmap *h, char key[], void *val){
  int hash = hash_func((long)key, h->n_buckets);
  h->buckets[hash] = val;
}

void *Hashmap_get(Hashmap *h, char key[]){
  int hash = hash_func((long)key, h->n_buckets);
  return h->buckets[hash];
}

void Hashmap_delete(Hashmap *h, char key[]){
  int hash = hash_func((long)key, h->n_buckets);
  h->buckets[hash] = NULL;
}


int main() {
  struct Hashmap *h = Hashmap_new();

  // basic get/set functionality
  int a = 5;
  float b = 7.2;
  Hashmap_set(h, "item a", &a);
  Hashmap_set(h, "item b", &b);
  assert(Hashmap_get(h, "item a") == &a);
  assert(Hashmap_get(h, "item b") == &b);

  // using the same key should override the previous value
  int c = 20;
  Hashmap_set(h, "item a", &c);
  assert(Hashmap_get(h, "item a") == &c);

  // basic delete functionality
  Hashmap_delete(h, "item a");
  assert(Hashmap_get(h, "item a") == NULL);

  // handle collisions correctly
  // note: this doesn't necessarily test expansion
  int i, n = STARTING_BUCKETS * 10, ns[n];
  char key[MAX_KEY_SIZE];
  for (i = 0; i < n; i++) {
    ns[i] = i;
    sprintf(key, "item %d", i);
    Hashmap_set(h, key, &ns[i]);
  }
  for (i = 0; i < n; i++) {
    sprintf(key, "item %d", i);
    assert(Hashmap_get(h, key) == &ns[i]);
  }

  Hashmap_free(h);
  /*
     stretch goals:
     - expand the underlying array if we start to get a lot of collisions
     - support non-string keys
     - try different hash functions
     - switch from chaining to open addressing
     - use a sophisticated rehashing scheme to avoid clustered collisions
     - implement some features from Python dicts, such as reducing space use,
     maintaing key ordering etc. see https://www.youtube.com/watch?v=npw4s1QTmPg
     for ideas
     */
  printf("ok\n");
}
