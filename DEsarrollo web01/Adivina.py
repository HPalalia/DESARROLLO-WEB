import random
import tkinter as tk
from tkinter import messagebox

# Generar número secreto
numero_secreto = random.randint(1, 10)
intentos = 0

# Crear función para verificar la adivinanza
def verificar_adivinanza():
    global intentos
    try:
        adivinanza = int(caja_entrada.get())
        intentos += 1

        if adivinanza < numero_secreto:
            etiqueta_resultado.config(text="Demasiado bajo.")
        elif adivinanza > numero_secreto:
            etiqueta_resultado.config(text="Demasiado alto.")
        else:
            etiqueta_resultado.config(text=f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            # Mostrar cuadro de diálogo de felicitaciones
            messagebox.showinfo("¡Felicidades!", f"¡Correcto! Lo adivinaste en {intentos} intentos.")
    except ValueError:
        etiqueta_resultado.config(text="Introduce un número válido.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Juego de Adivinanza")

# Etiqueta de instrucciones
etiqueta_instrucciones = tk.Label(ventana, text="Adivina el número entre 1 y 10")
etiqueta_instrucciones.pack()

# Cuadro de entrada para el número
caja_entrada = tk.Entry(ventana)
caja_entrada.pack()

# Botón para verificar la adivinanza
boton_verificar = tk.Button(ventana, text="Adivinar", command=verificar_adivinanza)
boton_verificar.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
