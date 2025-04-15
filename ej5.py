# Solicita al usuario que ingrese el monto de inversión y lo convierte a número decimal
capital = float(input("Ingrese el monto de inversión: "))

# Define la tasa de interés mensual como 2%
interest_rate = 0.02
# Calcula las ganancias multiplicando el capital por la tasa de interés
earnings = capital * interest_rate

# Calcula el monto total sumando el capital inicial más las ganancias
total = capital + earnings

# Imprime la inversión inicial formateada con 2 decimales
print(f"\nInversión inicial: ${capital:.2f}")
# Imprime la tasa de interés mensual convertida a porcentaje
print(f"Tasa de interés mensual: {interest_rate*100}%")
# Imprime las ganancias generadas formateadas con 2 decimales
print(f"Interés ganado: ${earnings:.2f}")
# Imprime el monto total después de un mes formateado con 2 decimales
print(f"Total después de un mes: ${total:.2f}")
