import math

def calcular_maclaurin(x, n_terminos):
    suma_total = 0.0
    print(f"\nCalculando e^{x} con {n_terminos} terminos:")
    
    for i in range(int(n_terminos)):
        # Formula de la imagen: x^n / n!
        termino = (x**i) / math.factorial(i)
        suma_total += termino
        print(f"  Termino {i}: {termino:.6f}")
    
    print(f"Resultado final: {suma_total:.8f}")
    print(f"Valor real (math.exp): {math.exp(x):.8f}")

def ejecutar_pruebas():
    # Abrimos el archivo de pruebas
    try:
        with open("pruebas_maclaurin.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) == 3:
                    val_x = float(partes[1].split('=')[1])
                    val_n = int(partes[2].split('=')[1])
                    calcular_maclaurin(val_x, val_n)
    except FileNotFoundError:
        print("Error: No se encontro pruebas_maclaurin.txt")

if __name__ == "__main__":
    ejecutar_pruebas()