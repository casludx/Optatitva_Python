#Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
#su factura N! siendo el factorial:

num = int(input("Introduce un número y calcularé su factorial: "))

if num < 0:
    print("El número debe ser mayo que cero")
else:
    factorial = 1
    for i in range(1, num +1):
        factorial *= i
        
print(f"El factorial de {num} es: {factorial}")