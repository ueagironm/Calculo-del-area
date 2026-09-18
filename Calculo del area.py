# Programa para calcular el área de un rectángulo

def calcular_area(base, altura):
    area = base * altura
    return area


# Datos de entrada
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Llamada a la función
resultado = calcular_area(base, altura)

# Mostrar el resultado
print("El área del rectángulo es:", resultado)