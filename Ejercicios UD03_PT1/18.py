#Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10.

num = int(input("Introduce un número y te diré si es multiplo de 10: "))

if num % 10 == 0:
    print(f"El número {num} es multiplo de 10")
else:
    print(f"El número {num} no es multiplo de 10")
