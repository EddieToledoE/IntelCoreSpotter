import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from main import procesar_automata_letras
from Itanium import procesar_automata_itanium
from xeon import procesar_automata_xeon
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
                procesar_automata_itanium(linea_lower, i, ocurrencias)
                procesar_automata_xeon(linea_lower, i, ocurrencias)
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
ventana.title("IntelCoreSpotter")

# Cambiar el color de fondo de la ventana
ventana.configure(bg='#0071C5')  # Azul característico de Intel
ventana.geometry("700x600")

# Descripción del programa
descripcion = """IntelCoreSpotter es una herramienta que permite validar modelos de procesadores Intel en archivos de texto.
Valida series de procesadores como Intel Core (i3, i5, i7, i9) y Itanium, entre otros.
Puedes cargar archivos y verificar las coincidencias encontradas en las líneas del texto."""

tk.Label(ventana, text="IntelCoreSpotter", font=("Arial", 24, "bold"), bg="#0071C5", fg="white").pack(pady=10)
tk.Label(ventana, text=descripcion, font=("Arial", 12), bg="#0071C5", fg="white", wraplength=650, justify="left").pack(pady=10)

# Variable para almacenar el archivo seleccionado
archivo_seleccionado = tk.StringVar()

# Crear widgets para seleccionar archivo
frame_seleccion = tk.Frame(ventana, bg='#0071C5')
frame_seleccion.pack(pady=20)

tk.Label(frame_seleccion, text="Archivo seleccionado:", font=("Arial", 12), bg="#0071C5", fg="white").pack(side="left")
tk.Entry(frame_seleccion, textvariable=archivo_seleccionado, width=50, state='readonly').pack(side="left", padx=10)
tk.Button(frame_seleccion, text="Seleccionar archivo", command=seleccionar_archivo, bg="#FFFFFF", fg="#0071C5").pack(side="left")

# Botón para procesar el archivo
tk.Button(ventana, text="Procesar archivo", command=procesar_archivo, bg="#FFFFFF", fg="#0071C5", font=("Arial", 12)).pack(pady=10)

# Caja de texto para mostrar los resultados con scroll
resultado = scrolledtext.ScrolledText(ventana, height=15, width=80, bg="#E5F6FD", fg="black")
resultado.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
