import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")
root.geometry("400x400")

# Lista para almacenar tareas
tareas = []

# Función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingresa una tarea.")

# Función para marcar una tarea como completada
def completar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        if not tarea.startswith("[Completada]"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "[Completada] " + tarea)
    except IndexError:
        messagebox.showwarning("Selección", "Por favor selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def eliminar_tarea(event=None):
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Selección", "Por favor selecciona una tarea para eliminar.")

# Función para cerrar la aplicación con la tecla Escape
def cerrar_app(event=None):
    root.quit()

# Crear el campo de entrada para las tareas
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)

# Crear el botón para añadir tareas
boton_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Crear la lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Crear los botones para completar y eliminar tareas
boton_completar = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Asignar atajos de teclado
root.bind('<Return>', agregar_tarea)      # Enter para añadir tarea
root.bind('<c>', completar_tarea)         # C para completar tarea
root.bind('<d>', eliminar_tarea)          # D para eliminar tarea
root.bind('<Delete>', eliminar_tarea)     # Supr para eliminar tarea
root.bind('<Escape>', cerrar_app)         # Esc para cerrar la aplicación

# Iniciar la aplicación
root.mainloop()
