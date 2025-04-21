# Pedir las 3 notas al usuario
n1 = float(input("Ingresa nota 1: "))
n2 = float(input("Ingresa nota 2: "))
n3 = float(input("Ingresa nota 3: "))

if n1 > 7 and n1 < 0 and n2 > 7 and n2 < 0 and n3 > 7 and n3 < 0:
    # Calcular el promedio
    promedio = (n1 + n2 + n3) / 3
    print(f"El promedio es: {promedio:.2f}")


    # Evaluar el promedio usando if
    if promedio >= 6.0:
        print("Eximido")    
    elif promedio >= 4.0:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("ingrese notas validas")
