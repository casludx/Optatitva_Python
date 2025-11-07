#Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
#producto y división (Ten en cuenta la división por cero).

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

while num2 == 0:
    print("ERROR! El número debe ser diferente de 0")
    num2 = int(input("Introduce de nuevo otro número: "))
    
suma = num1 + num2
print(f"La suma de ambos números es: {suma}")
resta = num1 - num2
print(f"La resta de ambos números es: {resta}")
multiplicacion = num1 * num2
print(f"La multiplicacion de ambos números es: {multiplicacion}")
division = num1 / num2
print(f"La división de ambos números es: {division}")
    