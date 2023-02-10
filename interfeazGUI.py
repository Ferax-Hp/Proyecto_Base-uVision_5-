import tkinter
from tkinter import filedialog
from tkinter import messagebox

import customtkinter as ctk
import RenombrarProyecto as rp

class ventana(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.path = "C:/"

        self.title('Crear Proyecto')
        # self.resizable(False, False)
        self.geometry('300x500')

        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Obtener las dimensiones de la ventana
        window_width = 300
        window_height = 500

        # Calcular la posición x e y para que la ventana se abra en el centro
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        # Configurar la posición de la ventana
        self.geometry("+%d+%d" % (x_coordinate, y_coordinate))

        self.label = ctk.CTkLabel(self, text="¿Donde Desea Crear el Proyecto?")
        self.boton = ctk.CTkButton(self, text="Crear", width=window_width, command=self.generar)
        self.botonPath = ctk.CTkButton(self, text="folder", command=self.solicitar_directorio, width=int(window_width/3))
        self.textPath = ctk.CTkEntry(self,  width=int(window_width/3)*2)
        self.textPath.insert(0, self.path)
        self.nombreProyecto = ctk.CTkEntry(self, width=window_width)
        self.nombreProyecto.insert(0, "Nombre_Proyecto")

        self.label.grid(row=0, column=0, columnspan="3", pady=10, sticky="ns")
        self.nombreProyecto.grid(row=1, column=0, columnspan="3", pady=10, sticky="nswe")
        self.botonPath.grid(row=2, column=2, pady=10)
        self.textPath.grid(row=2, column=0, columnspan="2", pady=10, sticky="nswe")
        self.boton.grid(row=3, column=0, columnspan="3", pady=10, sticky="nswe")

    def solicitar_directorio(self):
        self.path = filedialog.askdirectory()
        if self.path != "":
            self.textPath.delete(0, 'end')
            self.textPath.insert(0, self.path)

    def generar(self):
        rp.extraer(self.path)
        rp.modificacion_de_archivos(path=self.textPath.get(), nombre_proyecto=self.nombreProyecto.get())
        messagebox.showinfo("Proyecto Creado", "Proyecto Creado")
        self.destroy()