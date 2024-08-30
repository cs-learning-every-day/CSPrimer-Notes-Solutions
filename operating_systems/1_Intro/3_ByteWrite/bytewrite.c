/*
* Introduction to File System as an Abstraction
*
* Objective:
* - Write a program which opens a file and writes one megabyte to the file, one byte at a time
* - If the amount of space the file takes is greater than 1 mb, log it
*
* Background:
* - Running 'echo hello > tmp' to an empty file (tmp)
*    - Size of file via stat -x, will be 5 bytes + 1 byte for new line character from hello
* - Getting a certain number (X) of random bytes
*    - cat /dev/urandom | head -c X
*
* Findings:
* - The first byte creates a file with 1 byte in it that takes up 4096 blocks in the file system
* - Once 4097 bytes are written, the number of blocks taken is increased to 8092
* - As the bytes written exceed the block count, the block count is increased by 4096 each time, until the block count reaches 65536
* - Once the number of bytes in the file exceeds 65536, the block count begins to increase by 65536 each time the block count is exceeded
* - This pattern continues until the block size count reaches 1,114,112
*   - Then block sizes start increasing by 1,048,576
* - Relationship between 4096 (8 * 512), 65536 (128 * 512) & 1,048,576 (2048 * 512)
*     - 65,536 = 4096*16
*     - 1,048,576 = 65,536*16
*
* - 1 block -> 512 bytes
*
*/
#include <stdio.h>
#include <sys/stat.h>
#define BYTES 1000000

long long getAllocatedSpace(const char* filepath, long long currSpace){
    struct stat fileStat;

    if (stat(filepath, &fileStat) == -1) {
        perror("Error getting file information");
        return 1;
    }
    long long allocatedSpace = (long long)fileStat.st_blocks * 512;

    if (allocatedSpace > currSpace){
        printf(
            "Allocated Space has changed. Previous Blocks: %lld. Current Blocks: %lld\n", 
            currSpace, 
            allocatedSpace
        );
        printf(
            "File Stats - Size: %lld bytes, Block Size: %lld, Blocks: %lld\n",
            (long long)fileStat.st_size, 
            allocatedSpace,
            (long long)fileStat.st_blocks
        );
    }

    return allocatedSpace;
}


int main() {
    const char *filepath = "example.txt";

    int bytes_written = 0;
    long long fileSize = 0;
    long long fileBlocks = getAllocatedSpace(filepath, 0);

    while (BYTES - bytes_written > 0){
        // Open a file in write mode ("w")
        FILE *file = fopen(filepath, "a");
        
        // Check if the file was opened successfully
        if (file == NULL) {
            perror("Error opening file");
            return 1;
        }

        // Write to the file using fprintf
        fprintf(file, "X");

        // Close the file
        fclose(file);

        bytes_written++;

        if (bytes_written % 100000 == 0){
            printf("Bytes Written: %d\n", bytes_written);

        }
        fileBlocks = getAllocatedSpace(filepath, fileBlocks);

    }


    // Remove the file
    if (remove(filepath) == 0) {
        printf("File deleted successfully.\n");
    } else {
        perror("Error deleting the file");
    }
    return 0;


}
