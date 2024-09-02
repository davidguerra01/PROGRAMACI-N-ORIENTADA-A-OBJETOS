class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
import json

class Inventario:
    def __init__(self):
        self.productos = {}  # Usando un diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump([vars(producto) for producto in self.productos.values()], f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_data = json.load(f)
                self.productos = {producto['id']: Producto(**producto) for producto in productos_data}
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")
class SistemaGestionInventario:
    def __init__(self):
        self.inventario = Inventario()

    def menu(self):
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("0. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            self.inventario.añadir_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == 2:
            id = input("ID del producto a eliminar: ")
            self.inventario.eliminar_producto(id)
        elif opcion == 3:
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            self.inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == 4:
            nombre = input("Nombre del producto a buscar: ")
            resultados = self.inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")
        elif opcion == 5:
            self.inventario.mostrar_productos()
        elif opcion == 6:
            archivo = input("Nombre del archivo para guardar: ")
            self.inventario.guardar_inventario(archivo)
            print("Inventario guardado.")
        elif opcion == 7:
            archivo = input("Nombre del archivo para cargar: ")
            self.inventario.cargar_inventario(archivo)
            print("Inventario cargado.")

if __name__ == "__main__":
    sistema = SistemaGestionInventario()
    while True:
        sistema.menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 0:
            break
        sistema.ejecutar_opcion(opcion)

