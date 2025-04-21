n1 = int(input("ingrese primer numero: "))
n2 = int(input("ingrese Segundo numero: "))

 
if n2 == 0:
    print("Error , Ingrese numero 2 mayor a cero")
else:
    div = n1 / n2
    residuo= n1 % n2
    print(f"El resultado de la division es: {div}")

    if residuo == 0:
        print("La division es exacta")
    else:
        print("La division no es exacta ")