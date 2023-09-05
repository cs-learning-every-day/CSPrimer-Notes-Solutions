#include <stdio.h>
/*
* NOTES:
* - Registers
*   - Memory on the CPU that stores values to be operated over
* - We have other types of memory (RAM, Disk)
* - If we want to add two numbers
*   - They have to reside on the ALU
*   - Will be stored on the register
* - Not always in named registers - might be opened temporarily
* - In x86-64 you expect them to be 64 bits wide
*   - 16 general purpose registers
* - If you have a 4Ghz CPU - you're doing 4 billion things a second
*   - Each thing - i.e. adding 2 numbers together should take a quarter of a nanosecond
*   - Loading and reading from registers should take a fraction of a nanosecond
* - Going to RAM -> 50-100 nanoseconds
*   - Much slower to access than register
* - Working memory in registers is much much smaller than RAM
* - Compile flags
*   - O1 -> Make sure it goes into a register instead of the stack
*   - o -> debug flag: to step through C source code
* - Using LLDB:
*   - can step through the program
*   - Read from registers: register read
*   - You can see the value of i being dumped into a register
*       - reg re <register_name> to see this happening during debugging
*   - Useful but somewhat incorrect model of what a register is
*/



int main(){
    int i = 5;
    while (i < 10){
        i += 1;
        printf("i = %d\n", i);
    }

}
