"""
Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:
"""

try:
    altura = int(input("Introduce la altura de la escalera: "))
    if altura <= 0:
        raise ValueError 
    
except ValueError:
    print("ERROR: Eres mu tonto, solamente números válidos enteros")
else:
#-------------------------------
    print("\n Forma 1")
    for i in range(1, altura + 1):
        for j in range(1, i +1 ):
            print("*", end = "")
        print()
        
#-------------------------------
    print("\n Forma 2")
    asterisco = "*"
    for i in range(1, altura + 1):
        print(asterisco)
        asterisco = asterisco + "*"

#-------------------------------
    print("\n Forma 3")
    for i in range(1, altura + 1):
        print("*" *i)