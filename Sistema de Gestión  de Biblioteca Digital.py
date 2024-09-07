class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, categoria={self.categoria}, isbn={self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, id_usuario={self.id_usuario}, libros_prestados={self.libros_prestados})"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado en la biblioteca.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja de la biblioteca.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario} en la biblioteca.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro {libro.titulo} prestado a {usuario.nombre}.")
            else:
                print(f"El libro {libro.titulo} ya está prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro {libro.titulo} devuelto por {usuario.nombre}.")
            else:
                print(f"El libro {libro.titulo} no está prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo in libro.titulo) or (autor and autor in libro.autor) or (categoria and categoria in libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Crimen y castigo", "Fiodor M. Dostoievski", "Novela Literaria", "1234567890")
libro2 = Libro("El señor de los anillos", "J.J.R Tolkien", "Fantasía", "0987654321")
libro3 = Libro("Un mundo feliz", "Aldous Huxley", "Ciencia ficción", "0984342351")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Carlos Sanchez", "001")
usuario2 = Usuario("Angelica Pozo", "002")
usuario3 = Usuario("Maria Caiza", "003")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.registrar_usuario(usuario3)

# Prestar y devolver libros
biblioteca.prestar_libro("001", "1234567890")
biblioteca.devolver_libro("002", "1234567890")
biblioteca.prestar_libro("003", "0984342351")

# Buscar libros
resultados = biblioteca.buscar_libro(titulo="Crimen y castigo")
print("Resultados de búsqueda:", resultados)

# Listar libros prestados
prestados = biblioteca.listar_libros_prestados("002")
print("Libros prestados a Carlos Sanchez 1:", prestados)
print("Libros prestados a Maria Caiza 1:", prestados)