"""
Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto
"""

print("-" * 40)
print("Bienvenido, inicie sesión")
usuario = str(input("Introduce su nombre de usuario: "))
contraseña = str (input("Introduce su contraseña: "))
print("-" * 40)

if usuario == "Lucas" and contraseña == "Lucas123":
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario o contraseña incorrecto")