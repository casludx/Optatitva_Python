numero = int(input("Introduce un número: "))

for i in range(1, numero + 1):
    print(str(i) * i)

for i in range(numero - 1, 0, -1):
    print(str(i) * i)