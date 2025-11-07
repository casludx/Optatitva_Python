#Dibuja un ordinograma que toma como dato de entrada un número que corresponde a la
#longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
#de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
#círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la
#esfera que corresponde con dicho radio.

import math

radio = int(input("Introduzca el radio de la esfera: "))

diametro = radio * 2

longitud = 2 * math.pi * radio
area = math.pi * radio**2
volumen = 4/3 * math.pi * radio**3

print(f"La longitud de la esfera es: {longitud}")
print(f"El area de la esfera es: {area}")
print(f"El volumen de la esfera es: {volumen}")