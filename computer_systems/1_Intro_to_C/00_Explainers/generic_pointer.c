#include <stdio.h>

/*
* Notes:
* - In dynamically typed languages you can mix and match types as you please
* - In statically typed languages this is not the case b/c
*   - You have a type system protecting you
*   - Or the compiler needs to know how to lay your data structures
*     out in memory and which machine code instruction to emit
*   - Likely both!
* - What if you don't want to specify the type?
*   - In some languages you have a Generic Type
* - In C you can be generic via using memory addresses
*   - Specifically the generic pointer
* - void pointers and void are completely separate concepts
*/

struct Box {
    char* name;
    // Storing an 8 byte memory location pointer
    // Can't store an integer (4 bytes) - need to pass a reference to it
    void* value;

};

int main(){
    struct Box b1 = {"foo", "box"};
    int n = 5;
    struct Box b2 = {"bar", &n};

    printf(
        "values are: %s and %d\n", 
        // Casting here isn't strictly necessary b/c printf know
        // what to do, but it is more explicit to convert the 
        // generic pointer to a type specific one
        // Prior to the introduction of generic pointers, char*
        // were used for generic pointers
        (char*)b1.value, 
        // To retrieve the integer, we first have to cast
        // the generic pointer to an integer pointer
        // And we have to dereference the entire thing
        *(int*)b2.value
    );

    // Generic pointers are useful for abstracting generalizable
    // logic - i.e. sorting - via generic pointers
    // Check out man 3 qsort to check libc implementation of qsort
    // qsort interface
    // void qsort(
    //      void *base, - Generic pointer to your array of "things"
    //      size_t nel, - How many things are there?
    //      size_t width, - How big is each "thing" in bytes?
    //                      i.e. 4 for 32 bit integers
    //      int (* compar)(const void *, const void *)
    //          -> Function pointer declaration
    //             qsort expects you to pass a reference to a 
    //             comparison function.
    //             Accepts two void pointer arguments
    //  );

}
