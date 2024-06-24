# sistema_reservas.py

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


class Reserva:
    def __init__(self, cliente, fecha, hora, num_personas):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        self.num_personas = num_personas

    def __str__(self):
        return (f"Reserva para {self.cliente.nombre} el {self.fecha} a las {self.hora} "
                f"para {self.num_personas} personas.")


class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        print("Reserva agregada:", reserva)

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(reserva)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear clientes
    cliente1 = Cliente("David Hidalgo", "david.hidalgo@gmail.com")
    cliente2 = Cliente("Mary Morales", "mary.morales@outlook.com")

    # Crear reservas
    reserva1 = Reserva(cliente1, "2024-06-10", "19:00", 2)
    reserva2 = Reserva(cliente2, "2024-07-12", "16:00", 4)

    # Sistema de reservas
    sistema_reservas = SistemaReservas()
    sistema_reservas.agregar_reserva(reserva1)
    sistema_reservas.agregar_reserva(reserva2)

    # Mostrar todas las reservas
    print("\nListado de Reservas:")
    sistema_reservas.mostrar_reservas()