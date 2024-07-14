class Persona:
    """
    Clase que representa a una persona.

    Atributos:
        nombre (str): El nombre de la persona.
        edad (int): La edad de la persona.

    Métodos:
        __init__(self, nombre, edad): Constructor de la clase.
        __del__(self): Destructor de la clase.
        saludar(self): Muestra un mensaje de saludo.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Inicializa los atributos `nombre` y `edad` de la persona.

        Args:
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

        print(f"Creando persona: {self.nombre} ({self.edad} años)")

    def __del__(self):
        """
        Destructor de la clase Persona.

        Se ejecuta cuando la instancia de la clase ya no se utiliza.

        Muestra un mensaje de despedida.
        """
        print(f"Despidiendo persona: {self.nombre} ({self.edad} años)")

    def saludar(self):
        """
        Muestra un mensaje de saludo de la persona.
        """
        print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años.")


# Ejemplo de uso

persona1 = Persona("Marco", 32)
persona1.saludar()

# La persona1 se elimina automáticamente al salir del bloque de código.
# Se ejecuta el destructor.

persona2 = Persona("María", 37)
persona2.saludar()

del persona2  # Eliminación explícita de la persona2
# Se ejecuta el destructor.