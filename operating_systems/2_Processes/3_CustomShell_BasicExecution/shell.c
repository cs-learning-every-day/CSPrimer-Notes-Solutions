/*
* - Shell is a core part of an OS and Unix
*    - Despite being user-space program
* - APIs of the Operating System are set up to support the shell as the killer app
* Objective:
* - Write a shell prgogram that can run basic programs likes "ls" or "cat foo.txt", as well as builtin commands like "quite" and "help"
*       - It should handle signals like SIGINT correctly
*       - Doesn't need to support pipes, redirection or even strings
* - Write a simple shell to execute programs
* - Should handle signals correctly
*    - I.e. Ctrl-C should cancel the child process, not the shell
* - Parsing code will be very simple here
*    - Tokenize on spaces and tabs
*
* Understand:
* - Executing shell should enter into a prompt which waits for user input
* - Once user input is provided, the shell should parse the arguments
* - It is implicitly assumed that the arguments provided are mappable to programs available to the user, and their input arguments
* - The shell should then try to execute the provided command, given the argument(s) provided to it as a child process. This should be done using the fork/exec/wait cycle
* - Finally, the shell should handle signals to interact with the child process effectively
*   - Sending a SIGINT (ctrl-c), should cancel the child process (if there is one), not the shell
*   - You can exit the shell by passing "exit" command
*
*
* Plan:
* Write a C program that waits for user input and retrieves it
*   - This will involve reading from stdin, and parsing this if a certain trigger (enter) is sent
*
*/
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>


int main(int argc, char *argv[]){
    for(;;){
        printf("\n$ ");
        char c[20];
        char a[20];
        scanf("%s %s", &*c, &*a);
        pid_t pid;
        pid = fork();
        if (pid < 0){
            printf("Fork failed!");
            return 1;
        }
        else if (pid == 0){
            execlp(c, c, a, NULL);
        } else {
            int status;
            waitpid(pid, &status, 0);
        }
    }


}


