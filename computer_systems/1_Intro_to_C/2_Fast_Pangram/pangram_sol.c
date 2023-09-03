#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define MASK 0x07fffffe

/*
* NOTES
* - Want to check for the presence of 26 bits
* - Most compact -> 26 bits can be represented by a 32 bit integer
* - When you can conserve space you can conserve time 
*   - Integers can be saved in register and we can save trips to RAM
*   - You can't just think of asymptotic complexity, also physical
*     time spent accessing memory
* - Plan
*   - bs = 0 // bitset
*   - for ch in s:
*     - if ch is not a-z
*       - continue
*     - ch = ch.lower()
*     - bs |= 1 << (ch - 'a') // 0-25 inclusive
*   - return bs == 0x03ffffff
*     - Why 03 as the leading part when we use ff to denote 8 bits on?
*     - 03 (hex) -> 11 (binary)
*       - Therefore 0x 03 ff ff ff corresponds to
*         - 00000011 11111111 11111111 11111111
*
*/

bool ispangram(char *s) {
  int bs = 0;
  while(s){
    char val = tolower(s[0]);
    if(val == 0){break;}
    int asc = (int) val;
    if (!(asc > 96 && asc < 123)){
      s++;
      continue;
    }
    bs |= 1 << (val - 'a');
    s++;
  }

  bool result = bs == 0x03ffffff;
  return result;
}


bool ispangram_sol(char *s) {
  // REVIEW THIS
  uint32_t bs = 0;
  char c;
  // The below only increments after dereferencing s
  // equivalent to c = tolower(*s); s++
  while ((c = *s++) != '\0'){
    if (c < '@') continue; // ignore first 64 chars in ASCII
    // Mask the last 5 order bits
    bs |= 1 << (c & 0x1f);
  }
  return (bs & MASK) == MASK;

}





int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  bool result;
  while ((read = getline(&line, &len, stdin)) != -1) {
    result = ispangram_sol(line);
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
