import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
#from NuevoClienteGUI import NuevoClienteGUI #Removed this line
#from GestorClientes import GestorClientes #Removed this line

class SeleccionarClienteGUI:
    def __init__(self, gestor_clientes, nuevo_cliente_gui):
        self.gestor_clientes = gestor_clientes
        self.nuevo_cliente_gui = nuevo_cliente_gui

        self.ventana = tk.Tk()
        self.ventana.title("Seleccionar Cliente")
        self.ventana.geometry("400x300")

        # Crear la lista de clientes
        self.lista_clientes = tk.Listbox(self.ventana, selectmode=tk.SINGLE)
        self.lista_clientes.pack(expand=True, fill=tk.BOTH)

        # Botón para seleccionar cliente
        self.seleccionar_button = tk.Button(self.ventana, text="Seleccionar Cliente", command=self.seleccionar_cliente)
        self.seleccionar_button.pack(pady=10)

        # Cargar los clientes en la lista
        self.cargar_clientes()

        self.ventana.mainloop()

    def cargar_clientes(self):
        self.lista_clientes.delete(0, tk.END)
        clientes = self.gestor_clientes.obtener_clientes()
        for cliente in clientes:
            self.lista_clientes.insert(tk.END, cliente.get_nombre())  # Mostrar solo el nombre del cliente #Modified this line

    def seleccionar_cliente(self):
        # Obtener el cliente seleccionado
        seleccion = self.lista_clientes.curselection()
        if seleccion:
            nombre_seleccionado = self.lista_clientes.get(seleccion[0])

            # Buscar el cliente en el gestor
            cliente_seleccionado = self.gestor_clientes.obtener_cliente_por_nombre(nombre_seleccionado)
            if cliente_seleccionado:
                # Cargar los datos del cliente en la GUI de edición
                self.nuevo_cliente_gui.cargar_cliente_para_edicion(cliente_seleccionado)
                self.ventana.destroy()  # Cerrar la ventana de selección

# Definición de la clase GestorClientes y NuevoClienteGUI (solo ejemplos)
