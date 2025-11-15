"""
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado.    
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
        print(" " * (altura - i) + "*" * (2 * i - 1))    