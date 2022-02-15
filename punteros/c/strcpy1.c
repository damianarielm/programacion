#include <stdio.h>

void strcopy(char* dst, char* src) {
    int i;
    for (i = 0; src[i]; i++)
        dst[i] = src[i];
    dst[i + 1] = '\0';
}

void main() {
    char src[100] = "testing";
    char dst[100] = "";

    printf("BEFORE: src == \"%s\"; dst == \"%s\".\n", src, dst);
    strcopy(dst, src);
    printf("AFTER: src == \"%s\"; dst == \"%s\".\n", src, dst);
}
