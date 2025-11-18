"""
Programa que lea un número positivo N y calcule y visualice su factorial N! 
"""

num = int(input("Introduce un número y calcularé su factorial: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i
    print(factorial)