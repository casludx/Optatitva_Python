#Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).
resultado = ""
entrada = " "
while entrada != "":
    entrada = str(input("Ve introduciendo caracteres, cuando quieras parar introduce presiona el enter vacio: "))
    resultado = resultado + entrada

print(resultado)