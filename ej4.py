# Conversor simple de USD a CLP

# Solicitamos al usuario que ingrese el monto en dólares y lo convertimos a float
usd = float(input("Ingrese monto en USD: "))

# Multiplicamos el monto en USD por el tipo de cambio actual (970.87 CLP por 1 USD)
clp = usd * 970.87

# Mostramos el resultado de la conversión usando f-strings para formatear el texto
print(f"${usd} USD = ${clp} CLP")
