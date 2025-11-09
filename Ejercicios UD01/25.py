#Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y puntue la calificacion

nota = float(input("Introduce la nota que has tenido en la asignatura (0-10): "))

if nota < 0 or nota > 10:
    print("Introduce un valor entre 0 y 10")
elif nota < 3:
    print("Tu nota es: Muy Deficiente")
elif nota < 5:
    print("Tu nota es: Insuficiente")
elif nota < 6:
    print("Tu nota es: Suficiente")
elif nota < 7:
    print("Tu nota es: Bien")
elif nota < 9:
    print("Tu note es: Notable:")

else:
    print("Tu nota es: Sobresaliente")

