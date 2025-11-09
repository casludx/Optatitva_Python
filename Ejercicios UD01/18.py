#Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si
#son iguales.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 == num2:
    print("Ambos números son iguales")
else:
    if num1 > num2:
        print(f"El {num1} es el mayor")
    else:
        print(f"El {num2} es el mayor")