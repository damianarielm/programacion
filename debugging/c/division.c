#include <stdio.h>

int main() {
    int dividendo, divisor;

    printf("Ingrese un divisor distinto de 0: ");
    scanf("%d", &divisor);

    if (divisor != 0)
        printf("Ingrese un dividendo: ");
        scanf("%d", &dividendo);
        printf("%d / %d = %d.\n", dividendo, divisor, dividendo / divisor);
}
