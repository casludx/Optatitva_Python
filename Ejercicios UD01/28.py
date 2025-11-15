#Dibuja un ordinograma de un programa que suma independientemente los pares y los
#impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas
#sumas.

sum_impares = 0
sum_pares = 0

for i in range(100, 201):
    if i % 2 == 0:
        sum_pares += i
    else:
        sum_impares += i

print(f"La suma de todos los pares es: {sum_pares}")
print(f"La suma de todos los impares es: {sum_impares}")
