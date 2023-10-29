# What is the fetch-decode-execute cycle?
- Very basic mental model of how the CPU executes
    - It is wrong
    - We'll chip away at it later on
- CPU
    - Executes instructions
    - To execute an instruction, it needs to reside on the CPU
        - You may have a specific individual register that stores one instruction
            - "Instruction register" (this is hypothetical/not real)
    - This instruction needs to be fetched from memory and pushed into the register
    - Instruction
        - Might represent that register 1 and register 2 should be added together
    - There's a decode unit in the CPU
        - Reads the instruction bits
        - Sends signals to other parts of the CPU (i.e. the ALU)
            - Communicates which registers are being read and written to and what operation should be executed over them
    - Execute Step
        - Might happen in the ALU
        - Then figure out the next instruction to run
- Program Counter (Instruction Pointer)
    - Stores the address of the next instruction to pass through the fetch-decode-execute cycle
    - Very iterative progress
- What makes the machine run?
    - The CPU clock which ticks a certain amount of times
    - 4Ghz -> 4 billion times / second
        - Cycle finishes every quarter of a nanosecond


