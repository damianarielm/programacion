#include <stdio.h>

int len(char* str) {
    char* end = str;
    while(*end++);
    return end - str - 1;
}

void main() {
    char str[100] = "testing";
    printf("len(\"\") == %d.\n", len(""));
    printf("len(\"%s\") == %d.\n", str, len(str));
}
