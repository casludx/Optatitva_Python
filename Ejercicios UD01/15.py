#Dibuja un ordinograma de un programa que lee dos números y muestra el mayor.

num1 = int(input("Introduce el primero número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El número mayor es el: {num1}")
else:
    print(f"El número mayor es el: {num2}")