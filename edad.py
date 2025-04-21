edad = int(input("Ingresa Año de nacimiento: "))

an_ac=2025

Edad = an_ac - edad
if Edad < 18 :
    print(f"Eres menor de edad: {Edad}")
elif Edad > 65:
    print(f"Eres de la tercera edad: {Edad}")
else:
    print(f"Eres mayor de edad: {Edad}")