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
#define FIB_N 2


void print_stack_size(void *start) {
    int local_var;
    void *current_stack_pointer = &local_var;
    printf("Stack size: %ld bytes\n", (char *)start - (char *)current_stack_pointer);
    printf("Number of frames: %ld\n", ((char *)start - (char *)current_stack_pointer) / 48);
}

int fib(int n, void *start) {
    print_stack_size(start);
    if (n <= 1) {
        return n;
    }
    int left = fib(n - 1, start);
    int right = fib(n - 2, start);
    return left + right;
}

int main() {
    int local_var;
    sleep(SLEEP_SEC);
    int n = FIB_N; 
    int result = fib(n, &local_var);
    printf("Fibonacci of %d is %d\n", n, result);
}



