# Parcial Primer Corte 

El objetivo es demostrar el dominio de automatas, analizadores lexicos y sintacticos en los diferentes casos de uso.

## Estructura del Proyecto

El repositorio se organiza en cinco directorios independientes, cada uno con su respectivo codigo fuente y archivos de prueba:

* **PUNTO 1**: Implementacion de un AFD para validacion de movimientos de ajedrez.
* **PUNTO 2**: Implementacion de un AFD para identificadores de variables.
* **PUNTO 3**: Calculadora de raiz cuadrada mediante Flex, Bison y Newton-Raphson.
* **PUNTO 4**: Analisis comparativo de rendimiento (Euclides) en C y Haskell.
* **PUNTO 5**: Calculo de la serie de Maclaurin para e^x utilizando ANTLR.

---

## Punto 1: AFD para Movimientos de Ajedrez

Se desarrollo un Automata Finito Determinista capaz de reconocer una gramatica simplificada para el registro de jugadas. El sistema valida piezas atacantes, operadores de accion y casillas de destino.

### Logica del Sistema
El programa procesa cadenas de texto y transita entre estados criticos:
1. **Validacion de Pieza**: Reconocimiento de caracteres (p, k, q, r, b, n).
2. **Validacion de Operador**: Identificacion de movimiento simple (->) o captura (X).
3. **Validacion de Casilla**: Verificacion de coordenadas dentro del rango a1-h8.



### Instrucciones de Ejecucion
1. Navegar a la carpeta `PUNTO 1`.
2. Ejecutar el comando: `python punto1.py`.
3. El script leera automaticamente el archivo `prueba.txt`.

```bash
cd "PUNTO 1"
python punto1.py
```
---

## Punto 2: AFD para Identificadores (ID)

Se implemento la logica para validar identificadores basados en la expresion regular `[A-Za-z][A-Za-z0-9]*`. Esta es la base de la definicion de variables en la mayoria de los lenguajes compilados.

### Analisis de la Solucion
El codigo no utiliza librerias externas de expresiones regulares para demostrar el funcionamiento puro del automata. Compara caracter por caracter para asegurar que el primer elemento sea una letra y los subsecuentes sean alfanumericos.

### Pruebas Realizadas
Se utiliza el archivo `prueba_id.txt` con los siguientes casos:
* **Aceptados**: Variable1, temp, x.
* **Rechazados**: 1valor (error por inicio numerico), id_total (error por caracter especial).
  
```bash
cd "PUNTO 2"
python punto2.py
```
* Se utiliza el archivo prueba_id.txt que contiene casos aceptados (Variable1, temp, x) y rechazados (1valor, id_total).

---

## Punto 3: Calculadora de Raiz Cuadrada (Flex y Bison)

Implementacion de una calculadora de alta precision que utiliza el metodo numerico de Newton-Raphson para obtener raices cuadradas de numeros reales.

### Metodo de Newton-Raphson
La logica se basa en la formula de aproximacion sucesiva: `x(n+1) = 0.5 * (x(n) + S / x(n))`. El programa realiza multiples iteraciones para garantizar la convergencia hacia el resultado correcto de la raiz cuadrada de S.



### Compilacion y Ejecucion
1. Generar los archivos fuente: `flex ejerc3.l` y `bison -d ejerc3.y`.
2. Compilar el ejecutable: `gcc lex.yy.c ejerc3.tab.c -o calculadora -lm`.
3. Ejecutar: `./calculadora` (el programa procesara las entradas de `Entrada.txt`).

```bash
cd "PUNTO 3"
flex ejerc3.l
bison -d ejerc3.y
gcc lex.yy.c ejerc3.tab.c -o calculadora -lm
./calculadora
```
---

## Punto 4: Algoritmo de Euclides (C y Haskell)

Este punto realiza una comparacion profunda entre el paradigma imperativo y el paradigma declarativo utilizando el algoritmo de Maximo Comun Divisor (MCD).

### Comparativa 
* **C (Imperativo)**: Implementa la recursion de forma directa sobre la pila. Destaca por su velocidad de ejecucion y bajo consumo de recursos en sistemas de tiempo real.
* **Haskell (Declarativo)**: Define el problema como una relacion matematica. Utiliza Tail Call Optimization (TCO) para optimizar la recursion de cola, permitiendo un rendimiento competitivo con un codigo mucho mas legible.

### Cuadro Comparativo 

| Caracteristica | (C) | (Haskell) |
| :--- | :--- | :--- |
| **Enfoque** | Se centra en el "Como" (pasos y estados). | Se centra en el "Que" (definiciones logicas). |
| **Estado** | Las variables cambian su valor en memoria. | Las variables son inmutables (constantes). |
| **Recursion** | Puede ser costosa si no se optimiza. | Es la base del lenguaje y usa TCO (Tail Call Optimization). |
| **Transparencia Referencial** | No posee (depende del contexto y tiempo). | Si posee (mismo input siempre da mismo output). |
| **Control de Flujo** | Usa ciclos como for, while y saltos. | Usa recursion y funciones de orden superior. |

### Ejecucion de Pruebas
* **C**: `gcc punto4.c -o punto4_c && ./punto4_c`
* **Haskell**: `runhaskell punto4.hs`
* Ambos programas consumen el archivo `prueba_euclides.txt`.
  
```bash
cd "PUNTO 4"
gcc punto4.c -o punto4_c
./punto4_c
```
---

## Punto 5: Serie de Maclaurin (ANTLR)

Se construyo un programa que calcula la aproximacion de la funcion exponencial e^x utilizando los primeros n terminos de la serie de Maclaurin.

### Desarrollo con ANTLR
Se definio una gramatica en el archivo de gramatica para parsear las instrucciones de evaluacion. La ejecucion matematica se delega a un script de Python que aplica la sumatoria de terminos de la forma (x^i / i!).


### Ejecucion
1. Ejecutar: `python punto5.py`.
2. El sistema tomara los valores de x y los limites n desde el archivo `pruebas_maclaurin.txt`.

```bash
cd "PUNTO 5"
python punto5.py
```
---

## Conclusion de Pruebas

Para cada uno de los puntos, se han integrado archivos de texto externos (.txt) que contienen los casos de prueba solicitados. Esto asegura la repetibilidad de los resultados y permite verificar el comportamiento del software ante entradas correctas y erroneas sin necesidad de modificar el codigo fuente.


 
