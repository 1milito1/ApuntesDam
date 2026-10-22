import time
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Image
from reportlab.lib.units import inch
import os
from datetime import datetime
import subprocess  # Import the subprocess module


class FacturaPDF:
    def __init__(self, cliente, numero_factura, conceptos, cantidad, precio, main_window):
        self.cliente = cliente
        self.numero_factura = numero_factura
        self.conceptos = conceptos
        self.cantidad = cantidad
        self.precio = precio
        self.fecha_factura = datetime.now().strftime("%d/%m/%Y")
        self.main_window = main_window # This line has been added

    def generar_factura(self):
        # --- Get the Desktop directory ---
        user_home = os.path.expanduser("~")
        desktop_path = os.path.join(user_home, "Desktop")
        facturas_dir = os.path.join(desktop_path, "Facturas")

        if not os.path.exists(facturas_dir):
            os.makedirs(facturas_dir)

        nombre_archivo = os.path.join(facturas_dir, f"{self.cliente.get_nombre().replace(' ', '_')}_{self.numero_factura}.pdf")

        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        styles = getSampleStyleSheet()

        # --- Header Section ---

        # Company information styling
        company_style = ParagraphStyle(
            "companyInfo",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=colors.black,
        )

        company_name = "TRANSPORTES DOMINGUEZ"
        company_owner = "José Domínguez Garlito"
        company_address = "Carretera Trujillo s/n, Plasencia (Cáceres)"
        company_tel = "Tel: 927 41 60 79 / 656 637 708"
        company_nif = "NIF: 11789786-Z"

        # Client information styling
        client_style = ParagraphStyle(
            "clientInfo",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=colors.black,
        )

        client_name = self.cliente.get_nombre().upper()
        client_address = f"{self.cliente.get_direccion().title()}"
        client_phone = f"{self.cliente.get_telefono().title()}"
        client_nif = f"{self.cliente.get_nif()}"

        # Invoice information styling
        invoice_style = ParagraphStyle(
            "invoiceInfo",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=colors.black,
        )

        invoice_number = f"Factura: {self.numero_factura}"
        invoice_date = f"Fecha: {self.fecha_factura}"

        # ---Logo---
        try:
            # Get the directory of the script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the absolute path to logo.png
            logo_path = os.path.join(script_dir, "logo.png")
            if os.path.exists(logo_path):
                logo = Image(logo_path, width=1.5 * inch, height=1.5 * inch)
                logo.hAlign = "RIGHT"
                logo.drawOn(c, 450, 670)
            else:
                print(f"Logo not found at: {logo_path}")  # Added this line to notify that the logo has not been found
        except Exception as e:
            print(f"Error loading logo: {e}")
        # Draw the headers
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 750, company_name)
        c.setFont("Helvetica", 10)
        c.drawString(50, 735, company_owner)
        c.drawString(50, 720, company_address)
        c.drawString(50, 705, company_tel)
        c.drawString(50, 690, company_nif)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 650, invoice_number)
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 10)
        c.drawString(50, 635, invoice_date)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(400, 650, client_name)
        c.setFont("Helvetica", 10)
        c.drawString(400, 635, client_address)
        c.drawString(400, 620, client_phone)
        c.drawString(400, 605, client_nif)

        # --- Table of Concepts ---
        # Added margin between headers and table
        y_position = 580  # Change this position to create space between the header and the table
        y_position -= 50
        table_header_color = colors.lightgrey
        header_text_color = colors.black
        table_data_color = colors.white
        table_line_color = colors.black

        # Table Header
        c.setFillColor(table_header_color)
        c.setStrokeColor(table_line_color)
        c.rect(50, y_position, 500, 20, fill=1)
        c.line(50, y_position, 550, y_position)  # Add the line under the header

        c.setFillColor(header_text_color)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(60, y_position + 7, "Cantidad")
        c.drawString(150, y_position + 7, "Descripción")
        c.drawString(300, y_position + 7, "Precio Unitario")
        c.drawString(450, y_position + 7, "Total")

        y_position -= 20
        total_base_imponible = 0
        total_iva = 0
        c.setFont("Helvetica", 10)

        # Add table rows
        max_rows = 10
        for i in range(max_rows):
            if i < len(self.conceptos):
                concepto = self.conceptos[i]
                cantidad_int = concepto.get_cantidad()
                precio_unitario = concepto.get_precio()
                base_imponible = precio_unitario * cantidad_int
                iva = base_imponible * 0.21
                total = base_imponible + iva

                # Table Data background
                c.setFillColor(table_data_color)
                c.rect(50, y_position, 500, 20, fill=1, stroke=1)  # Added stroke=1 to have border
                # Add vertical lines
                c.line(140, y_position, 140, y_position + 20)
                c.line(290, y_position, 290, y_position + 20)
                c.line(440, y_position, 440, y_position + 20)

                # Table Data text
                c.setFillColor(colors.black)
                c.drawString(60, y_position + 7, str(cantidad_int))
                c.drawString(150, y_position + 7, concepto.get_descripcion().upper())
                c.drawString(300, y_position + 7, f"{precio_unitario:.2f} €")
                c.drawString(450, y_position + 7, f"{total:.2f} €")

                total_base_imponible += base_imponible
                total_iva += iva
            else:
                # Add empty row
                c.setFillColor(table_data_color)
                c.rect(50, y_position, 500, 20, fill=1, stroke=1)
                # Add vertical lines
                c.line(140, y_position, 140, y_position + 20)
                c.line(290, y_position, 290, y_position + 20)
                c.line(440, y_position, 440, y_position + 20)

            y_position -= 20

        # Table Totals
        # Remove last line
        # c.line(50, y_position, 550, y_position) #Removed this line

        # Totalizar factura
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 12)  # Set to normal font first
        total_x_position = 390  # Change this position to change the position of the total text to the left

        # Added margin between table and totals
        y_position -= 50  # Change this position to create space between the table and the totals

        c.drawString(
            total_x_position, y_position - 30, f"Total Base Imponible: {total_base_imponible:.2f} €"
        )
        c.drawString(total_x_position, y_position - 45, f"Total IVA (21%): {total_iva:.2f} €")

        y_position -= 20
        # Make only "Total Factura" bold
        c.setFont("Helvetica-Bold", 18)
        c.drawString(
            total_x_position,
            y_position - 60,
            f"Total Factura: {total_base_imponible + total_iva:.2f} €",
        )
        c.save()
        #print(f"Factura generada: {nombre_archivo}")

        self.mostrar_mensaje_confirmacion(nombre_archivo)

    def mostrar_mensaje_confirmacion(self, nombre_archivo):
        """Shows a message box with options to open or close the PDF."""
        from tkinter import messagebox  # Import messagebox here

        response = messagebox.askyesnocancel(
            "Factura Generada",
            "Factura generada correctamente. ¿Desea abrir el archivo?",
            default=messagebox.YES,
            icon="info",
            parent=self.main_window # this line has been added
        )

        if response is True:  # User clicked "Yes"
            self.abrir_pdf(nombre_archivo)
        elif response is False: # User clicked "No" or close window
          pass  # Do nothing, just close the message box

    def abrir_pdf(self, nombre_archivo):
        """Opens the generated PDF file using the default PDF viewer."""
        try:
            if os.name == "nt":  # Windows
                os.startfile(nombre_archivo)
            elif os.name == "posix":  # macOS or Linux
                try:
                    subprocess.run(["open", nombre_archivo], check=True)  # For macOS
                except subprocess.CalledProcessError as e:
                    print(f"Error al abrir el PDF en macOS: {e}")
                    try:
                        subprocess.run(["xdg-open", nombre_archivo], check=True)  # For linux
                    except subprocess.CalledProcessError as e:
                        print(f"Error al abrir el PDF en linux: {e}")
            else:
                print("Sistema operativo no soportado para abrir PDF automáticamente.")
        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error inesperado al intentar abrir el PDF: {e}")

