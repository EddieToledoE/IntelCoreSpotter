
# En este caso sera con la cadena xeon ya procesada digamos, es decir ya tenemos "xeon" en el buffer  


# Función para procesar el texto letra por letra
def procesar_automata_letras(texto):
    estado = "inicial"
    buffer = ""  # Almacenará las letras mientras se procesa

    for letra in texto:
        if estado == "inicial":
            if letra == " " or letra == "-":
                estado = "xeon-"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra




        
        # Si llega al estado final, significa que la cadena es válida
        if estado == "final":
            print(f"Cadena válida: {buffer}")
            buffer = ""
            estado = "inicial"  # Reiniciar el autómata para procesar nuevas cadenas
        elif estado == "invalido":
            buffer = ""
            estado = "inicial"

# Función para leer el documento y procesar letra por letra
def leer_documento_y_procesar(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read().lower()
            return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
        return ""

# Nombre del archivo de texto
nombre_archivo = 'prueba.txt'

# Leer el documento
contenido = leer_documento_y_procesar(nombre_archivo)

# Procesar el autómata letra por letra si el archivo se leyó correctamente
if contenido:
    procesar_automata_letras(contenido)
