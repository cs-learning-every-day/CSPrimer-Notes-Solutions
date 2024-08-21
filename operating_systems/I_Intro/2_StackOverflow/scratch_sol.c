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
*/

#include <stdio.h>

void f(int depth){
    printf("frame %d (%p)\n", depth, &depth);
    return f(depth + 1);
}

int main(){
    f(0);
    printf("OK\n");
}
