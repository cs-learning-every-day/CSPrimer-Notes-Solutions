#include <stdio.h>
#include <stdlib.h>

struct box{
    int num;
};

struct box *make_box(int n){
    struct box *b = malloc(sizeof(struct box));
    b->num = n;
    return b;
}

int main() { printf("%d\n", make_box(42)->num);}
