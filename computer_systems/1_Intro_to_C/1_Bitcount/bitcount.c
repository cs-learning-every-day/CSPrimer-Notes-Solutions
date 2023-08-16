#include <assert.h>
#include <stdio.h>
int bitcount(int n);
int bitcount_sol_signed(int n);
int bitcount_sol(unsigned n);

int main() {
    assert(bitcount_sol(0) == 0);
    assert(bitcount_sol(1) == 1);
    assert(bitcount_sol(3) == 2);
    assert(bitcount_sol(4) == 1);
    assert(bitcount_sol(8) == 1);
    assert(bitcount_sol(15) == 4);
    assert(bitcount_sol(16) == 1);
    // harder case:
    assert(bitcount_sol(0xfffffff) == 28); 
    assert(bitcount_sol(0xffffffff) == 32); 
    printf("OK\n");
}

int bitcount_pop(unsigned n) { return __builtin_popcount(n);}

int bitcount(int n){
    //printf("Num: %d\n", n);
    /*
     * Instantiate the number of bits
     * Get the total number of available
     * bits in the provided number
     */
    int bits = 0;
    int bytecount = sizeof(n);
    int bitcount = bytecount * 8;
    //printf("Size (Bytes): %d\n", bytecount);
    //printf("Size (Bits): %d\n", bitcount);
    /*
    * For each bit, shift the number down
    * then check if the first bit of that 
    * shifted number is equal to 1.
    * If yes, add it to the number of bits.
    */
    for (int i = 0; i<bitcount; ++i){
        int bit_shift_num = n >> i;
        int bit_add = bit_shift_num & 0x1;
        bits += bit_add;
    }
    //printf("Number of 'On' Bits: %d\n", bits);
    //printf("---------------------\n");
    return bits;
}

int bitcount_sol_signed(int n){
    int count = 0;
    while (n){
        count += n & 0x01;
        n >>= 1;
        /*
        * This works for signed integers out of the box 
        * because n is never getting to zero for these. 
        * Shifting right of a signed integer
        * results in an arithmetic shift
        * Which fills the higher order bits with 1
        * To review this, look at two's complement
        */
    }
    return count;
}

int bitcount_sol(unsigned n){
    /*
    * Stretch Goal:
    *   - Use the fact that x &= (x-1) deletes the rightmost 1-bit
    *
    * Why is the above the case?
    *   - Consider case where x=7
    *       - In binary:
    *           - 7 -> 111
    *           - 6 -> 110
    *   - Thus
    *       - 111 & 110 -> 110 (6)
    *   - Subtracting 0b1 from a given binary number will always
    *     change the rightmost place to either be a 1 or 0 from 
    *     the opposite case
    *
    *
    * How can this help to count on-bits?
    * - Current Approach
    *       - We currently retrieve the first bit for each bit in the number
    * - New Approach
    *       - Deleting the rightmost bit from the number
    *       - If you continuously delete the right most bit you can 
    *       - iterate over n and count for each iteration until n hits 0
    *
    * Why is the new approach faster?
    *   - Old Approach
    *       - You loop over every bit in the integer and identify if the lowest order bit is on
    *       - Worst_case = Average_case = best_case = n
    *   - New Approach
    *       - You are able to always remove the lowest order bit
    *       - Worst_case = n (i.e. 0b111)
    *       - Best_cast = 1 (i.e. 0b100 or any number with only a starting on bit)
    */
    int count = 0;
    while (n){
        n &= n-1;
        count++; 
    }
    return count;
}

