import tkinter as tk
from tkinter import ttk
from tkinter import *

def operacion():

    seleccion = lista.get()
    opcion1 = float(numero1.get())
    opcion2 = float(numero2.get())

    if seleccion == "Suma":
        resultado_suma = opcion1 + opcion2
        resultado = tk.Label(ventana, text=f"Resultado: {resultado_suma}", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
        resultado.pack()
        ventana.after(5000, resultado.destroy)
    elif seleccion == "Resta":
        resultado_resta = opcion1 - opcion2
        resultado = tk.Label(ventana, text=f"Resultado: {resultado_resta}", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
        resultado.pack()
        ventana.after(5000, resultado.destroy)
    elif seleccion == "Multiplicación":
        resultado_multiplicacion = opcion1 * opcion2
        resultado = tk.Label(ventana, text=f"Resultado: {resultado_multiplicacion}", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
        resultado.pack()
        ventana.after(5000, resultado.destroy)
    elif seleccion == "División":
        if opcion2 == 0:
            resultado = tk.Label(ventana, text="No es posible división entre 0", fg="black", font=("Arial", 16), width=100, height=2, anchor="center")
            resultado.pack()
            ventana.after(5000, resultado.destroy)
        else:
            resultado_division = opcion1 / opcion2
            resultado = tk.Label(ventana, text=f"Resultado: {resultado_division}", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
            resultado.pack()
            ventana.after(5000, resultado.destroy)
    else:
        print("Opción no valida")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(0,0)

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 500
alto_ventana = 400
posicion_x = (ancho_pantalla - ancho_ventana) // 2 
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

hola = tk.Label(ventana, text="¡Hola, mundo!", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
hola.pack()

instruccion = tk.Label(ventana, text="Selecciona la operacion que deseas realizar:", fg="black", font=("Arial", 16), width=100, height=2, anchor="center")
instruccion.pack()

lista = ttk.Combobox(state="readonly", values=["Suma", "Resta", "Multiplicación", "División"])
lista.pack()

texto_numero1 = tk.Label(ventana, text="Número 1:", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
texto_numero1.pack()

numero1 = tk.Entry(ventana, width=30)
numero1.pack()

texto_numero2 = tk.Label(ventana, text="Número 2:", fg="black", font=("Arial", 16), width=20, height=2, anchor="center")
texto_numero2.pack()

numero2 = tk.Entry(ventana, width=30)
numero2.pack()

boton_calcular = tk.Button(text="Calcular", command=operacion, font=("Arial", 16))
boton_calcular.pack(pady=10)

ventana.mainloop()