altura = int(input("Introduce la altura de la figura: "))

#Parte de arriba

for i in range(altura):
    if i == 0:
        print(" " * altura + "*")
    else:
        print(" " * (altura - i) + "*" + " " * (2 * i - 1) + "*")
        

#Parte de abajo

for i in range(altura - 2, -1, -1):
    if i != 0:
        print(" " * (altura - i) + "*" + " " * (2 * i - 1) + "*")
    else:
        print(" " * altura + "*")