import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from IntelCoreSpotter import automata
import csv

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo", 
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        archivo_seleccionado.set(archivo)

    
def procesar_archivo():
    archivo = archivo_seleccionado.get()
    if not archivo:
        messagebox.showerror("Error", "Por favor selecciona un archivo.")
        return
    
    resultado.delete("1.0", tk.END) 
    ocurrencias = [] 
    
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()  # Leer todas las líneas del archivo
            for i, linea in enumerate(lineas, start=1):
                linea_lower = linea.lower()  # Convertir la línea a minúsculas
                for columna, simbolo in enumerate(linea_lower, start=1):
                    automata.procesar_simbolo(simbolo, i, columna) 
                
              
                if automata.cadena_larga:
                    automata.posiciones.append((i, len(linea_lower) - len(automata.cadena_larga), automata.cadena_larga))
                automata.reiniciar()

           
            if automata.posiciones:
                for posicion in automata.posiciones:
                    fila, columna, texto = posicion
                    ocurrencias.append({"fila": fila, "columna": columna, "texto": texto})

      
        if ocurrencias:
            for ocurrencia in ocurrencias:
                resultado.insert(tk.END, f"Fila {ocurrencia['fila']}, Columna {ocurrencia['columna']}: {ocurrencia['texto']}\n")
            guardar_resultado(ocurrencias)
        else:
            messagebox.showinfo("Información", "No se encontraron ocurrencias.")
    
    except FileNotFoundError: 
        messagebox.showerror("Error", f"El archivo {archivo} no fue encontrado.")



def guardar_resultado(ocurrencias):
    formato = messagebox.askquestion("Guardar como", "¿En qué formato deseas guardar el reporte? (Sí para TXT, No para CSV)")
    
    if formato == 'yes':
        guardar_como_txt(ocurrencias)
    else:
        guardar_como_csv(ocurrencias)

def guardar_como_txt(ocurrencias):
    with open("resultado_ocurrencias.txt", "w") as f:
        for ocurrencia in ocurrencias:
            f.write(f"Fila {ocurrencia['fila']}, Columna {ocurrencia['columna']}: {ocurrencia['texto']}\n")
    messagebox.showinfo("Guardado", "Los resultados han sido guardados en 'resultado_ocurrencias.txt'.")

def guardar_como_csv(ocurrencias):
    with open("resultado_ocurrencias.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["fila", "columna", "texto"])
        writer.writeheader()
        for ocurrencia in ocurrencias:
            writer.writerow(ocurrencia)
    messagebox.showinfo("Guardado", "Los resultados han sido guardados en 'resultado_ocurrencias.csv'.")
ventana = tk.Tk()
ventana.title("IntelCoreSpotter")


ventana.configure(bg='#0071C5')  
ventana.geometry("700x600")

# Descripción del programa
descripcion = """IntelCoreSpotter es una herramienta que permite validar modelos de procesadores Intel en archivos de texto.
Valida series de procesadores como Intel Core (i3, i5, i7, i9), Itanium (2 y 9) y Xeon (scalable series 3,4,5).
Puedes cargar archivos y verificar las coincidencias encontradas en las líneas del texto."""

tk.Label(ventana, text="IntelCoreSpotter", font=("Arial", 24, "bold"), bg="#0071C5", fg="white").pack(pady=10)
tk.Label(ventana, text=descripcion, font=("Arial", 12), bg="#0071C5", fg="white", wraplength=650, justify="left").pack(pady=10)


archivo_seleccionado = tk.StringVar()


frame_seleccion = tk.Frame(ventana, bg='#0071C5')
frame_seleccion.pack(pady=20)

tk.Label(frame_seleccion, text="Archivo seleccionado:", font=("Arial", 12), bg="#0071C5", fg="white").pack(side="left")
tk.Entry(frame_seleccion, textvariable=archivo_seleccionado, width=50, state='readonly').pack(side="left", padx=10)
tk.Button(frame_seleccion, text="Seleccionar archivo", command=seleccionar_archivo, bg="#FFFFFF", fg="#0071C5").pack(side="left")


tk.Button(ventana, text="Procesar archivo", command=procesar_archivo, bg="#FFFFFF", fg="#0071C5", font=("Arial", 12)).pack(pady=10)


resultado = scrolledtext.ScrolledText(ventana, height=15, width=80, bg="#E5F6FD", fg="black")
resultado.pack(pady=10)


ventana.mainloop()
