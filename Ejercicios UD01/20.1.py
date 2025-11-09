#Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
#su factura N! siendo el factorial:

import math

num = int(input("Introduce un número y calcularé su factorial: "))

if num < 0:
    print("El número debe ser diferente de 0")
else:
    resultado = math.factorial(num)
    print(f"El factorial de {num} es: {resultado}")