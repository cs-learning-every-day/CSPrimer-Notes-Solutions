#include <assert.h>
#include <stdio.h>
int bitcount(int n);
int bitcount_sol_signed(int n);
int bitcount_sol(unsigned n);

int main() {
    assert(bitcount(0) == 0);
    assert(bitcount(1) == 1);
    assert(bitcount(3) == 2);
    assert(bitcount(4) == 1);
    assert(bitcount(8) == 1);
    assert(bitcount(15) == 4);
    assert(bitcount(16) == 1);
    // harder case:
    assert(bitcount(0xfffffff) == 28); 
    assert(bitcount_sol(0xffffffff) == 32); 
    printf("OK\n");
}


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
    * 
    */
    printf("n: %d\n", n);
    int count = 0;
    while (n){
        count += n & 0x01;
        n >>= 1;
        printf("new n: %d\n", n);
    }
    return count;
}

