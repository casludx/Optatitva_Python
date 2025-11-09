#Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
#que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
#cuantos negativos

contador_negativos = 0
contador_positivo = 0

while True:
    entrada = int(input(f"Dame un número: "))
    if entrada == 0:
        print("Has introducido un 0 y el programa termina")
        break
    else:
        
        if entrada < 0:
            contador_negativos = contador_negativos + 1
        else:
            contador_positivo = contador_positivo + 1
            
print(f"Se han leído {contador_negativos} números negativos")
print(f"Se han leído {contador_positivo} números positivos")