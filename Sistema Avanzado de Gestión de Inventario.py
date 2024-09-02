class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    import pickle  # Para la serialización y deserialización del inventario

    class Inventario:
        def __init__(self):
            self.productos = {}

        def agregar_producto(self, producto):
            if producto.id in self.productos:
                print(f"El producto con ID {producto.id} ya existe en el inventario.")
            else:
                self.productos[producto.id] = producto
                print(f"Producto {producto.nombre} agregado al inventario.")

        def eliminar_producto(self, id):
            if id in self.productos:
                del self.productos[id]
                print(f"Producto con ID {id} eliminado del inventario.")
            else:
                print(f"No se encontró ningún producto con ID {id}.")

        def actualizar_producto(self, id, cantidad=None, precio=None):
            if id in self.productos:
                if cantidad is not None:
                    self.productos[id].actualizar_cantidad(cantidad)
                if precio is not None:
                    self.productos[id].actualizar_precio(precio)
                print(f"Producto con ID {id} actualizado.")
            else:
                print(f"No se encontró ningún producto con ID {id}.")

        def buscar_producto_por_nombre(self, nombre):
            encontrados = [producto for producto in self.productos.values() if
                           producto.nombre.lower() == nombre.lower()]
            if encontrados:
                for producto in encontrados:
                    print(producto)
            else:
                print(f"No se encontraron productos con el nombre {nombre}.")

        def mostrar_todos_los_productos(self):
            if self.productos:
                for producto in self.productos.values():
                    print(producto)
            else:
                print("El inventario está vacío.")

        def guardar_inventario(self, archivo):
            with open(archivo, 'wb') as f:
                pickle.dump(self.productos, f)
            print(f"Inventario guardado en {archivo}.")

        def cargar_inventario(self, archivo):
            try:
                with open(archivo, 'rb') as f:
                    self.productos = pickle.load(f)
                print(f"Inventario cargado desde {archivo}.")
            except FileNotFoundError:
                print(f"El archivo {archivo} no existe. Se creó un nuevo inventario vacío.")
                self.productos = {}

                def mostrar_menu():
                    print("\n--- Sistema de Gestión de Inventarios ---")
                    print("1. Agregar producto")
                    print("2. Eliminar producto")
                    print("3. Actualizar producto")
                    print("4. Buscar producto por nombre")
                    print("5. Mostrar todos los productos")
                    print("6. Guardar inventario en archivo")
                    print("7. Cargar inventario desde archivo")
                    print("8. Salir")

                def main():
                    inventario = Inventario()

                    while True:
                        mostrar_menu()
                        opcion = input("Selecciona una opción: ")

                        if opcion == "1":
                            id = input("Ingresa el ID del producto: ")
                            nombre = input("Ingresa el nombre del producto: ")
                            cantidad = int(input("Ingresa la cantidad del producto: "))
                            precio = float(input("Ingresa el precio del producto: "))
                            producto = Producto(id, nombre, cantidad, precio)
                            inventario.agregar_producto(producto)

                        elif opcion == "2":
                            id = input("Ingresa el ID del producto a eliminar: ")
                            inventario.eliminar_producto(id)

                        elif opcion == "3":
                            id = input("Ingresa el ID del producto a actualizar: ")
                            cantidad = input("Ingresa la nueva cantidad (o presiona Enter para no actualizar): ")
                            precio = input("Ingresa el nuevo precio (o presiona Enter para no actualizar): ")
                            inventario.actualizar_producto(id, cantidad=int(cantidad) if cantidad else None,
                                                           precio=float(precio) if precio else None)

                        elif opcion == "4":
                            nombre = input("Ingresa el nombre del producto a buscar: ")
                            inventario.buscar_producto_por_nombre(nombre)

                        elif opcion == "5":
                            inventario.mostrar_todos_los_productos()

                        elif opcion == "6":
                            archivo = input("Ingresa el nombre del archivo para guardar el inventario: ")
                            inventario.guardar_inventario(archivo)

                        elif opcion == "7":
                            archivo = input("Ingresa el nombre del archivo desde el cual cargar el inventario: ")
                            inventario.cargar_inventario(archivo)

                        elif opcion == "8":
                            print("Saliendo del sistema...")
                            break

                        else:
                            print("Opción no válida, por favor selecciona una opción del menú.")

                if __name__ == "__main__":
                    main()
                