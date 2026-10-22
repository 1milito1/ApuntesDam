import tkinter as tk
from tkinter import messagebox
from Cliente import Cliente

class NuevoClienteGUI:
    def __init__(self, gestor_clientes, factura_gui):
        self.gestor_clientes = gestor_clientes
        self.factura_gui = factura_gui
        self.cliente_seleccionado = None  # Cliente seleccionado para editar

        # Crear ventana
        self.ventana = tk.Toplevel() #Changed tk.Tk() for tk.Toplevel()
        self.ventana.title("Nuevo Cliente")
        self.ventana.geometry("700x700")
        self.ventana.config(bg="#f4f4f4")  # Fondo más suave

        # Crear el marco principal
        main_frame = tk.Frame(self.ventana, bg="#f4f4f4")
        main_frame.pack(padx=20, pady=20)

        # Etiqueta principal
        titulo_label = tk.Label(main_frame, text="Gestión de Clientes", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#4CAF50")
        titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Panel de campos de texto
        self.nombre_field = self.create_text_field(main_frame, "Nombre:", 1)
        self.nif_field = self.create_text_field(main_frame, "NIF:", 2)
        self.direccion_field = self.create_text_field(main_frame, "Dirección:", 3)
        self.tlf_field = self.create_text_field(main_frame, "Población:", 4)

        # Botones
        guardar_button = self.create_button(main_frame, "Guardar Cliente", self.guardar_cliente, 5, 0)
        editar_button = self.create_button1(main_frame, "Editar Cliente", self.editar_cliente, 5, 1)
        eliminar_button = self.create_button2(main_frame, "Eliminar Cliente", self.eliminar_cliente, 5, 2)

        #self.ventana.mainloop() #Removed this line

    def create_text_field(self, parent, label_text, row):
        label = tk.Label(parent, text=label_text, font=("Arial", 12), bg="#f4f4f4", anchor="w")
        label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
        text_field = tk.Entry(parent, font=("Arial", 12))
        text_field.grid(row=row, column=1, padx=10, pady=10)
        return text_field

    def create_button(self, parent, text, command, row, column):
        button = tk.Button(parent, text=text, command=command, font=("Arial", 12, "bold"), 
                           bg="green", fg="white", relief="raised", bd=3, width=15)
        button.config(activebackground="green", activeforeground="white")
        button.grid(row=row, column=column, padx=10, pady=10)
        return button
    def create_button1(self, parent, text, command, row, column):
        button = tk.Button(parent, text=text, command=command, font=("Arial", 12, "bold"), 
                           bg="blue", fg="white", relief="raised", bd=3, width=15)
        button.config(activebackground="blue", activeforeground="white")
        button.grid(row=row, column=column, padx=10, pady=10)
        return button
    def create_button2(self, parent, text, command, row, column):
        button = tk.Button(parent, text=text, command=command, font=("Arial", 12, "bold"), 
                           bg="red", fg="white", relief="raised", bd=3, width=15)
        button.config(activebackground="red", activeforeground="white")
        button.grid(row=row, column=column, padx=10, pady=10)
        return button

    def eliminar_cliente(self):
        nombre = self.nombre_field.get()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del cliente a eliminar.", parent=self.ventana) #Added parent=self.ventana
            return

        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar al cliente?",parent = self.ventana) # Added parent = self.ventana
        if confirm:
            self.gestor_clientes.eliminar_cliente(nombre)
            self.limpiar_campos()
            self.factura_gui.cargar_clientes() #Added this line

    def guardar_cliente(self):
        nombre = self.nombre_field.get()
        nif = self.nif_field.get()
        direccion = self.direccion_field.get()
        telefono = self.tlf_field.get()

        # Validación de campos
        if not nombre or not nif or not direccion or not telefono:
            messagebox.showerror("Error", "Todos los campos deben ser completados.",parent = self.ventana) # Added parent = self.ventana
            return

        # Crear o actualizar el cliente
        if self.cliente_seleccionado:
            self.cliente_seleccionado.set_nombre(nombre)
            self.cliente_seleccionado.set_nif(nif)
            self.cliente_seleccionado.set_direccion(direccion)
            self.cliente_seleccionado.set_telefono(telefono)
            self.gestor_clientes.actualizar_cliente(self.cliente_seleccionado)  # Actualizar cliente
        else:
            nuevo_cliente = Cliente(nombre, nif, direccion, telefono)
            self.gestor_clientes.agregar_cliente(nuevo_cliente)  # Agregar nuevo cliente

        # Limpiar los campos después de guardar
        self.limpiar_campos()
        self.factura_gui.cargar_clientes()

    def limpiar_campos(self):
        self.nombre_field.delete(0, tk.END)
        self.nif_field.delete(0, tk.END)
        self.direccion_field.delete(0, tk.END)
        self.tlf_field.delete(0, tk.END)
        self.cliente_seleccionado = None

    def editar_cliente(self):
        # Crear y mostrar la ventana para elegir el cliente a editar
        from SeleccionarClienteGUI import SeleccionarClienteGUI
        SeleccionarClienteGUI(self.gestor_clientes, self)

    def cargar_cliente_para_edicion(self, cliente):
        self.cliente_seleccionado = cliente
        self.nombre_field.insert(0, cliente.get_nombre())
        self.nif_field.insert(0, cliente.get_nif())
        self.direccion_field.insert(0, cliente.get_direccion())
        self.tlf_field.insert(0, cliente.get_telefono())
