#include <stdio.h>

int main() {
    char s[] = "12345678";
    *((int*) s + 1) = '@';
    puts(s);
}
