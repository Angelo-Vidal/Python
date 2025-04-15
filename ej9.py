# Solicita al usuario ingresar el número total de estudiantes y lo convierte a entero
total_estudiantes = int(input("Ingrese el número total de estudiantes: "))

# Solicita al usuario ingresar el número de estudiantes hombres y lo convierte a entero
estudiantes_hombres = int(input("Ingrese el número de estudiantes hombres: "))

# Calcula el número de estudiantes mujeres restando los hombres del total
estudiantes_mujeres = total_estudiantes - estudiantes_hombres

# Calcula el porcentaje de estudiantes hombres usando regla de tres
porcentaje_hombres = (estudiantes_hombres / total_estudiantes) * 100

# Calcula el porcentaje de estudiantes mujeres usando regla de tres
porcentaje_mujeres = (estudiantes_mujeres / total_estudiantes) * 100

# Muestra el porcentaje de estudiantes hombres formateado a 2 decimales
print(f"Porcentaje de estudiantes hombres: {porcentaje_hombres:.2f}%")

# Muestra el porcentaje de estudiantes mujeres formateado a 2 decimales
print(f"Porcentaje de estudiantes mujeres: {porcentaje_mujeres:.2f}%")
