# Exploring the Process Lifecycle
## Introduction
- Once the kernel has initialized itself, how does it start running user programs?
    - systemd / launchd / initd/ etc
        - The first process that starts
        - Process ID (PID) 1
    - How does systemd start sshd? Or how does bash start another bash process?
- What is a process?
    - Instance of a running program
    - Examples -> `ls`
        - It is an executable file in the filesystem (`/bin/ls`)
        - If we execute `ls` from the file, we create a process that is running `ls`
- How does a process start?
    - How is it that bash can run pstree?
        - It starts with a system call
        - Why do we need a system call?
            - We need to give the kernel a program (blueprint) to verify whether we can allocated resources to open this program
            - Reasons to deny:
                - No permission
                - No memory
                - etc
        - The system call to create a new process -> `fork`
            - Creates a new process by duplicating the calling process
                - The new process is called the child process
                - The child process differs only in:
                    - PID
                    - PPID (Parent Process ID)
                    - Empty set of pending signals
                    - Timer values are reset
                    - File locks set by parent are not inherited
        - The system call to execute a new program -> `exec`
            - This is responsible for executing a given program within a given PID


## Example Program
```
#include <unistd.h>
#include <syswait.h>
#include <stdio.h>

int main(){
    printf("hi!\n");
    pid_t pid;
    if ((pid = fork()) == 0){
        // we are the child
        execlp("ls", "ls", NULL);
        // The child process should be replaced by the ls process
        // Before getting to this print statement
        printf("We should never get here\n");
    } else {
        // we are the parent
        int status;
        waitpid(pid, &status, 0);
    }
}
```
- The above program
    - Creates a child process, which executes `ls`
        - By calling `execlp`, the child process is replaced by the `ls` process, and we exit the child process
    - Why does the child see a process id of 0?
        - Because the `fork` system call returns 0 to the child process
        - The parent process gets the actual PID (>0) of the child process
    - The parent process enter the `else` block, and waits for the child process to finish
- When running strace on this program
    - You won't see the `fork` system call
        - It will use `clone` under the hood
    - We also only see the system calls of the parent process by default
        - Unless you pass the `-f` flag to strace, at which point it will follow the child process
- The `status` that is returned by `waitpid` will give you the unix exit code (0,1) which indicates whether the process has exited correctly
- Generally speaking, the parent will always wait until the child has completed to finish
    - If this doesn't happen, the processes will be in some unnormal state

## Process States
- Common States
    - R -> Running
        - Running or runnable (on run queue)
    - S -> Sleeping
        - Interruptible sleep (waiting for an event to complete)
    - T -> Stopped
        - Stopped by a job control signal
    - X -> Dead
        - This should never be seen, as the parent should clean it up
- Aside: What happens if you stop and restart sleep?
    - If you stop (put into T) `sleep 10`, and then restart it after 10 seconds, what happens?
    - Restart command:
        - `kill -s SIGCONT <PROCESS_ID> %% ps -o pid,stat | grep <PROCESS_ID>` 
    - Result?
        - You won't see the process ID come up, b/c if the process is restarted after 10 seconds, it will be immediately cleaned up and put into state X (which is not observed by the user)

## Infinite Loops
```
int main(){
    while(1);
}
```
- At the level of the CPU
    - It's just constantly checking if the loop has finished
- How can you stop something runnign like this?
    - By sending `SIGINT` signal
- `kill`
    - Doesn't just kill processes, but actually sends signal to the Kernel about a particular process
    - The OS then interprets that signal and uses that to manage the process in some way
- Non-Preemitble Code
    - Process State D (usually I/O)
    - You've gotten into a state where the kernel doesn't want signals to be processed for this process
    - Historically -> Disk Reads
        - If a signal showed up during a Disk Read would lead to weird consequences
        - This meant the signal was ignored
        - This was hard to deal with b/c you had uninterruptible processes
        - Overtime this was reduced to the extent that this rarely happens now
    - There is no way on an OS built on preemptible signals and timer interrupts to write particular assembly code that will create an uninterruptible program


## Zombie
```
#include <unistd.h>

int main(){
    if (fork() == 0){
        exit(0);
    }
    while(1);
}
```
- Zombie Process
    - When a child is created and the parent does not wait on it
    - In the program above we 
        - Create a child process that exits immediately
        - Create a parent process that loops forever and does not wait on the child process
    - What is a zombie process?
        - A state that a child process enters after exiting in order to stay available for the parent to reference
        - It can happen either b/c the parent incorrectly forgot to wait OR b/c the parent has not yet waited on the Child
            - If the parent is working on a computationally intensive task, and the child process exits quickly, during the delta between the child processes' exit and the point at which the parent begins waiting, the child will be in a zombie state
    - What happens if you kill the parent of a zombie process?
        - Both the Zombie process and the child will be killed
- Process Adoption (Reparenting)
    - If a child process is running (not in Zombie state), and its parent exits, it gets reparented under process 1
    - Why?
        - Every process needs a parent at all times
    - What does launchd to do this?
        - It periodically calls wait to pick up these processes that have lost their parent
