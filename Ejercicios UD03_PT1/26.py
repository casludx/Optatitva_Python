"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente
"""

dado1 = int(input("Introduce el resultado obtenido en el primer dado: "))
dado2 = int(input("Introduce el resultado obtenido en el segundo dado: "))
dado3 = int(input("Introduce el resultado obtenido en el tercer dado: "))

if dado1 == 6 and dado2 == 6 and dado3 == 6:
    print("Usted ha obtenido un resultado excelente")

elif dado1 == 6 and dado2 == 6:
    print("Usted ha obtenido un resultado muy bueno")
    
elif dado1 == 6 and dado3 == 6:
    print("Usted ha obtenido un resultado muy bueno")

elif dado2 == 6 and dado3 == 6:
    print("Usted ha obtenido un resultado muy bueno")
    
elif dado1 == 6 or dado2 == 6 or dado3 == 6:
    print("Usted ha obtenido un resultado regular")
    
else:
    print("Usted ha obtenido un resultado pesimo")
