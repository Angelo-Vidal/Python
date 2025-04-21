aa = int(input("Ingrese año actual: "))
ca = int(input("Ingrese fecha: "))

diferencia = ca - aa

if diferencia == 0:
    print("Estamos en el mismo año", ca)
elif diferencia == 1:
    print("Faltamente un año para llegar al año ", ca)
elif diferencia == -1:
    print("Ha pasado un año desde el año ", ca)
elif diferencia > 1:
    print(f"Faltan {diferencia} años para llegar al año ", ca)
else:
    print(f"Han pasado {-diferencia} años desde el año {ca}")