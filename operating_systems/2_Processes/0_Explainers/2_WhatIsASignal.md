# What is a signal?
- Way of communicating between things mediated by an Operating system
    - Can originate from user, process, kernl, etc.
- Type of Signals
    - SIGINT   -> Interrupt Program
    - SIGALARM -> Real-time timer expired
- Messages that are getting to the user process via the Operating System
    - Either b/c the user has prompted them (sigint, sigkill)
    - Inform the process about how they need to behave
- Signals are exceptions to ordinary control flow
    - Live outside of the fetch-decode-execute cycle
    - Example -> SIGFPE
        - If you divide by 0, this will be triggered, and we can't just go on to the next instruction
        - You may be able to recover from this, for which you need a particular handler
        - In other cases you want to terminate
- If you don't have a signal handler
    - There is a predefined action a process will take
- There is a queue of signals
    - The OS defines how to send these signals dedicated for a particular for processes
    - It is up to the scheduler to define how these signals should be communicated to the process and handled
    - Only the following cases are handled immediately
        - SIGILL -> Illegal instruction


## Registering a Signal Handler
```C
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

void handle(int sig){
    if (sig == SIGINT){
        printf("Caught SIGINT\n");
        exit(0); // Without exiting here, the process would become immune to SIGINT
    }
}

int main(int argc, char* argv[]){
    signal(SIGINT, handle);
    while(1);
}
```
