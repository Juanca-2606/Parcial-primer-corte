%{
#include <stdio.h>
#include <stdlib.h>

/* Algoritmo Newton-Raphson simplificado para el parcial */
double calcular_raiz(double s) {
    if (s < 0) return -1.0;
    if (s == 0) return 0.0;

    double x = s / 2.0; // Estimacion inicial
    for (int i = 0; i < 15; i++) {
        // x = x - (x^2 - s) / (2x)
        x = 0.5 * (x + (s / x));
    }
    return x;
}

extern FILE *yyin;
int yylex();
void yyerror(const char *s);
%}

%union {
    double fval;
}

%token <fval> NUM
%token SQRT

%%
input:
    | input linea
    ;

linea:
    SQRT '(' NUM ')' { 
        double res = calcular_raiz($3);
        if (res == -1.0) 
            printf("Error: No existe raiz real de %.2f\n", $3);
        else 
            printf("sqrt(%.2f) = %.6f\n", $3, res); 
    }
    ;

%%

int main() {
    // Lectura desde archivo de texto segun el punto 3
    FILE *archivo = fopen("entrada.txt", "r");
    if (!archivo) {
        printf("Error: No se pudo abrir entrada.txt\n");
        return 1;
    }

    yyin = archivo;
    yyparse(); // Inicia el proceso de la calculadora
    
    fclose(archivo);
    return 0;
}

void yyerror(const char *s) {
    printf("Error sintactico: %s\n", s);
}