#include <stdio.h>
#include <time.h>

// Algoritmo recursivo de Euclides
int mcd(int a, int b) {
    if (b == 0) return a;
    return mcd(b, a % b);
}
int main() {
    int a = 1071, b = 462;
    
    clock_t inicio = clock();
    
    // Ejecutamos 1,000,000 de veces para que el tiempo sea medible
    for (int i = 0; i < 1000000; i++) {
        mcd(a, b);
    }
    
    clock_t fin = clock();
    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Resultado en C: %d\n", mcd(a, b));
    printf("Tiempo para 1 millon de iteraciones: %f segundos\n", tiempo);
    
    return 0;
}