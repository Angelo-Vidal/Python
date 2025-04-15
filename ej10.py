# Imprime una línea divisoria para mejorar la presentación
print("--------------------------")
# Imprime el título del programa
print("Calculadora de masa de aire")
# Imprime otra línea divisoria
print("--------------------------")

# Solicita y almacena el valor de la presión, convirtiéndolo a número decimal
presion = float(input("Ingrese la presión: "))
# Solicita y almacena el valor del volumen, convirtiéndolo a número decimal
volumen = float(input("Ingrese el volumen: "))
# Solicita y almacena el valor de la temperatura, convirtiéndolo a número decimal
temperatura = float(input("Ingrese la temperatura: "))

# Calcula la masa del aire usando la fórmula: masa = (presión * volumen)/(0.37 * (temperatura + 460))
masa = (presion * volumen)/(0.37 * (temperatura + 460))

# Imprime el resultado formateado a 2 decimales
print(f"\nLa masa del aire es: {masa:.2f}")
