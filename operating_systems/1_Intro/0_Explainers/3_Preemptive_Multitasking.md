# Pre-Emptive Multitasking
## Introduction
- On one CPU, the OS can run multiple processes at the same time.
    - But not in parallel, it switches between them.
- Timer Interrupt
    - Piece of hardware that causes running program to stop  and for the kernel to run instead

## Cooperative Multitasking
- Windows 3.1 
    - Had multitasking
    - Consumer OS designed to run on a variety of personal computers
    - Some of these PCs didn't have a timer interrupt
    - How was concurrency implemented?
        - When a program made the equivalent of a system call, the OS would check if the program had been running for a long time
        - If it had, the OS would run another program instead
    - What if the program never made a system call or yields to the OS via a sleep?
        - CPU just continues on fetch-decode-execute cycle
            - None of those instructions will yield to the OS
        - The OS would never run another program
            - The program would run forever
            - This is called a "starvation" problem
        - It required a physical reset of the computer
        - Scheme name -> Cooperative Multitasking

## Preemptive Multitasking
- This is the scheme we currenlty use
- Older OSes (than Windows 3.1) also used this
- Requires a timer interrupt
    - CPU needs a physical mechanism to stop the running program and run the kernel
- Timer Interrupt
    - Fires at regular intervals to ensure that OS responsibilities are attended to
- Example
    - Minesweeper is running
    - Timer interrupt goes off
    - Instruction pointer register is set to the kernel
    - Mode is set to kernel mode
    - Kernel code runs next

