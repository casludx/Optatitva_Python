#Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

texto = str(input("Introduce una cadena de texto: "))
caracter = str(input("Introduce el caracter que quieras comprobar: "))

contador = 0

for i in texto:
    if i == caracter:
        contador += 1

print(f"El caracter que has elegido aparece {contador} veces")