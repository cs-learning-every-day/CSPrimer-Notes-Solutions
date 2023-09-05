#include <stdio.h>

/*
* NOTES:
* - Group of variables together
* - Most value of structs to represent semantically close data
* - Essentially objects without methods
* - Size of the struct is fixed
*   - This allows for array indexing via pointer arithmetic
* - If you know the size of a string, you can put it in the struct
*   - To maintain fixed memory size
* - You will often use pointers to structs
*   - B/c otherwise you copy the entire struct into a function
*   - Not a problem for struct of our size - for large struct this
*     will take time and space
*   - Syntactic sugar to refer to attributes on struct pointer: ->
*       - I.e. p->name
*/

struct user {
    int age; // 4 bytes
    short postcode; // 2 bytes
    //short rating; // 2 bytes
    char* name; // 8 bytes
};

int main() {
    struct user u = { 25, 10000, "Bob"};
    struct user u2 = {17, 20000, "Alice" };

    struct user *p = &u2;
    // Struct is generally: laid out entirely contiguous in memory
    // One gotcha: first element is at the same reference to the beginning of the struct in memory
    printf("%s is %d years old\n", u.name, u.age);
    printf("%s is %d years old\n", p->name, p->age);

    printf(
        "%p %p %p %p\n", 
        &u,  // Address of struct u
        &(u.age),  // Address of struct attribute u.age
        &(u.postcode),  //etc
        &(u.name)
        //&(u.rating)
    );
    // u.postcode is 4 bytes further than u.age
    // Why? so that the following 8 byte value (u.name) is properly aligned
    // This is handled by the compiler
    // You can save space & time by ordering your entries in a way to minimize the amount of padding!
    // Example: Uncomment the "u.rating" code, you'll see that the
    // entries are packed into memory in accordance with their byte
    // size
    
    struct user users[2] = {
        {1, 10000, "foo"},
        {2, 10001, "bar"},
    };
    printf("One struct is %lu bytes\n", sizeof(struct user));
    printf("%s is %d years old\n", users[1].name, users[1].age);
    printf(
        "users array is a %p, \"%s\" is located at %p\n", 
        users,users[1].name,  
        &users[1].name
    ); 

    // Be thoughtful about passing structs
    // Choose between references or values of individual fields
    // No one right answer

    printf("ok\n");
}
