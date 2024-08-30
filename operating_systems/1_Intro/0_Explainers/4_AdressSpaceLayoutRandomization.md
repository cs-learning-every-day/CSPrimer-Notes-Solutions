# Address Space Layout Randomization
- [Smashing the Stack for Fun and Profit](http://phrack.org/archives/issues/49/14.txt)
  - Guides you through how to theoretically exploit a buffer overflow vulnerability
- It's up to the user to ensure that the program does not overspend the memory buffer it is allocated
- If you realize the stack ahs the return address of any function that has been called at that point
    - You could modify the return address, and cause a function to return to your arbitrary code
- The reason this exploit worked, is b/c the stack was in a predictable location
    - Since 1996, most operating systems have implemented Address Space Layout Randomization (ASLR), which randomizes the location of the stack
- On x86 ASLR is not that effective
    - Someone who wants to figure out where the stack will start can do so


## Smashing the Stack for Fun and Profit Notes
### Introduction
- Buffer
    - Contiguous block of computer memory that holds multiple instances of the same data type
    - Also an array (character array) to a C programmer
- Static vs. Dynamic Variables
    - Static Variables
        - Allocated at load time on the data segment of the program
    - Dynamic Variables
        - Allocated at runtime on the stack
- Stack-based buffer overflows
    - Attacks that overflow dynamic buffers, i.e. buffers allocated on the stack

### Process Memory Organization
- Text
    - Fixed by the program and includes code and read-only data
- Data
    - Contains initialized and uninitialized data
    - Stores static variables
    - Corresponds to `data-bss` sections of the executable file
    - If expansion of bss data or user stack exhausts available memory, the process is blocked and rescheduled to run again with larger memory space

### Stack
- What is a stack?
    - Abstract data type that is LIFO
- Why use a stack?
    - Stack is used to:
        - Dynamically allocated the local variables used in functions
        - Pass parameters to functions
        - Return values from the function
- Stack Region
    - Stack is a contiguous block of memory containing data
    - Stack pointer register points to the top of stack
    - Bottom of stack is at a fixed address
    - Size of the stack is dynamically adjusted by the kernel at run time
    - Stack consists of logical stack frames
    - Logical Stack Frame
        - Contains:
            - Parameters to a function
            - Local variables
            - Dta necessary to recover the previous stack frame (including value of instruction pointer at the itme of the function call)
    - Stack can grow up or down, depending on the architecture
        - Stack pointer may point to the last address on the stack, or the next free available address after the stack (this assumes it is the last address on the stack)
    - Many compilers use a second register, FP, for referencing local variables and parameters
        - B/c their distances from FP do not change w/ pushes & pops

