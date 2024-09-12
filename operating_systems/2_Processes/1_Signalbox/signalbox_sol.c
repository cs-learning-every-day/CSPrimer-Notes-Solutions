#include <signal.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>



volatile sig_atomic_t resized = 0;


void handler(int sig){
    // Handler atomically updates a flag
    // which is checked outside of the handler
    // This avoids invocations of the handler
    // overlapping with another if signal triggers
    // are faster than the handler execution
    resized = 1;
}

void w1(char*s){
    write(1, s, 1);
}

void wn(int n, char*s){
    while(n--){
        w1(s);
    }
}

void print_box(){
    struct winsize ws;
    ioctl(0, TIOCGWINSZ, &ws);
    int x = ws.ws_col / 3;
    int y = ws.ws_row / 3;
    printf("Cols: %d, rows: %d\n", ws.ws_col, ws.ws_row);   

    wn(y, "\n"); // Space at top
    wn(x, " ");
    w1(".");
    wn(x-2, "-");
    w1(".");
    w1("\n");
    for (int i=2;i<y;i++){
        wn(x, " ");
        w1("|");
        wn(x-2, " ");
        w1("|");
        w1("\n");
    }
    wn(x, " ");
    w1("'");
    wn(x-2, "-");
    w1("'");
    w1("\n");
    wn(ws.ws_row - 2*y, "\n"); // Space at bootom
}

int main(){
    struct sigaction sa;
    sa.sa_handler = handler;
    sigaction(SIGWINCH, &sa, NULL);
    printf("Waiting for signal\n");
    print_box();
    for(;;)
        if (resized) {
            print_box();
            resized = 0;
        }
    ;
}
