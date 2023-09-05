#include <stdio.h>
/*
* Intro
* - Memory available to process
*     - Bunch of cells from 0 -> n
*         - Each cell is a byte you can reference by number
*     - Memory is byte addressable
* - Example: integer at byte 40
*     - Integer (32 bits) takes up 1 byte
*     - You may want to refer to the address of this integer
*         - Say a function wants to change that value
*     - Incrementing the integer is in place if you just pass some number *i* into the function
*     - Why?
*         - Because *i* is going to be copied, not the value stored at the memory address
*     - You can obtain the address by using the &
*         - &i -> Value of memory at address i
* - Objects of indeterminate lenght (i.e. strings)
*     - Can't do much but refer to the beginning of it
*     - At the end of the object you have a null point
*     - By dereferencing the pointer to the object you get the first value
*         - Then by incrementing the byte value you get the next element (i.e. of the string)
* - Imagine you want a function that has an error code and a string
*     - You can have an integer that is returned for the error code
*     - To pass the result you'd need to return the reference to that string
*- Arrays are basically a syntax for pointers
*   - Name for the starting location of a contiguous sequence of things
*/

void incr(int *i){
    // - Dereferences a pointer to an integer
    // - Increments it
    // - Sets the new value to the provided pointer
    int val = *i;
    val++;
    *i = val;
}

int main() {
    int n = 5;

    // * to declare a pointer and retrieve value from pointer/address
    // & to get the address
    // Why? -> Asterisk to highlight you'll want to use * on
    int *p = &n;

    int foo = *p;

    // n -> value (5)
    // %&n -> memory address / pointer (i.e. 0x16d85f0bc)
    printf("N = %d, p = %p, p+1 = %p \n", foo, p, p+1);

    int arr[10];

    // The memory address of arr is incremented by 4 bytes
    // B/c that is one cell of memory
    printf("arr = %p, arr + 1 = %p\n", arr, arr+1);

    // The below says:
    // Take the address of arr
    // and retrieve the address 3 bytes from that address
    // which returns 42
    arr[3] = 42;
    printf("arr[3] = %d\n", arr[3]);



    // The below says:
    // Take the address of arr and add three bytes to it to retrieve
    // the address
    // To retrieve the value, you need to dereference (with *)
    // Thus, arr[3] is syntactic sugar for *(arr + 3)
    printf("arr + 3 = %p, *(arr + 3) = %d\n", arr + 3, *(arr + 3));

    // We can increment the value of the array by passing a 
    // pointer to the memory address
    incr(arr + 3);
    printf("arr[3] = %d", arr[3]);
}




