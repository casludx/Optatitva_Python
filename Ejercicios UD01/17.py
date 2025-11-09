#Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
#ascendente.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1}")
    print(f"{num2}")
else:
    print(f"{num2}")
    print(f"{num1}")