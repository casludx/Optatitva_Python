#Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
#10 primeros números naturales.

suma = 0
producto = 1

for num in range(1, 11):
   suma = num + suma
   producto = num * producto
   
print(f"El resultado de la suma de los 10 primero números es: {suma}")
print(f"El resultado del producto de los 10 primero números es: {producto}")
    