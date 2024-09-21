import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")

        # Treeview para mostrar los eventos
        self.columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(root, columns=self.columns, show='headings')
        for col in self.columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        # DatePicker usando datetime
        self.fecha_var = tk.StringVar()
        self.fecha_entry = tk.Entry(root, textvariable=self.fecha_var)
        self.fecha_btn = tk.Button(root, text="Seleccionar Fecha", command=self.seleccionar_fecha)
        # ... (grid o pack los elementos)

        # Otros campos de entrada
        self.hora_entry = tk.Entry(root)
        self.descripcion_entry = tk.Entry(root)

        # Botones
        self.agregar_btn = tk.Button(root, text="Agregar Evento", command=self.agregar_evento)
        self.eliminar_btn = tk.Button(root, text="Eliminar Evento", command=self.eliminar_evento)
        self.salir_btn = tk.Button(root, text="Salir", command=root.quit)
        # ... (grid o pack los botones)

    def seleccionar_fecha(self):
        fecha = tk.simpledialog.askstring("Seleccionar Fecha", "Ingrese la fecha (AAAA-MM-DD):")
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            self.fecha_var.set(fecha)
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use AAAA-MM-DD")

    def agregar_evento(self):
        fecha = self.fecha_var.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación básica
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))

    def eliminar_evento(self):
        item = self.tree.selection()[0]
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

