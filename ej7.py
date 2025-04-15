# Solicita al usuario ingresar el sueldo base y lo convierte a número decimal
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))

# Solicita al usuario ingresar el monto de la primera venta y lo convierte a número decimal
venta1 = float(input("Ingrese el monto de la primera venta: "))
# Solicita al usuario ingresar el monto de la segunda venta y lo convierte a número decimal
venta2 = float(input("Ingrese el monto de la segunda venta: "))
# Solicita al usuario ingresar el monto de la tercera venta y lo convierte a número decimal
venta3 = float(input("Ingrese el monto de la tercera venta: "))

# Calcula el total de las tres ventas sumándolas
total_ventas = venta1 + venta2 + venta3

# Calcula la comisión multiplicando el total de ventas por 10% (0.10)
comision = total_ventas * 0.10

# Calcula el sueldo total sumando el sueldo base más la comisión
sueldo_total = sueldo_base + comision

# Imprime un encabezado para los resultados
print("\nResultados:")
# Imprime la comisión por ventas con formato de 2 decimales
print(f"Comisión por ventas: ${comision:.2f}")
# Imprime el sueldo total del mes con formato de 2 decimales
print(f"Sueldo total del mes: ${sueldo_total:.2f}")
