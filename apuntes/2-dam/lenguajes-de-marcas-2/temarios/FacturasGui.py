import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import Image, ImageTk
import os  # Import the 'os' module
import sys

from FacturaPDF import FacturaPDF
from NuevoClienteGUI import NuevoClienteGUI
from GestorClientes import GestorClientes
from Concepto import Concepto


class FacturaGUI:
    ARCHIVO_ULTIMO_NUMERO = "ultimo_numero_factura.txt"

    def __init__(self, gestor_clientes):
        self.gestor_clientes = gestor_clientes
        self.conceptos = []

        self.ventana = tk.Tk()
        self.ventana.title("Generador de Facturas")
        self.ventana.geometry("800x800")
        self.ventana.configure(bg="#f0f0f0")
        
        #icono ventana 

        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio del script
        icon_path = os.path.join(script_dir, "logo.png")

        if not os.path.exists(icon_path):
            print(f"Error: El archivo {icon_path} no existe.")  # Depuración

        # Cargar icono
        icon_image = Image.open(icon_path)
        icon_tk = ImageTk.PhotoImage(icon_image)
        
        # Establecer icono
        self.ventana.iconphoto(True, icon_tk)
        

        # --- Estilos ---
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))

        # Modified button styles for better visibility
        self.style.configure(
            "TButton",
            background="#0078d7",
            foreground="white",  # Changed to white
            font=("Helvetica", 10, "bold"),
            padding=10,
        )  # Blue button
        self.style.map("TButton", background=[("active", "#005ba1"), ])  # Darker blue on hover

        self.style.configure(
            "Red.TButton",
            background="#d9534f",
            foreground="white",  # Changed to white
            font=("Helvetica", 10, "bold"),
            padding=10,
        )  # Red button
        self.style.map("Red.TButton", background=[("active", "#c9302c")])

        self.style.configure(
            "Green.TButton",
            background="#5cb85c",
            foreground="white",  # Changed to white
            font=("Helvetica", 10, "bold"),
            padding=10,
        )  # Green button
        self.style.map("Green.TButton", background=[("active", "#4cae4c")])

        self.style.configure("TEntry", padding=5)
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("Vertical.TScrollbar", background="#cccccc", arrowcolor="#444444")

        # --- Logo (Load from Absolute Path) ---
        try:
            # Get the directory of the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the absolute path to logo.png
            logo_path = os.path.join(script_dir, "logo.png")

            self.logo_image = Image.open(logo_path)  # Load the logo from its absolute path
            self.logo_image = self.logo_image.resize((150, 150), Image.LANCZOS)
            self.logo_tk = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(self.ventana, image=self.logo_tk, bg="#f0f0f0")
            self.logo_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)
        except FileNotFoundError:
            self.logo_label = tk.Label(
                self.ventana, text="Logo no encontrado", bg="#f0f0f0", font=("Helvetica", 12, "bold")
            )
            self.logo_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        # --- Panel de datos de factura ---
        self.datos_frame = ttk.Frame(self.ventana, padding=10, borderwidth=2, relief="groove")
        self.datos_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.factura_num_label = ttk.Label(self.datos_frame, text="Número de Factura:")
        self.factura_num_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.factura_num_field = ttk.Entry(self.datos_frame)
        self.factura_num_field.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.cliente_label = ttk.Label(self.datos_frame, text="Cliente:")
        self.cliente_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.cliente_combobox = tk.StringVar()
        self.cliente_combobox.set("Seleccionar Cliente")

        # Create the OptionMenu
        self.cliente_menu = ttk.OptionMenu(
            self.datos_frame, self.cliente_combobox, "Seleccionar Cliente"
        )
        self.cliente_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        # Then, call cargar_clientes
        self.cargar_clientes()

        self.cantidad_label = ttk.Label(self.datos_frame, text="Cantidad:")
        self.cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.cantidad_field = ttk.Entry(self.datos_frame)
        self.cantidad_field.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.concepto_label = ttk.Label(self.datos_frame, text="Concepto:")
        self.concepto_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.concepto_field = ttk.Entry(self.datos_frame)
        self.concepto_field.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.precio_label = ttk.Label(self.datos_frame, text="Precio:")
        self.precio_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.precio_field = ttk.Entry(self.datos_frame)
        self.precio_field.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.ultimo_numero_factura_label = ttk.Label(
            self.datos_frame, text="Último número de factura:"
        )
        self.ultimo_numero_factura_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        # --- Load and Set Last Factura Number ---
        self.cargar_ultimo_numero_factura()

        # --- Panel para la fecha ---
        self.fecha_frame = ttk.Frame(self.ventana, padding=10, borderwidth=2, relief="groove")
        self.fecha_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        self.fecha_label = ttk.Label(self.fecha_frame, text="Fecha:")
        self.fecha_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.fecha_field = ttk.Entry(self.fecha_frame)
        self.fecha_field.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.fecha_button = ttk.Button(self.fecha_frame, text="Fecha Actual", command=self.set_fecha_actual)
        self.fecha_button.grid(row=0, column=2, padx=5, pady=5)

        # --- Lista de conceptos ---
        self.lista_conceptos_label = ttk.Label(self.ventana, text="Conceptos añadidos:")
        self.lista_conceptos_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.lista_conceptos_frame = ttk.Frame(self.ventana)
        self.lista_conceptos_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        self.lista_conceptos_scrollbar = ttk.Scrollbar(self.lista_conceptos_frame, orient="vertical")
        self.lista_conceptos_scrollbar.pack(side="right", fill="y")

        self.lista_conceptos = tk.Listbox(
            self.lista_conceptos_frame,
            height=8,
            yscrollcommand=self.lista_conceptos_scrollbar.set,
            selectbackground="#b0e0e6",
        )
        self.lista_conceptos.pack(side="left", fill="both", expand=True)

        self.lista_conceptos_scrollbar.config(command=self.lista_conceptos.yview)

        # --- Panel de botones ---
        self.botones_frame = ttk.Frame(self.ventana, padding=10)
        self.botones_frame.grid(row=5, column=0, pady=10, sticky="nsew")

        # --- Botones ---
        self.agregar_concepto_button = ttk.Button(
            self.botones_frame, text="Añadir Concepto", command=self.agregar_concepto, style="TButton"
        )
        self.agregar_concepto_button.grid(row=0, column=0, padx=10, pady=5)

        self.eliminar_concepto_button = ttk.Button(
            self.botones_frame,
            text="Eliminar Concepto",
            command=self.eliminar_concepto,
            style="Red.TButton",
        )
        self.eliminar_concepto_button.grid(row=0, column=1, padx=10, pady=5)

        self.guardar_factura_button = ttk.Button(
            self.botones_frame, text="Guardar Factura", command=self.guardar_factura, style="Green.TButton"
        )
        self.guardar_factura_button.grid(row=0, column=2, padx=10, pady=5)

        self.nuevo_cliente_button = ttk.Button(
            self.botones_frame, text="Nuevo Cliente", command=self.nuevo_cliente, style="TButton"
        )
        self.nuevo_cliente_button.grid(row=0, column=3, padx=10, pady=5)

        # --- Configuración de pesos para redimensionar ---
        self.ventana.grid_rowconfigure(4, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.datos_frame.grid_columnconfigure(1, weight=1)
        self.fecha_frame.grid_columnconfigure(1, weight=1)
        self.botones_frame.grid_columnconfigure(0, weight=1)
        self.botones_frame.grid_columnconfigure(1, weight=1)
        self.botones_frame.grid_columnconfigure(2, weight=1)
        self.botones_frame.grid_columnconfigure(3, weight=1)

        self.ventana.mainloop()

    def cargar_clientes(self):
        clientes_nombres = self.gestor_clientes.obtener_clientes()
        self.cliente_menu['menu'].delete(0, 'end')
        for cliente in clientes_nombres:
            self.cliente_menu['menu'].add_command(
                label=cliente.get_nombre(), command=tk._setit(self.cliente_combobox, cliente.get_nombre())
            )

    def set_fecha_actual(self):
        self.fecha_field.delete(0, tk.END)
        self.fecha_field.insert(0, datetime.now().strftime("%d/%m/%Y"))

    def agregar_concepto(self):
        cantidad = self.cantidad_field.get()
        concepto = self.concepto_field.get()
        precio = self.precio_field.get()

        if cantidad and concepto and precio:
            try:
                cantidad = int(cantidad)
                precio = float(precio)
                nuevo_concepto = Concepto(cantidad, concepto, precio)
                self.conceptos.append(nuevo_concepto)
                self.actualizar_lista_conceptos()
                self.limpiar_campos()
            except ValueError:
                messagebox.showerror("Error", "Cantidad y precio deben ser numéricos.")
        else:
            messagebox.showwarning("Advertencia", "Debe rellenar todos los campos.")

    def eliminar_concepto(self):
        selected_index = self.lista_conceptos.curselection()
        if selected_index:
            self.conceptos.pop(selected_index[0])
            self.actualizar_lista_conceptos()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un concepto para eliminar.")

    def actualizar_lista_conceptos(self):
        self.lista_conceptos.delete(0, tk.END)
        for concepto in self.conceptos:
            self.lista_conceptos.insert(
                tk.END, f"{concepto.get_cantidad()} x {concepto.get_descripcion()} - {concepto.get_precio()}€"
            )

    def limpiar_campos(self):
        self.cantidad_field.delete(0, tk.END)
        self.concepto_field.delete(0, tk.END)
        self.precio_field.delete(0, tk.END)

    def guardar_factura(self):
        numero_factura = self.factura_num_field.get().strip()
        if not numero_factura or not self.conceptos:
            messagebox.showwarning(
                "Advertencia", "Debe ingresar un número de factura y al menos un concepto."
            )
            return

        try:
            numero_factura = int(numero_factura)
            cliente_nombre = self.cliente_combobox.get()
            cliente = self.gestor_clientes.obtener_cliente_por_nombre(cliente_nombre)
            if not cliente:
                messagebox.showwarning("Advertencia", "Cliente no encontrado.")
                return

            factura_pdf = FacturaPDF(
                cliente,
                numero_factura,
                self.conceptos,
                self.cantidad_field.get(),
                self.precio_field.get(),
                self.ventana  # <--- Added self.ventana here
            )
            factura_pdf.generar_factura()

            # --- Update and Save Last Factura Number ---
            self.actualizar_ultimo_numero_factura(numero_factura)

            self.limpiar_campos()
            self.conceptos.clear()
            self.actualizar_lista_conceptos()
        except ValueError:
            messagebox.showerror("Error", "Número de factura inválido.")

    def nuevo_cliente(self):
        NuevoClienteGUI(self.gestor_clientes, self)
        self.cargar_clientes()  # Added this line

    def cargar_ultimo_numero_factura(self):
        try:
            if os.path.exists(self.ARCHIVO_ULTIMO_NUMERO):
                with open(self.ARCHIVO_ULTIMO_NUMERO, "r") as f:
                    ultimo_numero = int(f.read().strip())
                    self.factura_num_field.insert(0, str(ultimo_numero + 1))
                    self.ultimo_numero_factura_label.config(
                        text=f"Último número de factura: {ultimo_numero}"
                    )
            else:
                self.factura_num_field.insert(0, "1")
                self.ultimo_numero_factura_label.config(text="Último número de factura: 0")
        except (ValueError, FileNotFoundError):
            self.factura_num_field.delete(0, tk.END)
            self.factura_num_field.insert(0, "1")
            self.ultimo_numero_factura_label.config(text="Último número de factura: Error al cargar")

    def actualizar_ultimo_numero_factura(self, numero):
        try:
            with open(self.ARCHIVO_ULTIMO_NUMERO, "w") as f:
                f.write(str(numero))
            self.ultimo_numero_factura_label.config(
                text=f"Último número de factura: {numero}"
            )
            self.factura_num_field.delete(0, tk.END)
            self.factura_num_field.insert(0, str(numero + 1))

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el último número de factura: {e}")

   


gestor_clientes = GestorClientes()
FacturaGUI(gestor_clientes)
