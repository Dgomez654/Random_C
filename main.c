#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int numero_aleatorio = rand();
    printf("Numero aleatorio: %d\n", numero_aleatorio);
    return 0;
}
