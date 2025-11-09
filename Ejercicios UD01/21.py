#Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
#mensaje de si ha leído número negativo o no.

contador_negativos = 0
contador = 0

while contador < 100:
    entrada = int(input(f"Dame el números {contador + 1}: "))
    if entrada == 0:
        print("No introduzcas el número 0")
    else:
        contador = contador + 1
        
        if entrada < 0:
            contador_negativos = contador_negativos + 1

if contador_negativos > 0:
    print(f"Se han leído {contador_negativos} números negativos")
else:
    print("No se ha leído ningún número negativo")