#include <stdio.h>

void strcopy(char* dst, char* src) {
    while (*dst++ = *src++);
}

void main() {
    char src[100] = "testing";
    char dst[100] = "";

    printf("BEFORE: src == \"%s\"; dst == \"%s\".\n", src, dst);
    strcopy(dst, src);
    printf("AFTER: src == \"%s\"; dst == \"%s\".\n", src, dst);
}
