#Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
#van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.

hubo_diez = False

nota = int(input("Introduce una nota (0-10). Escribe -1 si quieres acabar el programa: "))

while nota != -1:
    if nota == 10:
        hubo_diez = True
        
    nota = int(input("Introduce una nota (0-10). Escribe -1 si quieres acabar el programa: "))

if hubo_diez == True:
    print("Se introdujo al menos una nota 10")
else:
    print("No se introdujo ninguna nota 10")