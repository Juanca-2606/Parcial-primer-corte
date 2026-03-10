def afd_identificador(cadena):
    # Estado 0: Inicio, Estado 1: Aceptado, Estado -1: Error
    estado = 0
    
    for caracter in cadena:
        if estado == 0:
            if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
                estado = 1
            else:
                estado = -1
                break
        elif estado == 1:
            if (caracter >= 'a' and caracter <= 'z') or \
               (caracter >= 'A' and caracter <= 'Z') or \
               (caracter >= '0' and caracter <= '9'):
                estado = 1
            else:
                estado = -1
                break
                
    if estado == 1:
        return "ACEPTE"
    else:
        return "NO ACEPTE"

# Lectura del archivo linea por linea
archivo = open("prueba_id.txt", "r")

print("RESULTADOS DE LAS PRUEBAS:")
for linea in archivo:
    ID = linea.strip() 
    if ID:
        resultado = afd_identificador(ID)
        print("ID:", ID, "->", resultado)

archivo.close()