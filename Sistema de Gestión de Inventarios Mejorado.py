import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data_str):
        id_producto, nombre, cantidad, precio = data_str.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario_desde_archivo()

    def cargar_inventario_desde_archivo(self):
        """Carga los productos desde el archivo de inventario al iniciar el programa."""
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Se creará al añadir productos.")
            return

        try:
            with open(self.archivo, 'r') as f:
                for line in f:
                    producto = Producto.from_string(line)
                    self.productos[producto.id_producto] = producto
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado.")
        except PermissionError:
            print(f"No se tienen permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario_en_archivo(self):
        """Guarda el estado actual del inventario en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"No se tienen permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print(f"El producto con ID {id_producto} ya existe.")
            return

        producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos[id_producto] = producto
        self.guardar_inventario_en_archivo()
        print(f"Producto {nombre} añadido exitosamente.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print(f"Producto con ID {id_producto} no encontrado.")
            return

        producto = self.productos[id_producto]
        if nombre:
            producto.nombre = nombre
        if cantidad:
            producto.cantidad = cantidad
        if precio:
            producto.precio = precio
        self.guardar_inventario_en_archivo()
        print(f"Producto {id_producto} actualizado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario_en_archivo()
            print(f"Producto {id_producto} eliminado exitosamente.")
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Agregar productos
    inventario.agregar_producto("001", "Manzanas", 40, 0.35)
    inventario.agregar_producto("002", "Naranjas", 30, 0.25)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Actualizar producto
    inventario.actualizar_producto("001", cantidad=70)

    # Mostrar inventario actualizado
    inventario.mostrar_inventario()

    # Eliminar producto
    inventario.eliminar_producto("002")

    # Mostrar inventario final
    inventario.mostrar_inventario()