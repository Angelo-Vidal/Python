# Solicita al usuario ingresar la primera nota parcial y la convierte a número decimal
n1 = float(input("Ingrese primera nota parcial: "))

# Solicita al usuario ingresar la segunda nota parcial y la convierte a número decimal
n2 = float(input("Ingrese segunda nota parcial: "))

# Solicita al usuario ingresar la tercera nota parcial y la convierte a número decimal
n3 = float(input("Ingrese tercera nota parcial: "))

# Solicita al usuario ingresar la nota del examen final y la convierte a número decimal
examen_final = float(input("Ingrese nota del examen final: "))

# Solicita al usuario ingresar la nota del trabajo final y la convierte a número decimal
trabajo_final = float(input("Ingrese nota del trabajo final: "))

# Calcula el promedio de las tres notas parciales
promedio_parciales = (n1 + n2 + n3) / 3

# Calcula la calificación final usando los porcentajes:
# 55% para promedio de parciales, 30% para examen final y 15% para trabajo final
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Muestra la calificación final formateada con dos decimales
print(f"Su calificación final es: {calificacion_final:.2f}")
