#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Inicialitza el generador de nombres aleatoris amb la hora actual
    srand(time(NULL));

    // Genera un nombre aleatori entre 0 i RAND_MAX
    int nombre_aleatori = rand();

    // Imprimeix el nombre aleatori
    printf("Nombre aleatori: %d\n", nombre_aleatori);

    return 0;
}
