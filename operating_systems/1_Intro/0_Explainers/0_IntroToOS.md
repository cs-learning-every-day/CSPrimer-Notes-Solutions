# Introduction to Operating Systems: Exploring Syscalls as the Interface
## Introduction
### Objectives
- What the kernel is
- What is some of the functionality it provides
- How does it provide it

### Kernel Responsibilities
- Mediation of I/O Devices + Driver Code
    - Drivers
        - Code that is part of the kernel that interfaces with particular hardware
        - Modular and specific to the hardware (i.e. Logitech mouse driver)
        - Why should the kernel provdide this?
            - Why not have this available as a library?
            - Reasons
                - Security / Protection so that processes can't conflict in accessing it
                - Mediated access to hardware 
                    - As OS has more and more concurrent processes
                    - Enables permission management, it ensures that the hardware is not accessed by unauthorized processes
    - Types of I/O managed
        - Disk (SSD)
        - Networking
        - Keyboard
        - Display
        - Mouse
- Process management (mediating access to CPU)
    - Orginitation/launching of processes
    - Lifecycle management
        - Should other processes be notified if something changes in other processes?
    - Signalling/IPC
        - Interprocess communication
    - Scheduling
        - Fairness
        - Interactive processes prioritized
        - Multicore
- Access to RAM?
- All Kernel Responsibilities are effectively defined by the system calls that the kernel provides

## Tracing System Calls
- Simplest way to interact with I/O (stdout, stdin, stderr)
```c
#include <stdio.h>
int main() {
    printf("%s", "hello"); // Writing to stdout
    return 0;
}
```
- Why is this I/O?
    - Historically, the terminal was considered external to the core compute system
    - The terminal was the "terminal node" that we accessed via a console plugged into the mainframe
    - Within this context, it makes sense to think of writing to stdout as I/O, even if it doesn't feel as such intuitively
- What is asked of the OS here?
    - The `write` system call is accesse
        - `man 2 <command>` gives access to system calls
    - Our `main` function invokes this system call
        - `ssize_t write(int fd, const void *buf, size_t count);`
            - `fd` -> file descriptor
            - `*buf` -> buffer (i.e. pointer to the buffer containing the string hello)
            - `count` -> number of bytes to write (length of the string "hello")
- `strace` command
    - `strace ./a.out`
    - This command will show all the system calls that are invoked by the program
    - Among other things will show the `write` system call for the program above
    - Also includes the exit system call
        - `exit_group(0) = ?`
        - Why have an exit system call?
            - Explicit handoff between kernel and the process
            - Indicates that the process no longer needs access to resources like CPU/RAM, and that the kernel can reclaim them
        - What would happen if we didn't have this?
            - You can run out of instructions
            - Program counter can go into weird memories
            - Illegal instructions
            - Segfault
        - Fundamental part of the OS lifecycle management
        - Where does the `exit` call come from?
            - The fact that we get the exit call in the strace output means that the `exit` is not invoked by the kernel, it must be part of the user code
    - Running this over a dummy scratch.py file
        - Uses `openat` system call to access the file to get a file descriptor
        - From looking at the output of the strace on a python file with one empty line, we observe behaviour such as the file being read twice
- System Calls are empowering
    - B/c they are the interface between the user code and the kernel
    - Any language you use will eventually have to interact with the kernel via system calls
    - If you are able to understand system calls, you can understand how the kernel is interacting with your code, and what any part of a language's standard library must be behaving ultimately
- How does seek work?
    - In the filesystem of an spinning disk for example, we represent each file via an inode
        - Interaction with a spinning disk is a block based interaction
        - All data is stored in 4kb chunks (blocks)
    - In the filesystem, the inode is a data structure that represents a file, which provides metadata about which blocks of data are associated with the file
    - The inode containes metadata about the file, including the size of the file and the pointers to data blocks that contain the file's data
    - The `lseek` system call allows us to move the file descriptor to a different position in the file, in terms of the number of bytes
    - Operating System will cache reads, so if you read the same file twice, after seeking, the OS will not have to read the file again
- User Space Buffering for Writes
    - When you're doing a lot of write operations, the kernel will buffer the writes in a user space buffer
    - Then the kernel will flush the buffer to write to the output destination
    - What is user space?
        - The part of the Operating System we use that does not interact with the kernel (which we interact with via system calls)
    - Why?
        - To avoid calling the syscall for every single write operation
        - The overhead of switching to the kernel and having it process the system call is not ideal (if you're writing 1 byte at a time in a loop for example)
    - Therefore
        - If you set up a program to do a lot of writes (e.g. via a while loop), you can cause the printing to "fail" (i.e. not print) by intentionally crashing the program before the buffer is flushed
        - This runs counter to our intuition about how this works
    - How to force a flush of a user space buffer?
        - In the print statement, add a newline character `\n` to the end of the string - this forces a buffer
        - Use the actual system call instead of a wrapper around it (i.e. printf), instead use `write` directly

## Links & Symlinks
- Symlinks are between the system call interface
    - Because they are part of the filesystem
    - `symlink` system call
- Link
    - A link that points from one "file" to the data of another
- Removing a Link (`rm foo`)
    - `rm` is a misnomer (also called `unlink`)
        - For links, it removes 1 link, not the files referenced by them
        - There can be multiple links
- Symlink
    - A file that points to another file
    - It has its own inode
    - What happens if the underlying file is removed for the symlink?
        - The symlink remains, but if you try to interact with the symlink, you'll get a file not found error
        - Recreating the original file will cause the symlink to work again
            - Why? B/c the symlink contains the name of the file to which it is linked
    - Will a symlink continue to work if you move the file around?
        - Only if you specify the full path
    - A symlink will generally not have any blocks associated with it
        - It is just a pointer to another file
        - If the path to which it is pointing is long enough, it will take up 1 block
        - Why?
            - The inode itself has some space to store contents
            - If the path is too long, it will be stored in a block
    - Necessary I/O steps (for single-nested symlink)
        - Access the inode of the symlink
        - Access the data saved within the inode of the symlink
        - Access the blocks associated with the file to which the symlink points
        - Follow the path to the file to which the symlink points
        - Access the inode of the file to which the symlink points
        - Access the data saved within the inode of the file to which the symlink points
        - Access the blocks associated with the file to which the symlink points

## System Calls and Man Pages
- `man 1 intro` -> Intro to general commands (tools and utilities)
- `man 2 intro` -> Gives the introduction to system calls and error numbers
- `man 3 intro` -> Gives the introduction to C library functions
- On linux
    - `man 2 syscalls` -> Gives a list of all syscalls
- POSIX system calls
    - Unix-like systems standard for system calls
    - You can expect these in Linux + MacOs
- Non-POSIX
    - System calls specific to a particular OS, not unix-wide

## What is the Kernel Not?
- What is Ubuntu other than Linux?
    - Ubuntu is a distribution of Linux
    - Linux is the kernel
    - Ubuntu is a collection of software that includes the Linux kernel
- What is the kernel not?
    - The shell (runs in user space) but needs to interact with the kernel
    - Essentially everything in the OS that is in user-space 
        - Shell
        - Compiler
        - Linker
        - C Standard Library
    - Essentially everything that *generally* ships with an OS, but does not "technically" need to for the machine to work. You could install everything yourself
        - This is what a distribution does for you in Linux, it makes certian decisions about what user-space programs are included in the OS

