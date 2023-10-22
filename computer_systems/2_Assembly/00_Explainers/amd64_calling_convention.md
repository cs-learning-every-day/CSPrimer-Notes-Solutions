# System V AMD64 Calling Convention
- We need a convention for how to call functions on the OS
    - One piece of code should be able to set up arguments such that when it jumps to another piece of code, the code can be executed from there and knows in which registers to look into, what to do with the register values and how to return values
- System V AMD64 convention is used for all unix-derived systems
    - Windows is quite different
- Argument Register Overview
    - Integer/Pointer Arguments (1-6)
        - RDI
        - RSI
        - RDX
        - RCX
        - R8
        - R9
    - Floating Point Arguments (1-8)
        - XMM0-XMM7
    - Excess Arguments 
        - Stack
        - Is it slower to put 7th,8th,etc. args here?
            - Kind of yes
            - We have good cache utilization for the stack
            - But the stack is fundamentally stored on the main memory (RAM), for which a roundtrip takes 50-100 nanoseconds, vs. the ~nanosecond retrieval from the register
            - Aside
                - Go is moving to a register-based calling convention for Go functions
                    - 5-10% improvement in throughput 
- Example
```c
int foo(int a, int b, int c, int d, int e, int f, int g) {
    return a + b + c + d + e + f + g;
}
```
- Results in the following machine code
```asm
foo:
    lea eax, [rdi + rsi]
    add eax, edx
    add eax, ecx
    add eax, r8d
    add eax, r9d
    add eax, dword ptr [rsp + 8]
    ret
```
- What does `dword ptr [rsp + 8]` do?
    - It's a memory dereference operation
    - `rsp` register is the stack pointer in x86-64, points to the top of the stack
        - By adding 8 to the value in `rsp`, we reference a location that is 8 bytes above the current top of the stack
    - `rsp` will hold the return address, i.e. the address in memory where the result of the function should be returned to
- How do you go back to a calling function from a called function?
    - How does the function know where to return to?
    - The return address is saved on the stack, which `ret` will pop off the stack and return the value to
- NOTE
    - To use the following registers
        - RBX
        - RSP
        - RBP
        - R12-R15
    - You need to restore the original values before returning control to the caller
        - The caller (i.e. the process calling your function) expects these to remain the same
        - When the caller is making a function call, it puts the values it wants to hold on to during function execution onto the stack and popping off again
    - Generally avoid using them as the callee
        - If you do need them:
            - Push their values to the stack first
            - Then use them with your values
            - Then pop the values off the stack and restore the original values before returning
    - This is why Oz usually just uses ax / cx and skips bx as the general register to use

