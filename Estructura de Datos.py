# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos ID, nombre, cantidad y precio.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters para cada atributo
    def get_id_producto(self):
        return self.id_producto

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
        """
        Método especial para representar el objeto como una cadena.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía de productos.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario, asegurándose de que el ID sea único.
        """
        for prod in self.productos:
            if prod.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        """
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                self.productos.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        """
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    prod.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    prod.set_precio(nuevo_precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: No se encontró un producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos en el inventario por nombre. Puede haber nombres similares.
        """
        productos_encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for prod in productos_encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            print("Inventario de productos:")
            for prod in self.productos:
                print(prod)
        else:
            print("El inventario está vacío.")

# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()