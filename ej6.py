# Programa para calcular descuento en una tienda
# Este programa calcula un descuento del 15% sobre el total de una compra

# Solicitar el total de la compra al usuario
# Usamos float() para convertir la entrada del usuario a número decimal
total_compra = float(input("Ingrese el total de la compra: "))

# Calcular el descuento (15%)
# Multiplicamos el total por 0.15 para obtener el 15% de descuento
descuento = total_compra * 0.15

# Calcular el precio final
# Restamos el descuento del total para obtener el precio final
precio_final = total_compra - descuento

# Mostrar resultados
# Usamos f-strings para formatear los números con 2 decimales
print(f"Total de la compra: ${total_compra:.2f}")  # Muestra el total original
print(f"Descuento (15%): ${descuento:.2f}")       # Muestra el monto del descuento
print(f"Precio final a pagar: ${precio_final:.2f}")  # Muestra el precio con descuento aplicado
