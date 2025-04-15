# Solicita al usuario que ingrese el salario anterior y lo convierte a número decimal
previous_salary = float(input("Ingrese el salario anterior del obrero: "))

# Calcula el incremento del 25% multiplicando el salario anterior por 0.25
increase = previous_salary * 0.25

# Calcula el nuevo salario sumando el salario anterior más el incremento
new_salary = previous_salary + increase

# Muestra el salario anterior formateado con 2 decimales
print(f"Salario anterior: ${previous_salary:.2f}")
# Muestra el incremento formateado con 2 decimales
print(f"Incremento (25%): ${increase:.2f}")
# Muestra el nuevo salario formateado con 2 decimales
print(f"Nuevo salario: ${new_salary:.2f}")
