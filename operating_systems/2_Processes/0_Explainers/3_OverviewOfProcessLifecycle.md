# Overview of Process Lifecycle
- All user processes are under a single tree of parent/child relationships
    - Every process will be reparented other than process 1
- Process 1 -> systemd/initd/launchd
    - THE user process that is launched by the kernel once the kernel is ready to go
    - It runs user processes as child processes

## Creating a New Process
- `fork` in unix
    - Creates a child process
    - This child process is an immediate copy of the parent process
        - Except with different process id and parent process id
- `execv` 
    - Replaces the running child process with the provided program process

## Process States
- `D` -> uninterruptible sleep (usually IO)
- `I` -> Idle Kernel thread
- `R` -> Running or runnable (on run queue)
- `S` -> Interruptible sleep (waiting for an event to complete)
- `T` -> Stopped by job control signal
- `t` -> Stopped by debugger during the tracing
- `W` -> Paging (not valid since the 2.6.xx kernel)
- `X` -> Dead (should never be seen)
- `Z` -> Defunct ("zombie") process, terminated but not reaped by its parent

## General State Transitions
- fork -> Created
- Created -> "Ready to Queue" -> Ready (`Rr`)
- Ready -> "Schedule Dispatch" -> Running (`R`)
- Running -> "Interrupt" -> Ready (`Rr`)
- Running -> "I/O or event wait" -> Blocked (`D`, `S`)
- Blocked -> "I/O or event completion" -> Ready (`Rr`)
- Running -> "exit()" -> Terminated (`Z`)
- Terminated -> "wait()" by parent -> (`X`)
