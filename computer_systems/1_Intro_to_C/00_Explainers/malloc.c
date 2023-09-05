/*
* NOTES:
* - Malloc is a c standard library function
*   - Convenient way to manage heap memory
* - You don't *need* to use it
* - Not a system call - but may require additional system calls
*   to retrieve space for memory
* - Data not managed by malloc
*   - Text code
*   - Data known about at compile time
*   - Stack for function locals
*   - Heap for everything else
* - Heap
*   - We'd like to use some of it without caring about what's around it
*   - Avoid some pitfalls around reserving and freeing that space
* - Malloc
*   - Finds a free location of x bytes for whatever you want to save
*   - How does it do that? Linkedlist/freelist (depending on implementation)
*       - Links together the free parts of memory you can iterate over
*         for the user to store memory
*   - Once a node is freed
*       - The freelist is updated to include that free space
*/
