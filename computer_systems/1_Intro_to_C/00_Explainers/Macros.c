#include <stdio.h>
#define FOO 5
#define square(x) (x) * (x)
// Enables the modulation of program logic to
// add additional print statements for example
#define DEBUG 1
/*
* NOTES:
* - C Preprocessor 
*   - Replaces FOO with 5 at compile time
*   - Same with function definitions
* - Important to use paranthesis a lot 
*   - B/c order of operations can mess with you 
*     when you're doing string replacement like this
*   - See the case of square(5) vs. square(5 + 1)
* - 
*
*/

int bar(){
    #if DEBUG == 1
        fprintf(stderr, "error\n");
    #endif
    return square(5 + 1);
}

