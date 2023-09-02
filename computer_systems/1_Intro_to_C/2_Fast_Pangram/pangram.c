#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int ascii[26] = {
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
    char val = tolower(s[0]);
    if(val == 0){break;}
    int asc = (int) val;
    //printf("s: %p\n", s);
    //printf("val: %c\n", val);
    //printf("ascii letter: %c\n", asc);
    
    // Check if char is in seen
    bool is_seen = false;
    for (int i = 0; i<26; i++){
      if (seen[i] == val){
          //printf("SEEN: %c\n", val);
        is_seen = true;
        break;
      }
    }
    // Continue while loop if character has been seen
    if (!is_seen){
      for (int i = 0; i<26; i++){
        if (asc == ascii[i]){
            seen[i] = val;
            break;
        }
      }
    }
    bool is_finished = true;
    for (int i = 0; i<26; i++){
      if (seen[i] == 0){
        is_finished = false;
        break;
      }
    }
    if (is_finished){ break; }
    s++;
  }
  bool result = true;
  for (int i = 0; i<26;i++){
    //printf("Seen #%d: %c\n", i, seen[i]);
    if (seen[i] == 0){
      result = false;
      break;
    }
  }
  //printf("Seen set: %s\n", seen);
  return result;
}





int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  bool result;
  while ((read = getline(&line, &len, stdin)) != -1) {
    result = ispangram(line);
    if (result){
      printf("%s", line);
    } 
  }

  //printf("Result: %i", result);

  if (ferror(stdin))
    fprintf(stderr, "Error reading from stdin");

  free(line);
  fprintf(stderr, "ok\n");
}
