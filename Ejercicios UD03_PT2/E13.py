"""
Crea una aplicación que dibuje una escalera de números, siendo cada línea números
empezando en uno y acabando en el numero de la línea.
"""

try:
    altura = int(input("Introduce la altura de la escalera: "))
    if altura <= 0:
        raise ValueError 
    
except ValueError:
    print("ERROR: Eres mu tonto, solamente números válidos enteros")
else:
#-------------------------------
    print("\nForma 1")
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print(j , end = "")
        print()

#-------------------------------
    print("\nForma 2")
    escalera = "1"
    for i in range(2, altura + 2):
        print(escalera)
        escalera = escalera + str(i)
        