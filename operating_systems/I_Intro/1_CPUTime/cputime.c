/*
* OS Course -> You'll get a sense of what OS do and what subsystems it are made of
* Intro sequence of problems to answer:
* - What is an OS?
* - What is a system call? How do I make one?
* - What are the core responsibilities of the OS?
*
* - You'll figure out how much time your CPU is taking and how much time the kernel is taking
* - We confront the original responsibility of multitasking Operating systems
*   - Enabling multiple programs to run at the same time
*   - While providing illusion that each program has computer to itself
* - One of main ideas:
*     - Core responsibility of OS is to switch between ongoing processes in a way in which they can share the underlying CPU (across multiple cores if available) without explicitly being aware of one another
* 
* Very Open ended problem -> you could check how much the OS is context switching
*
* Task:
*  You want to provide the 
*   - Pid
*     - Stretch goal -> Color by PID
*   - CPU (Stretch goal)
*   - Explanation of what is happening at every step
*   - Real, user & sys time spent per step
*
*
* ASIDE:
* - Difference between & and &&
*     - & -> Processes should run at the same time - first program should run in the background, stdin goes to second process
*     - && -> Run first process to completion, then with exit code 0, run second task to completiong
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define SLEEP_SEC 3
#define NUM_MULS 100000000
#define NUM_MALLOCS 100000
#define MALLOC_SIZE 1000

// TODO define this struct
struct profile_times {
  int muls_done;
  time_t muls_start;
  int mallocs_done;
  time_t mallocs_start;
  int sleeps_done;
  time_t sleeps_start;
};

// TODO populate the given struct with starting information
void profile_start(struct profile_times *t) {
  printf("%p", t->muls_done);
  if (!t -> muls_done){
    t -> muls_start = time(NULL);
    printf("Starting %d Muls", NUM_MULS);
  }

}
  

// TODO given starting information, compute and log differences to now
void profile_log(struct profile_times *t) {

}

int main(int argc, char *argv[]) {
  struct profile_times t;

  // TODO profile doing a bunch of floating point muls
  float x = 1.0;
  profile_start(&t);
  for (int i = 0; i < NUM_MULS; i++)
    x *= 1.1;
  profile_log(&t);

  // TODO profile doing a bunch of mallocs
  profile_start(&t);
  void *p;
  for (int i = 0; i < NUM_MALLOCS; i++)
    p = malloc(MALLOC_SIZE);
  profile_log(&t);

  // TODO profile sleeping
  profile_start(&t);
  sleep(SLEEP_SEC);
  profile_log(&t);
  printf("DONE\n");
}
