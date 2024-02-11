/*
* Everything is sequentially accessed, can't change that
* We can make this faster using understanding of explainer
* Idea: Multiple accumulators?
* Keep the optimization level at O1 (O2 would be faster)
*   O0 -> Won't care about optimization, pulls a lot of data in and out of registers
*   O2 -> You won't be able to beat this; you're encouraged to look at the disassembly after the exercise
*     - Effectively the code converted to assembly using the compiler's understanding of the microarchitecture
* There is a discipline of performance engineering
*   - They can beat the compiler via their understanding of the microarchitecture
*/
int oldsum(int *nums, int n) {
  int total = 0;
  for (int i = 0; i < n; i++)
    total += nums[i];
  return total;
}

/*
* Weird trick:
* - Intel Skylake has 8 execution ports with execution units that can be used in parallel
* - Four of these have integer ALUs -> could theoretically do 4 additions per CPU cycle
*   - Additions have to be independent
* - At some point another bottleneck will come
*   - If we're memory constrainted instead of compute constrained, our optimizations won't help
*/
int newsum(int *nums, int n){
  int t1 = 0, t2 = 0;//, t3 = 0, t4 = 0;//, t5 = 0;
  for (int i = 0; i<n; i+=5){
    t1 += nums[i];
    t2 += nums[i + 1];
  }

  return t1 + t2;// + t3;// + t4;// + t5;
}

int sum(int *nums, int n) {
  return newsum(nums, n);
}







