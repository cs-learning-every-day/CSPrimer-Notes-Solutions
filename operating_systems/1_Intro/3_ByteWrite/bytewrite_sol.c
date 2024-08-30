#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#define ONE_MEG 1 << 20

int main(){
    int f = open("test.txt", O_WRONLY | O_TRUNC);
    struct stat st;
    int prior_blocks = -1;
    for (int i=0; i< ONE_MEG;i++){
        write(f, ".", 1);
        fstat(f, &st);
        if (st.st_blocks != prior_blocks){
            printf(
                "Size: %lld, blocks: %lld, on disk: %lld\n",
                st.st_size,
                st.st_blocks,
                st.st_blocks * 512
            );
            prior_blocks = st.st_blocks;
        }
    }

}
