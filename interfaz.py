import tkinter as tk
from tkinter import filedialog, messagebox
import os
from main import procesar_automata_letras

# Función para seleccionar el archivo
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo", 
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        archivo_seleccionado.set(archivo)

# Función para procesar el archivo y mostrar ocurrencias
def procesar_archivo():
    archivo = archivo_seleccionado.get()
    if not archivo:
        messagebox.showerror("Error", "Por favor selecciona un archivo.")
        return
    
    resultado.delete("1.0", tk.END)  # Limpiar la caja de texto
    ocurrencias = []
    
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            for i, linea in enumerate(lineas, start=1):
                linea_lower = linea.lower()  # Convertir la línea a minúsculas
                procesar_automata_letras(linea_lower, i, ocurrencias)
        
        if ocurrencias:
            for ocurrencia in ocurrencias:
                resultado.insert(tk.END, f"Fila {ocurrencia['fila']}, Columna {ocurrencia['columna']}: {ocurrencia['texto']}\n")
            guardar_resultado(ocurrencias)
        else:
            messagebox.showinfo("Información", "No se encontraron ocurrencias.")
    
    except FileNotFoundError:
        messagebox.showerror("Error", f"El archivo {archivo} no fue encontrado.")


# Función para guardar el resultado en un archivo
def guardar_resultado(ocurrencias):
    with open("resultado_ocurrencias.txt", "w") as f:
        for ocurrencia in ocurrencias:
            f.write(f"Fila {ocurrencia['fila']}, Columna {ocurrencia['columna']}: {ocurrencia['texto']}\n")
    messagebox.showinfo("Guardado", "Los resultados han sido guardados en 'resultado_ocurrencias.txt'.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Texto con Autómata")
ventana.geometry("600x400")

# Variable para almacenar el archivo seleccionado
archivo_seleccionado = tk.StringVar()

# Crear widgets
tk.Label(ventana, text="Archivo seleccionado:").pack(pady=10)
tk.Entry(ventana, textvariable=archivo_seleccionado, width=50, state='readonly').pack(pady=5)
tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo).pack(pady=5)
tk.Button(ventana, text="Procesar archivo", command=procesar_archivo).pack(pady=5)

# Caja de texto para mostrar los resultados
resultado = tk.Text(ventana, height=10, width=60)
resultado.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
