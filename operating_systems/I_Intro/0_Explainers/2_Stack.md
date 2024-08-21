# What is "the stack"?
## Simple Explanaiton
- Call Stack
    - Mechanism for storing values associated with funciton invocations
    - So that when you call a function, the values associated with it can be stored somewhere and retrieved after the function is done executing
- Why use a stack instead of memory/heap?
    - It's very simple to keep track of function values by simply keeping a pointer to the previous frame
