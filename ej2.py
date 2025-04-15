# Solicita al usuario que ingrese su nombre y lo guarda en la variable 'nombre'
nombre = input("Ingresa tu nombre: ")

# Solicita la primera nota, la convierte a número decimal y la guarda en 'n1'
n1 = float(input("Ingresa la primera nota: "))

# Solicita la segunda nota, la convierte a número decimal y la guarda en 'n2'
n2 = float(input("Ingresa la segunda nota: "))

# Suma las dos notas y guarda el resultado en la variable 'suma'
suma = n1 + n2

# Calcula el promedio dividiendo la suma entre 2 y lo guarda en 'prom'
prom = suma / 2

# Muestra un mensaje con el nombre del usuario y su promedio
print(f"{nombre} tu promedio es: {prom}")