/*
* - Stack overflow is achieved by recursing infinitely
* - Segmentation Fault
*   - Stack is a memory segment (region)
*       - Segment is a holdover from a virtual memory system that is deprecated
*   - We don't have permission to access the location in memory we try to access, which causes a seg fault
* - We expect the pointer to the local variable to decrease as stack frames increase
*   - By convention on Unix, the stack was designed to start at low addresses and grow to smaller addresses
*   - For legacy reasons that have to do with the limits of earlier systems
*   - This is not done in Windows and is somewhat arbitrary at this stage
* - On my system, we see that each stack frame takes 48 bytes
*
* - Investigation
*   - On rerun, are the variables placed in the same space in Memory?
*       - No, b/c of Address Space Layout Randomization (ASLR)
*           - This is a security mesure
*           - Having non-deterministic starting stack locations mitigates certain types of vulnerabilities
*           - You could turn it off, and you'd allocate to the same space in memory
*       - Can stacks overlap if you run it two instances of the program?
*           - They can overlap, b/c they are virtual addresses that the OS maps from the virtualized address within the process to the actual physical memory
*           - So even if they overlap, they would never collide even though it may look like they access the same sections of memory
*               - Because under the hood these are being mapped to different areas of memory
*   - You may get areas of memory that aren't even addressable on your system
*       - I.e. an address of 0x7ff700000000 on a physical system implies that you have at least 140698 gigabytes of memory, far beyond current capabilities
*       - This makes sense becaues these are virtual addresses, taken from a given range that is mapped to the physical address space. 
*           - This virtual space does not correspond to how much physical memory is taken up, so a value such as the above is reasonable in this context
*   - What is the limit of the stack space?
*       - You can check this from vmmap output
*   - Multithreading & the Stack
*       - What happens if you only have 1 stack for 1 process?
*       - If you have multiple threads, you need multiple stacks
*       - B/c each thread will need to make its own function calls, and therefore need to maintain a stack of its own
*/

#include <stdio.h>
#include <unistd.h>

void f(int depth, long bottom){
    if (depth % 1 == 0){
        printf(
            "[pid %d] frame %d %ld (%p)\n", 
            getpid(),
            depth, 
            bottom - (long)&depth, 
            &depth
        );
    }
    for(;;);
    return f(depth + 1, bottom);
}

void start(){
    int depth = 0;
    /*
    * Passing the address of the local variable depth
    */
    f(depth, (long) &depth);
}

int main(){
    start();
    printf("OK\n");
}
