/*
* Task: 
* Cause as many unique signals as you can to be logged by the program defined in siglog.c. You can and should modify the program itself to meaningfully generate some signals, whereas others will arrise via your interactions with it. Don't just use `kill -n` for all n, that's boring!
* 
*
*
           Name             Default Action       Description
     1     SIGHUP           terminate process    terminal line hangup      -> Handled when I killed a related process
     2     SIGINT           terminate process    interrupt program          -> ctrl c
     3     SIGQUIT          create core image    quit program               -> ctrl 4
     4     SIGILL           create core image    illegal instruction
     5     SIGTRAP          create core image    trace trap
     6     SIGABRT          create core image    abort program (formerly
                                                 SIGIOT)
     7     SIGEMT           create core image    emulate instruction
                                                 executed
     8     SIGFPE           create core image    floating-point exception
     9     SIGKILL          terminate process    kill program              -> send kill
     10    SIGBUS           create core image    bus error
     11    SIGSEGV          create core image    segmentation violation
     12    SIGSYS           create core image    non-existent system call
                                                 invoked
     13    SIGPIPE          terminate process    write on a pipe with no
                                                 reader
     14    SIGALRM          terminate process    real-time timer expired
     15    SIGTERM          terminate process    software termination
                                                 signal
     16    SIGURG           discard signal       urgent condition present
                                                 on socket
     17    SIGSTOP          stop process         stop (cannot be caught or  
                                                 ignored)
     18    SIGTSTP          stop process         stop signal generated from -> crtl z
                                                 keyboard
     19    SIGCONT          discard signal       continue after stop
     20    SIGCHLD          discard signal       child status has changed
     21    SIGTTIN          stop process         background read attempted
                                                 from control terminal
     22    SIGTTOU          stop process         background write attempted
                                                 to control terminal
     23    SIGIO            discard signal       I/O is possible on a
                                                 descriptor (see fcntl(2))
     24    SIGXCPU          terminate process    cpu time limit exceeded
                                                 (see setrlimit(2))
     25    SIGXFSZ          terminate process    file size limit exceeded
                                                 (see setrlimit(2))
     26    SIGVTALRM        terminate process    virtual time alarm (see
                                                 setitimer(2))
     27    SIGPROF          terminate process    profiling timer alarm (see
                                                 setitimer(2))
     28    SIGWINCH         discard signal       Window size change          -> Window Size Change
     29    SIGINFO          discard signal       status request from         -> Ctrl T
                                                 keyboard
     30    SIGUSR1          terminate process    User defined signal 1
     31    SIGUSR2          terminate process    User defined signal 2
*
*
*/
#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

volatile uint64_t handled = 0;

void handle(int sig) {
  handled |= (1 << sig);
  printf("Caught %d: %s (%d total)\n", sig, sys_siglist[sig],
         __builtin_popcount(handled));
}

int main(int argc, char* argv[]) {
    // Register all valid signals
    for (int i = 0; i < NSIG; i++) {
        signal(i, handle);
    }
    

    // spin
    for (;;){
      char val;
      if (argc == 1){
        val = *argv[0];
      } else{
        val = ' ';
      }
      printf("%d", val);
      sleep(1);
  }
}
