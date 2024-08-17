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
*
* ASIDE:
* - Difference between & and &&
*     - & -> Processes should run at the same time - first program should run in the background, stdin goes to second process
*     - && -> Run first process to completion, then with exit code 0, run second task to completiong
*
*   Goals:
*   1. Research needed syscalls/library functions
*     - We can research via `apropos` command to look up commands related to pids for example
*   2. Print pid using getpid(2)
*   3. Determined elapsed "real" (wall clock) time using gettimeofday(3) include <sys/time.h>
*   4. Determine elapsed time on CPU (both user and system) using getrusage(3) include <sys/resource.h> (rusage -> ru_utime (user) and russage -> ru_stime (system))
*   5. Refactoring/cleanup, maybe cpuid
*
*
* - Notes:
*   - For research, use man pages to look up functions (apropos is better on linux)
*   - You can also trace systemcalls on command line utilities
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>

#define SLEEP_SEC 3
#define NUM_MULS 100000000
#define NUM_MALLOCS 100000
#define MALLOC_SIZE 1000

// TODO define this struct
struct profile_times {
};

// TODO populate the given struct with starting information
void profile_start(struct profile_times *t) {}

// TODO given starting information, compute and log differences to now
void profile_log(struct profile_times *t) {}

int main(int argc, char *argv[]) {
  struct profile_times t;
  struct timeval start_mul, end_mul;
  pid_t pid = getpid();

  // TODO profile doing a bunch of floating point muls
  float x = 1.0;
  profile_start(&t);
  printf("[pid %d] %d fmuls\n", pid, NUM_MULS);
  gettimeofday(&start_mul, NULL);
  struct rusage usage_mul;
  for (int i = 0; i < NUM_MULS; i++)
    x *= 1.1;
  gettimeofday(&end_mul, NULL);
  getrusage(RUSAGE_SELF, &usage_mul);
  profile_log(&t);

  long seconds_mul_r  = end_mul.tv_sec  - start_mul.tv_sec;
  long useconds_mul_r = end_mul.tv_usec - start_mul.tv_usec;

  long seconds_mul_u = usage_mul.ru_utime.tv_sec;
  long useconds_mul_u = usage_mul.ru_utime.tv_usec;

  long seconds_mul_s = usage_mul.ru_stime.tv_sec;
  long useconds_mul_s = usage_mul.ru_stime.tv_usec;

  // Convert to total elapsed time in seconds
  double elapsed_mul_u = seconds_mul_u + useconds_mul_u/1e6;
  double elapsed_mul_s = seconds_mul_s + useconds_mul_s/1e6;
  double elapsed_mul_r = elapsed_mul_u + elapsed_mul_s;
  printf("[pid %d] real: %.3fs user: %.3fs system: %.3fs\n", pid, elapsed_mul_r, elapsed_mul_u, elapsed_mul_s);


  // TODO profile doing a bunch of mallocs
  profile_start(&t);
  void *p;
  printf("[pid %d] %d mallocs of size %d\n", pid, NUM_MALLOCS, MALLOC_SIZE);
  for (int i = 0; i < NUM_MALLOCS; i++)
    p = malloc(MALLOC_SIZE);
  profile_log(&t);

  // TODO profile sleeping
  struct timeval start_sleep, end_sleep;

  // TODO profile doing a bunch of floating point muls
  profile_start(&t);
  printf("[pid %d] sleeping for %d seconds\n", pid, SLEEP_SEC);
  gettimeofday(&start_sleep, NULL);
  struct rusage usage_sleep;
  sleep(SLEEP_SEC);
  gettimeofday(&end_sleep, NULL);
  getrusage(RUSAGE_SELF, &usage_sleep);
  profile_log(&t);

  long seconds_sleep_r  = end_sleep.tv_sec  - start_sleep.tv_sec;
  long useconds_sleep_r = end_sleep.tv_usec - start_sleep.tv_usec;

  long seconds_sleep_u = usage_sleep.ru_utime.tv_sec;
  long useconds_sleep_u = usage_sleep.ru_utime.tv_usec;

  long seconds_sleep_s = usage_sleep.ru_stime.tv_sec;
  long useconds_sleep_s = usage_sleep.ru_stime.tv_usec;

  // Convert to total elapsed time in seconds
  double elapsed_sleep_u = seconds_sleep_u + useconds_sleep_u/1e6;
  double elapsed_sleep_s = seconds_sleep_s + useconds_sleep_s/1e6;
  double elapsed_sleep_r = elapsed_sleep_u + elapsed_sleep_s;
  printf("[pid %d] real: %.3fs user: %.3fs system: %.3fs\n", pid, elapsed_sleep_r, elapsed_sleep_u, elapsed_sleep_s);

  printf("DONE\n");
}
