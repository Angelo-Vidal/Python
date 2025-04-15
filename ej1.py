# Solicita al usuario que ingrese su nombre y lo guarda en la variable 'nombre'
nombre = input("Ingrese su nombre: ")

# Solicita el año actual, lo convierte a entero y lo guarda en la variable 'act'
act = int(input("Ingrese año actual: "))

# Solicita el año de nacimiento, lo convierte a entero y lo guarda en la variable 'nac'
nac = int(input("Ingrese año de nacimiento: "))

# Calcula la edad restando el año de nacimiento del año actual
edad = act - nac

# Imprime un mensaje con el nombre y la edad calculada usando f-string
print(f"{nombre} tiene {edad} años")