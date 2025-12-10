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