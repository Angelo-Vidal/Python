# Solicita al usuario que ingrese su nombre y lo almacena en la variable 'nombre'
nombre = input("Ingrese su nombre: ")

# Solicita la primera nota y la convierte a número decimal
n1 = float(input("Ingrese la primera nota: "))

# Solicita la segunda nota y la convierte a número decimal
n2 = float(input("Ingrese la segunda nota: "))

# Solicita la tercera nota y la convierte a número decimal
n3 = float(input("Ingrese la tercera nota: "))

# Solicita la cuarta nota y la convierte a número decimal
n4 = float(input("Ingrese la cuarta nota: "))

# Solicita la quinta nota y la convierte a número decimal
n5 = float(input("Ingrese la quinta nota: "))

# Calcula la suma de todas las notas
suma = n1 + n2 + n3 + n4 + n5

# Calcula el promedio dividiendo la suma entre 5
prom = suma / 5

# Muestra el resultado con el nombre del estudiante y su promedio
print(f"{nombre} tu promedio es: {prom}")