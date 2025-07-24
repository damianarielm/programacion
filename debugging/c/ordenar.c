#include <stdio.h>

int main() {
    int numero1, numero2, numero3;

    printf("Ingrese un numero: ");
    scanf("%d", &numero1);
    printf("Ingrese otro numero: ");
    scanf("%d", &numero2);
    printf("Ingrese otro numero: ");
    scanf("%d", &numero3);

    if (numero1 < numero2 < numero3)
        printf("%d < %d < %d.\n", numero1, numero2, numero3);
    else if (numero1 < numero3 < numero2)
        printf("%d < %d < %d.\n", numero1, numero3, numero2);
    else if (numero2 < numero1 < numero3)
        printf("%d < %d < %d.\n", numero2, numero1, numero3);
    else if (numero2 < numero3 < numero1)
        printf("%d < %d < %d.\n", numero2, numero3, numero1);
    else if (numero3 < numero1 < numero2)
        printf("%d < %d < %d.\n", numero3, numero1, numero2);
    else
        printf("%d < %d < %d.\n", numero3, numero2, numero1);
}
