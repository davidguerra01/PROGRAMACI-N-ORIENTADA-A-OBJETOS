import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entry.get()
    if info:
        listbox.insert(tk.END, info)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

# Función para limpiar la lista
def limpiar_lista():
    listbox.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Información")
ventana.geometry("400x300")

# Etiqueta para el campo de texto
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Campo de texto
entry = tk.Entry(ventana, width=40)
entry.pack(pady=10)

# Botón "Agregar"
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
btn_agregar.pack(pady=5)

# Botón "Limpiar"
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Lista para mostrar la información
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
