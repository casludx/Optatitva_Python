# 1. Leer los tres números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 == num2 and num2 == num3:
    print(f"Los tres números son iguales (todos son {num1})")

else:
    if num1 == num2:
        print(f"El primer y segundo número son iguales ({num1}).")
        if num1 > num3:
            print(f"El mayor es {num1} (el primero y el segundo)")
            print(f"El menor es {num3}")
        else:
            print(f"El mayor es {num3}")
            print(f"El menor es {num1} (el primero y el segundo)")

    elif num1 == num3:
        print(f"El primer y tercer número son iguales ({num1}).")
        if num1 > num2:
            print(f"El mayor es {num1} (el primero y el tercero)")
            print(f"El menor es {num2}")
        else:
            print(f"El mayor es {num2}")
            print(f"El menor es {num1} (el primero y el tercero)")

    elif num2 == num3:
        print(f"El segundo y tercer número son iguales ({num2}).")
        if num2 > num1:
            print(f"El mayor es {num2} (el segundo y el tercero)")
            print(f"El menor es {num1}")
        else:
            print(f"El mayor es {num1}")
            print(f"El menor es {num2} (el segundo y el tercero)")

    else:
        print("Los tres números son distintos.")
        
        if num1 > num2 and num1 > num3:
            mayor = num1
        elif num2 > num1 and num2 > num3:
            mayor = num2
        else:
            mayor = num3
            
        if num1 < num2 and num1 < num3:
            menor = num1
        elif num2 < num1 and num2 < num3:
            menor = num2
        else:
            menor = num3
        
        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")