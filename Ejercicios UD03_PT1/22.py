"""
Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo.
"""

horas = int(input("Introduce la hora (0-23): "))
minutos = int(input("Introduce los minutos (0-60): "))
segundos = int(input("Introduce los segundos (0-60): "))

if not (0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59):
    print("Los datos introducidos no son correctos")
    
segundos += 1

if segundos == 60:
    segundos = 0
    minutos += 1
    
    if minutos == 60:
        minutos = 0
        horas += 1
    
        if horas == 24:
            horas = 0
            
print("\nLa hora un segundo despues es: ")
print(f"{horas:02}:{minutos:02}:{segundos:02}")
