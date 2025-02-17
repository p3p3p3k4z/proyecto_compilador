from tkinter import *

class Boton:
    def __init__(self, master, text="Botón", command=None):
        # Crear el botón y almacenar su estado inicial como deshabilitado
        self.boton = Button(master, text=text, command=command)
        self.estado = 0  # 0 para deshabilitado, 1 para habilitado
        
        # Establecer color de fondo original (puedes cambiarlo según desees)
        self.bg_color_original = self.boton.cget("bg")

        # Asociar los eventos para el sombreado
        self.boton.bind("<Enter>", self.sombrear)  # Al pasar el mouse por encima
        self.boton.bind("<Leave>", self.restaurar_color)  # Al salir el mouse del botón

    def __str__(self):
        # Mostrar el estado del botón en la consola como 1 o 0
        return f"Botón '{self.boton.cget('text')}' - Estado: {self.estado}"

    def mostrar(self, x, y):
        # Colocar el botón en la posición (x, y)
        self.boton.grid(row=x, column=y, sticky="nsew", padx=5, pady=5)

    def habilitar(self):
        # Habilitar el botón y establecer estado en 1
        self.boton.config(state=NORMAL)
        self.estado = 1
        print(self)  # Mostrar el estado del botón en la consola

    def deshabilitar(self):
        # Deshabilitar el botón y establecer estado en 0
        self.boton.config(state=DISABLED)
        self.estado = 0
        print(self)  # Mostrar el estado del botón en la consola

    def obtener_estado(self):
        # Devolver el estado del botón como 1 o 0
        return self.estado

    def cambiar_texto(self, nuevo_texto):
        # Cambiar el texto del botón
        self.boton.config(text=nuevo_texto)

    def cambiar_colores(self, bg_color=None, fg_color=None):
        # Cambiar los colores de fondo y texto del botón
        if bg_color:
            self.boton.config(bg=bg_color)
        if fg_color:
            self.boton.config(fg=fg_color)

    def cambiar_tamano(self, ancho, alto):
        # Cambiar el tamaño del botón
        self.boton.config(width=ancho, height=alto)

    def cambiar_fuente(self, tipo_fuente="Helvetica", tamaño=12, negrita=False, cursiva=False):
        # Cambiar la fuente del botón
        fuente = (tipo_fuente, tamaño)
        if negrita:
            fuente = (fuente[0], fuente[1], "bold")
        if cursiva:
            fuente = (fuente[0], fuente[1], "italic")
        self.boton.config(font=fuente)
        
    def aumentar_tamano(self, aumento_x, aumento_y):
        # Aumentar el tamaño del botón
        ancho_actual = self.boton.winfo_width()
        alto_actual = self.boton.winfo_height()
        self.boton.config(width=ancho_actual + aumento_x, height=alto_actual + aumento_y)

    def sombrear(self, event):
        # Cambiar el color de fondo cuando el mouse pasa por encima
        self.boton.config(bg="lightgray")  # Puedes cambiar este color a tu gusto

    def restaurar_color(self, event):
        # Restaurar el color original cuando el mouse sale del botón
        self.boton.config(bg=self.bg_color_original)  # Restaurar el color original

