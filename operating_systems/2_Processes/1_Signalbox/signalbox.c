/*
* Objective
* - Write a program which uses the current terminal size to draw a picture, and responds to resizing
*
* Plan:
* 1 Determine the size of the terminal
*    - Todo: How to do this?
* 2 Print a picture (box) in the terminal that has some relation to the size of the terminal
* 3 Listen for a signal that the terminal has been resized
*    - Todo: What signal is this?
* 4 Find out what size the terminal has in response to this signal
*    - Todo: Either via approach in step 1 or is indicated by the previous signal
* 5 Print the box with respect to the new dimensions
* 6 Return to step 4 
*/

#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <curses.h>
#define SIGWINCH 28
#define SCALEDOWN 2

int getRestOfArea(int x){
    return (x - (x / SCALEDOWN))/2;
}


void printBox(int rows, int columns){
    int printRows = rows / SCALEDOWN;
    int printColumns = columns / SCALEDOWN;
    int clearRows = getRestOfArea(rows);
    int clearColumns = getRestOfArea(columns);

    for (int i = 0;i<clearRows;i++){
        printf("\n");
    }
    for (int i =0;i<printRows;i++){
        for (int i = 0;i<clearColumns;i++){
            printf(" ");
        }
        if (i == 0 || i == printRows-1){
            printf("|");
            for (int j=1;j<printColumns-1;j++){
                printf("-");
            }
            printf("|");
        } else {
            printf("|");
            for (int j=1;j<printColumns-1;j++){
                if (i == 0 || i == printColumns-1){
                   printf("-");
                } else {
                   printf(" ");
                }
            }
            printf("|");
        }

        printf("\n");
    }
    for (int i = 0;i<clearRows;i++){
        printf("\n");
    }
}


void sigwinch_handler(int sig){
    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
    printBox(w.ws_row,w.ws_col);

}

int main(int argc, char **argv){
    while(1){
        signal(SIGWINCH, sigwinch_handler);
    };
}


