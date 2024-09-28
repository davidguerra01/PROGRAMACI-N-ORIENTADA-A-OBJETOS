import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista para almacenar las tareas
        self.tasks = []

        # Entrada de texto para nuevas tareas
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir una nueva tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind("<Double-Button-1>", self.mark_completed)

        # Botón para marcar la tarea seleccionada como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar la tarea seleccionada
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    # Función para añadir tareas
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    # Función para marcar una tarea como completada
    def mark_completed(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{task} (Completada)"
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"{task} (Completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    # Función para eliminar una tarea
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
