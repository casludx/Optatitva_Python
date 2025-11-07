#Dibuja un ordinograma de un programa que muestre los números desde el 1 hasta el
#número N que se introducirá por teclado

n = int(input("Dime un número y te mostrare todos los números hasta el que tu has dicho: "))

for num in range(1, n + 1):
    print(num)