# Función para ingresar temperaturas diarias
def ingresar_temperatura_dia(dia):
  """
  Función para ingresar la temperatura de un día específico.

  Args:
    dia: Nombre del día de la semana (en minúscula).

  Returns:
    La temperatura ingresada como un valor flotante.
  """
  while True:
    try:
      temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
      break
    except ValueError:
      print("Error: Ingrese un valor numérico válido para la temperatura.")

  return temperatura

def calcular_promedio_semanal(temperaturas):
  """
  Función para calcular el promedio semanal de temperaturas.

  Args:
    temperaturas: Lista que contiene las temperaturas de cada día.

  Returns:
    El promedio semanal de temperaturas como un valor flotante.
  """
  if len(temperaturas) != 7:
    raise ValueError("La lista de temperaturas debe contener 7 valores.")

  promedio = sum(temperaturas) / len(temperaturas)
  return promedio

def main():
  """
  Función principal del programa.
  """
  temperaturas_semanales = []

  for dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
    temperatura_dia = ingresar_temperatura_dia(dia)
    temperaturas_semanales.append(temperatura_dia)

  promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
  print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} grados Celsius")

if __name__ == "__main__":
  main()

