/*
* - vmmap tool -> Allows us to investigate the memory map of a process
* - Stack
*    - There is no compile time stack
* - Objective
*   - Write a function that will create a stackoverflow
*   - Try to get the stack frame you're up to
*   - Get a measure of where in the stack you're up to at that time
*       - You need a program with pionters
*   - What is the size of the consumed stack space
*   - Some testing
*       - What happens when you run it twice
*
*
*/
#include <stdio.h>
#include <unistd.h>
#define SLEEP_SEC 0
#define FIB_N 10 

void f(int depth, long bottom){
    /*
     * We get the frame (depth), and the pointer to the bottom of the stack frame
     * To get the size of the stack, you take the pointer to your copy of depth, which exists in the next frame of the stack, and subtract the pointer to the initial variable from it.
     *
     */
    printf("Frame %d\n", depth);
    printf("Stack Size: %ld\n", bottom - (long) &depth);
    printf("Current Depth Pointer: %p\n", &depth);
    printf("---------\n");
    f(depth+1, bottom);

}


int first(){
    /*
    * We instantiate depth at 0, and pass the pointer to that variable to f
    */
    int depth = 0;
    f(depth, (long) &depth);
    return depth;

}

int main() {
    first();
}



