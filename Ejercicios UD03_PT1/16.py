#Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.

num = int(input("Introduce un número entre el 0 y el 99999 y te diré cuantas cifras tiene: "))

print(f"Tu número tiene {len(str(num))} cifras")