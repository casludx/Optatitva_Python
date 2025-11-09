#Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
#mensaje indicando cuántos son positivos y cuantos negativos.

contador_negativos = 0
contador_positivo = 0
contador = 0

while contador < 100:
    entrada = int(input(f"Dame el números {contador + 1}: "))
    if entrada == 0:
        print("No introduzcas el número 0")
    else:
        contador = contador + 1
        
        if entrada < 0:
            contador_negativos = contador_negativos + 1
        else:
            contador_positivo = contador_positivo + 1

print(f"Se han leído {contador_negativos} números negativos")
print(f"Se han leído {contador_positivo} números positivos")