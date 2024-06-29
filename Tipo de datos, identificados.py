# Calcular el área de un rectángulo y un círculo

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return base * altura


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    import math
    return math.pi * radio ** 2


# Variables para almacenar las dimensiones
base_rectangulo = 9.0  # Base del rectángulo (float)
altura_rectangulo = 7.0  # Altura del rectángulo (float)
radio_circulo = 4.0  # Radio del círculo (float)

# Calcular el área del rectángulo
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print(f"El área del rectángulo es: {area_rectangulo} unidades cuadradas.")

# Calcular el área del círculo
area_circulo = calcular_area_circulo(radio_circulo)
print(f"El área del círculo es: {area_circulo} unidades cuadradas.")

# Variable booleana para indicar si el área del rectángulo es mayor que la del círculo
es_area_rectangulo_mayor = area_rectangulo > area_circulo
print(f"¿El área del rectángulo es mayor que la del círculo? {es_area_rectangulo_mayor}")