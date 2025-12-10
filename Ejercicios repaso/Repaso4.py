numero = int(input("Introduce un número: "))

for i in range(1, numero + 1):
    print(str(i) * i)

for i in range(numero - 1, 0, -1):
    print(str(i) * i)
    
#####

N = int(input("Introduce el número de filas (N): "))

for i in range(1, N + 1):
    espacios = " " * (N - i)
    izquierda = ""
    
    for j in range(1, i + 1):
         izquierda = izquierda + str(j)
         derecha = ""
         
    for k in range(i - 1, 0, -1):
        derecha = derecha + str(k)
    
    print(espacios + izquierda + derecha)
    
#####

texto_guardado = ""

while True:
    print("1.- Introducir texto carácter a carácter (Pulsar = para finalizar el texto)")
    print("2.- Mostrar carácter a carácter")
    print("3.- Salir del programa")
    opcion = input("Seleccione una opción (1, 2 o 3): ")

    match opcion:
        case "1":
            entrada_bruta = input("Escriba el texto y pulse '=' para terminar: ")
            texto_guardado = "" 
            for caracter in entrada_bruta:
                texto_guardado += caracter
                if caracter == "=":
                    break
            print("Texto almacenado correctamente.")
        case "2":
            if not texto_guardado:
                print("ERROR: No hay ningún texto introducido. Use la opción 1 primero.")
            else:
                contador = 1
                for caracter in texto_guardado:
                    print(f"Letra {contador}:{caracter}")
                    contador += 1

        case "3":
            print("Saliendo del programa...")
            break 
        case _:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")