class RegistroClima:
  """
  Clase para representar la información diaria del clima.

  Atributos:
    dia: Nombre del día de la semana (en minúscula).
    temperatura: Temperatura del día en grados Celsius.
  """

  def __init__(self, dia, temperatura):
    self.dia = dia
    self.temperatura = temperatura

  def ingresar_temperatura(self):
    """
    Método para ingresar la temperatura del día.
    """
    while True:
      try:
        self.temperatura = float(input(f"Ingrese la temperatura para el día {self.dia}: "))
        break
      except ValueError:
        print("Error: Ingrese un valor numérico válido para la temperatura.")

  def calcular_promedio_semanal(self, registros_clima):
    """
    Método para calcular el promedio semanal de temperaturas a partir de una lista de registros.

    Args:
      registros_clima: Lista de objetos RegistroClima que representan los datos de cada día.

    Returns:
      El promedio semanal de temperaturas como un valor flotante.
    """
    if len(registros_clima) != 7:
      raise ValueError("La lista de registros de clima debe contener 7 objetos.")

    temperaturas = [registro.temperatura for registro in registros_clima]
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
  """
  Función principal del programa.
  """
  registros_semanales = []

  for dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
    registro_dia = RegistroClima(dia, 0)
    registro_dia.ingresar_temperatura()
    registros_semanales.append(registro_dia)

  promedio_semanal = registros_semanales[0].calcular_promedio_semanal(registros_semanales)
  print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} grados Celsius")

if __name__ == "__main__":
  main()