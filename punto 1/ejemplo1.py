import os

def afd_ajedrez(movimiento):
    estado = 0
    
    # Normalizamos para que el split funcione con o sin espacios en ->
    procesado = movimiento.replace("->", " -> ").replace(" X ", " X ")
    tokens = procesado.split()

    for t in tokens:
        if estado == 0:
            if all(c in 'pkqrbn' for c in t.lower()):
                estado = 1
            else:
                return "RECHAZADO"

        elif estado == 1:
            if t == "->" or t == "X":
                estado = 2
            else:
                return "RECHAZADO"

        elif estado == 2:
            if len(t) >= 2 and t[-2] in 'abcdefgh' and t[-1] in '12345678':
                estado = 3
            # Tambien puede ser solo una pieza si es parte de la captura (ej: qn)
            elif all(c in 'pkqrbn' for c in t.lower()):
                estado = 2 
            else:
                return "RECHAZADO"

    return "ACEPTADO" if estado == 3 else "RECHAZADO"

if __name__ == "__main__":
    archivo_prueba = "prueba.txt"
    if os.path.exists(archivo_prueba):
        with open(archivo_prueba, "r") as f:
            for linea in f:
                mov = linea.strip()
                if mov:
                    resultado = afd_ajedrez(mov)
                    print(f"Movimiento: {mov:12} | Resultado: {resultado}")
    else:
        print(f"Error: No se encontro el archivo {archivo_prueba}")