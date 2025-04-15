# Muestra el título del programa
print("Calculadora de pulsaciones por cada 10 segundos de ejercicio")

# Solicita la edad al usuario y la convierte a número entero
edad = int(input("Ingrese su edad: "))

# Calcula las pulsaciones usando la fórmula: (220 - edad) / 10
pulsaciones = (220 - edad) / 10

# Muestra los resultados formateados
print(f"Para una persona de {edad} años:")
print(f"Número de pulsaciones por cada 10 segundos de ejercicio: {pulsaciones:.1f}")
