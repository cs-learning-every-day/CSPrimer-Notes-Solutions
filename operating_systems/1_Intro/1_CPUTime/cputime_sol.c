/*
* - How does sleep work
*   - System call that instructs the scheduler to not schedule the process for a certain amount of time
*   - There is no guarantee that the process will be scheduled immediately after the sleep time
* - getcpu
*   - Available as a system call on Linux, but not on MacOS
*   - You could figure out why it is that way by stepping through the system call
*   - It turns out that on x86, there's an assembly instruction that you can call which will get you the cpu (cpuid.h)
* - Conclusions
*   - Spending as much time in user-space as possible during a program is good (we wantto spend time on our code, not the OS, which may be handling other processes)
*   - 
*/

#include <cpuid.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/time.h>
#include <sys/resource.h>

#define SLEEP_SEC 1
#define NUM_MULS 100000000
#define NUM_MALLOCS 100000
#define MALLOC_SIZE 1000
#define MICROSECONDS_IN_SECOND 1000000.0
#define TOTAL_USEC(tv) ((tv).tv_sec * MICROSECONDS_IN_SECOND + (tv).tv_usec)


#define RESET   "\x1b[0m"
#define RED     "\x1b[31m"
#define GREEN   "\x1b[32m"
#define YELLOW  "\x1b[33m"
#define BLUE    "\x1b[34m"

unsigned getcpu(){
  //
  unsigned reg[4];
  __cpuid_count(1, 0, reg[0], reg[1], reg[2], reg[3]);
  return reg[1] >> 24;
}

struct profile_times {
  uint64_t real_usec;
  uint64_t user_usec;
  uint64_t sys_usec;
};

void profile_start(
  struct profile_times *t,
  pid_t pid 
) {
  struct timeval tv;
  struct rusage ru;
  gettimeofday(&tv, NULL);
  getrusage(RUSAGE_SELF, &ru);
  t->real_usec = TOTAL_USEC(tv);
  t->user_usec = TOTAL_USEC(ru.ru_utime);
  t->sys_usec = TOTAL_USEC(ru.ru_stime);
}



void profile_log(
  struct profile_times *t,
  pid_t pid 
) {
  struct timeval tv;
  struct rusage ru;
  gettimeofday(&tv, NULL);
  getrusage(RUSAGE_SELF, &ru);
  uint64_t real_diff = TOTAL_USEC(tv) - t->real_usec;
  uint64_t user_diff = TOTAL_USEC(ru.ru_utime) - t->user_usec;
  uint64_t sys_diff = TOTAL_USEC(ru.ru_stime) - t->sys_usec;
  fprintf(
    stderr, // Writing to stderr as this is debugging output
    RED "[pid: %d]" RESET GREEN "real %0.03f " RESET BLUE "user: %0.03f " RESET YELLOW "sys %0.03f\n" RESET, 
    getpid(),
    //getcpu(), This only works on x86 - I'm running on M1 Mac
    real_diff / MICROSECONDS_IN_SECOND, 
    user_diff / MICROSECONDS_IN_SECOND, 
    sys_diff / MICROSECONDS_IN_SECOND
  );
}

int main(int argc, char *argv[]) {
  struct profile_times t;
  pid_t pid = getpid();

  // TODO profile doing a bunch of floating point muls
  fprintf(stderr, RED "[pid: %d] " RESET "%d fmuls\n", pid, NUM_MULS);
  float x = 1.0;
  profile_start(&t, pid);
  for (int i = 0; i < NUM_MULS; i++)
    x *= 1.1;
  profile_log(&t, pid);

  // TODO profile doing a bunch of mallocs
  fprintf(stderr, RED "[pid: %d] " RESET "%d mallocs of size %d\n", pid, NUM_MALLOCS, MALLOC_SIZE);
  profile_start(&t, pid);
  void *p;
  for (int i = 0; i < NUM_MALLOCS; i++)
    p = malloc(MALLOC_SIZE);
  profile_log(&t, pid);

  // TODO profile sleeping
  fprintf(stderr, RED "[pid: %d] " RESET "sleeping for %d seconds\n", pid, SLEEP_SEC);
  profile_start(&t, pid);
  sleep(SLEEP_SEC);
  profile_log(&t, pid);

  printf("OK\n");
}
