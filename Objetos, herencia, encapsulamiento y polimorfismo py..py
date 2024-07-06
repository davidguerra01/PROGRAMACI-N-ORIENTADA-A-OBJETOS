# Clase base Empleado
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self._salario = salario  # Atributo privado para demostración de encapsulación

    def obtener_informacion(self):
        """
        Método para obtener la información del empleado.
        """
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: ${self._salario}"

    def obtener_salario(self):
        """
        Método para obtener el salario del empleado.
        """
        return self._salario

    def incrementar_salario(self, incremento):
        """
        Método para incrementar el salario del empleado.
        """
        self._salario += incremento

# Clase derivada Gerente, que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def obtener_informacion(self):
        """
        Sobrescribe el método para incluir el departamento del gerente.
        """
        informacion_base = super().obtener_informacion()
        return f"{informacion_base}, Departamento: {self.departamento}"

# Demostración de polimorfismo y uso de las clases

# Creación de instancias de las clases
empleado1 = Empleado("Diego Ochoa", 27, 460)
gerente1 = Gerente("Rosa Pillajo", 42, 1250, "Recursos Humanos")

# Uso de los métodos para mostrar la funcionalidad
print("Información del empleado:")
print(empleado1.obtener_informacion())

print("\nInformación del gerente:")
print(gerente1.obtener_informacion())

# Incremento de salario utilizando encapsulación
print("\nIncrementando salario del empleado y del gerente...")
empleado1.incrementar_salario(100)
gerente1.incrementar_salario(150)

print("\nInformación del empleado después del incremento de salario:")
print(empleado1.obtener_informacion())

print("\nInformación del gerente después del incremento de salario:")
print(gerente1.obtener_informacion())

# Verificación de polimorfismo
empleados = [empleado1, gerente1]
print("\nDemostración de polimorfismo:")
for empleado in empleados:
    print(empleado.obtener_informacion())