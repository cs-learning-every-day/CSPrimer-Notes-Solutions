#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int ascii[52] = {
  65,
  66,
  67,
  68,
  69,
  70,
  71,
  72,
  73,
  74,
  75,
  76,
  77,
  78,
  79,
  80,
  81,
  82,
  83,
  84,
  85,
  86,
  87,
  88,
  89,
  90,
  97,
  98,
  99,
  100,
  101,
  102,
  103,
  104,
  105,
  106,
  107,
  108,
  109,
  110,
  111,
  112,
  113,
  114,
  115,
  116,
  117,
  118,
  119,
  120,
  121,
  122,
};



bool ispangram(char *s) {
  // TODO implement this!
  char seen[26] = {};
  while(s){
    char val = s[0];
    int asc = (int) val;
    printf("s: %p\n", s);
    printf("val: %c\n", val);
    printf("ascii letter: %c\n", asc);
    for (int i = 0; i<52; i++){
      if (asc != ascii[i]){
          continue;
      }
      for (int i = 0; i<26; i++){
        if (seen[i] == val){
          printf("Already Seen!\n");
          break;
        }
        if (seen[i] == 0){
          printf("Unseen!\n");
          seen[i] = val;
          break;
        }
      }
    }
    if(val == 0){break;}
    s++;
  }
  bool result = true;
  for (int i = 0; i<26;i++){
    printf("Seen #%d: %c\n", i, seen[i]);
    if (seen[i] == 0){
      result = false;
    }
  }
  printf("Seen set: %s\n", seen);
  return result;
}

int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  bool result;
  while ((read = getline(&line, &len, stdin)) != -1) {
    result = ispangram(line);
    if (result)
      printf("%s", line);
  }

  printf("Result: %i", result);

  if (ferror(stdin))
    fprintf(stderr, "Error reading from stdin");

  free(line);
  fprintf(stderr, "ok\n");
}
