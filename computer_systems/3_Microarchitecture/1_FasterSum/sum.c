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

int newsum(int * nums, int n){
  int total0 = 0;
  int total1 = 0;
  int total2 = 0;
  int total3 = 0;

  for (int i = 0; i < n / 4; i++)
    total0 += nums[i];
  for (int i = n/4; i< n/2;i++)
    total1 += nums[i];
  for (int i = n/2; i< 3*n/4;i++)
    total2 += nums[i];
  for (int i = 3*n/4; i< n;i++)
    total3 += nums[i];
  return total0 + total1 + total2 + total3;
}

int sum(int *nums, int n) {
  return newsum(nums, n);
}







