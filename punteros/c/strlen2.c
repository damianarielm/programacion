#include <stdio.h>

int len(char* str) {
    int len = 0;
    while(*str++) len++;
    return len;
}

void main() {
    char str[100] = "testing";
    printf("len(\"\") == %d.\n", len(""));
    printf("len(\"%s\") == %d.\n", str, len(str));
}
