# Definimos los sufijos válidos y los procesadores admitidos
sufijos_validos_ix = {"K", "F", "U", "T","G"}
sufijos_validos_xeon = {"W", "D", "M", "L", "T", "V", "R", "S", "E", "A"}
sujifos_validos_atom = {"C", "E", "Z", "P", "S", "T", "X", "Y", "N", "L", "M", "Q", "D", "B", "G", "H", "J", "K", "R", "U", "V", "W"}
modelos_validos_ix = {
    "i3", "i5", "i7", "i9"
}




# Función para procesar el texto letra por letra
def procesar_automata_letras(texto):
    estado = "inicial"
    buffer = ""  # Almacenará las letras mientras se procesa

    for letra in texto:
        if estado == "inicial":
            if letra == "i":
                estado = 'inicio_i'
                buffer += letra  
            elif letra == "c" :
                buffer += letra
                estado = "inicio_c"
            elif letra == "x":
                buffer += letra
                estado = "inicio_x"
            elif letra == "a":
                buffer += letra
                estado = "inicio_a"
            elif letra == "p":
                buffer += letra
                estado = "inicio_p" 
            else:
                estado = "invalido"
                buffer = ""  # Reinicia el buffer si no es válido

        elif estado == "inicio_i":
            buffer += letra
            print(buffer)
            if buffer in modelos_validos_ix:
                estado = "ix"
            elif letra == "n":
                estado = "in"
            elif letra == "t":
                estado = "it"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix":
            print(f'Llego a ix : {buffer}')
            if letra == "-" or letra == " ":
                buffer += letra
                estado = "ix_separador"
            elif letra == "\n":
                estado = "final"
            elif letra.isdigit():
                buffer += letra
                estado = "ix_generacion"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_separador":
            print(f'Llego a ix_separador : {buffer}')
            if letra == " " or letra == "\n" or letra == "-":
                buffer += letra
                estado = "invalido"
            elif letra.isdigit() and letra != "0":  # Aceptar cualquier dígito excepto "0"
                buffer += letra
                if letra == "1":
                    estado = "ix_generacion_1"
                else:
                    estado = "ix_generacion_n"
            else:
                estado = "invalido"
                buffer = ""    

        elif estado == "ix_generacion_1":
            print(f'Llego a ix_generacion_1 : {buffer}')
            if letra == " " or letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.isdigit():
                if letra == "1" or letra == "2" or letra == "3" or letra == "4":
                    buffer += letra
                    estado = "ix_generacion_1w"
                else:
                    buffer += letra
                    estado = "ix_generacion_1x"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1w":
            print(f'Llego a ix_generacion_1w : {buffer}')
            if letra.isdigit() and letra != "0":
                buffer += letra
                estado = "ix_generacion_1xx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1x":
            print(f'Llego a ix_generacion_1x : {buffer}')
            if letra.isdigit():
                if letra != "0":
                    buffer += letra
                    estado = "ix_generacion_1xx"
                else:
                    buffer += letra
                    estado = "ix_generacion_1xxx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1xx":
            print(f'Llego a ix_generacion_1xx : {buffer}')
            if letra.isdigit():
                buffer += letra
                estado = "ix_generacion_1xxx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1xxx":
            print(f'Llego a ix_generacion_1xxx : {buffer}')
            if letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.isdigit() and (letra == '5' or letra == '0'):
                buffer += letra
                estado = "ix_generacion_nxxx"    
            elif letra.upper() in sufijos_validos_ix:
                buffer += letra
                estado = "final"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"
            elif letra == " ":    
                buffer += letra
                estado = "ix_generacion_nxxx_"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_n":
            print(f'Llego a ix_generacion_n : {buffer}')
            if letra == " " or letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.isdigit():
                buffer += letra
                estado = "ix_generacion_nx"
            else:
                estado = "invalido"
                buffer = ""
        elif estado == "ix_generacion_nx":
            print(f'Llego a ix_generacion_nx : {buffer}')
            if letra.isdigit():
                buffer += letra
                estado = "ix_generacion_nxx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nxx":
            print(f'Llego a ix_generacion_nxx : {buffer}')
            if letra.isdigit() and (letra == '5' or letra == '0'):
                buffer += letra
                estado = "ix_generacion_nxxx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nxxx":
            print(f'Llego a ix_generacion_nxxx : {buffer}')
            if letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.upper() in sufijos_validos_ix:
                buffer += letra
                estado = "final"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"
            elif letra == " ":    
                buffer += letra
                estado = "ix_generacion_nxxx_"
            else:
                estado = "invalido"
                buffer = ""
        elif estado == "ix_generacion_nxxx_":
            print(f'Llego a ix_generacion_nxxx_ : {buffer}')
            if letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.upper() in sufijos_validos_ix:
                buffer += letra
                estado = "final"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nxxxA":
            print(f'Llego a ix_generacion_nxxxA : {buffer}')
            if letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.upper() in sufijos_validos_ix:
                buffer += letra
                estado = "final"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"    
            else:
                estado = "invalido"
                buffer = ""   

        elif estado == "ix_generacion_nxxxH":
            print(f'Llego a ix_generacion_nxxxH : {buffer}')
            if letra == "\n":
                buffer += letra
                estado = "final"
            elif letra.upper() == "Q":
                buffer += letra
                estado = "final"
            else:
                estado = "invalido"
                buffer = ""     

        elif estado == "inicio_c":
            buffer += letra
            if letra == "o":
                estado = "co"
            elif letra == "e":
                estado = "ce"
            else:
                estado = "invalido"
                buffer = ""    

       

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
