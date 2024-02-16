[[_TOC_]]

## strlen

### C

```c
#include <stdio.h>

int len(char* str) {
    int len = 0;
    while(str[len]) len++;
    return len;
}

void main() {
    char str[100] = "testing";
    printf("len(\"\") == %d.\n", len(""));
    printf("len(\"%s\") == %d.\n", str, len(str));
}
```

```c
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
```

```c
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
```

## strcpy

### C

```c
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
```

```c
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
```

## realloc

## Aritmetica de punteros

### C

```c
#include <stdio.h>

int main() {
    char s[] = "12345678";
    *((int*) s + 1) = '@';
    puts(s);
}
```

## Desbordamiento de buffer

### C

```c
// gcc password.c -fno-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define LEN 10

void main() {
    char password[LEN];
    char input[LEN];

    // Generacion de contraseña aleatoria
    srand(time(NULL));
    for (int i = 0; i < LEN; i++)
        password[i] = rand();

    // Lectura de contraseña por teclado
    printf("Ingrese la contraseña: ");
    scanf("%s", input);

    // Verificacion de contraseña
    if (!strncmp(input, password, LEN))
        printf("Contraseña correcta.\n");
    else
        printf("Contraseña incorrecta.\n");
}
```
