#Sufijos validos para el modelo iX
sufijos_validos_ix = {"K", "F", "U", "T","G"}
modelos_validos_ix = {
    "i3", "i5", "i7", "i9"
}


def procesar_automata_letras(texto,fila,ocurrencias):
    estado = "inicial"
    buffer = ""
    for columna, letra in enumerate(texto, start=1):

        if estado == "inicial":
            if letra == "i":
                buffer += letra
                estado = "inicio_i"
            elif letra == "c":
                buffer += letra
                estado = "inicio_c"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "inicio_i":
            if letra == "3" or letra == "5" or letra == "7" or letra == "9":
                buffer += letra
                estado = "ix"
            elif letra == "n":
                buffer += letra
                estado = "in"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "in":
            if letra == "t":
                buffer += letra
                estado = "int"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "int":
            if letra == "e":
                buffer += letra
                estado = "inte"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "inte":
            if letra == "l":
                buffer += letra
                estado = "intel"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "intel":
            if letra == " ":
                buffer += letra
                estado = "intel_espacio"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "intel_espacio":
            if letra == "c":
                buffer += letra
                estado = "inicio_c"
            elif letra == "i":
                buffer += letra
                estado = "intel_i"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "intel_i":
            if letra.isdigit():
                if letra == "3" or letra == "5" or letra == "7" or letra == "9":
                    buffer += letra
                    estado = "ix"
                else:
                    estado = "invalido"
                    buffer = ""
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "inicio_c":
            if letra == "o":
                buffer += letra
                estado = "co"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "co":
            if letra == "r":
                buffer += letra
                estado = "cor"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "cor":
            if letra == "e":
                buffer += letra
                estado = "core"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "core":
            if letra == " ":
                buffer += letra
                estado = "core_espacio"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "core_espacio":
            if letra == "i":
                buffer += letra
                estado = "core_i"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "core_i":
            if letra.isdigit():
                if letra == "3" or letra == "5" or letra == "7" or letra == "9":
                    buffer += letra
                    estado = "ix"
                else:
                    estado = "invalido"
                    buffer = ""
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "ix":
            print(f'Llego a ix metodo : {buffer}')
            if letra == "-" or letra == " ":
                buffer += letra
                estado = "ix_separador"
            elif letra == "\n" or letra == "\t":
                estado = "final"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_separador":
            print(f'Llego a ix_separador : {buffer}')
            if letra.isdigit() and letra != "0":  # Aceptar cualquier dígito excepto "0"
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
            if letra.isdigit():
                if letra =="0" or letra == "1" or letra == "2" or letra == "3" or letra == "4": # GEN 10-14
                    buffer += letra
                    estado = "ix_generacion_1g"
                else: # GEN 1 recibiendo 5-9
                    buffer += letra
                    estado = "ix_generacion_1x"
            elif letra == "t":
                buffer += letra
                estado = "ix_generacion_1t"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1t":
            print(f'Llego a ix_generacion_1t : {buffer}')   
            if letra == "h":
                buffer += letra
                estado = "ix_generacion_1th"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1th":
            print(f'Llego a ix_generacion_1th : {buffer}')
            if letra == "\n" or letra == " ":
                buffer += letra
                estado = "final"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1g":
            print(f'Llego a ix_generacion_1g : {buffer}')
            if letra.isdigit() and letra != "0": #Es decir 1-9
                buffer += letra
                estado = "ix_generacion_1gx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1gx":
            print(f'Llego a ix_generacion_1gx : {buffer}')
            if letra.isdigit(): #Acepta cualquier digito
                buffer += letra
                estado = "ix_generacion_1gxx"
            else:
                estado = "invalido"
                buffer = ""        

        elif estado == "ix_generacion_1gxx":
            print(f'Llego a ix_generacion_1gxx : {buffer}')
            if letra.isdigit() and (letra == '5' or letra == '0'):
                buffer += letra
                estado = "ix_generacion_nxxx"
            else:
                estado = "invalido"
                buffer = ""



        elif estado == "ix_generacion_1x":
            print(f'Llego a ix_generacion_1x : {buffer}')
            if letra.isdigit() and (letra == '5' or letra == '0'):
                buffer += letra
                estado = "ix_generacion_1xx"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_1xx":
            print(f'Llego a ix_generacion_1xx : {buffer}')
            if letra == "\n" or letra == " ": #Los de primera generacion no tienen sufijo y lucen asi i3 150, con solo 2 numeros de sku
                buffer += letra
                estado = "final"
            else:
                estado = "invalido"
                buffer = ""        

        elif estado == "ix_generacion_n":
            print(f'Llego a ix_generacion_n : {buffer}')
            if letra.isdigit() and letra != "0": # Aceptar cualquier dígito excepto "0"
                buffer += letra
                estado = "ix_generacion_nx"
            elif letra == "t":
                buffer += letra
                estado = "ix_generacion_1t" # Lo manda a obtener el "th"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nx":
            print(f'Llego a ix_generacion_nx : {buffer}')
            if letra.isdigit() and letra != "0":
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
                estado = "ix_generacion_nxxxs"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"
            elif letra == " ":    
                buffer += letra
                estado = "ix_generacion_nxxx_"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nxxxs":
            print(f'Llego a ix_generacion_nxxxs : {buffer}')
            if letra == "\n" or letra == " ":
                buffer += letra
                estado = "final"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "ix_generacion_nxxx_":
            print(f'Llego a ix_generacion_nxxx_ : {buffer}')
            if letra.upper() in sufijos_validos_ix:
                buffer += letra
                estado = "ix_generacion_nxxxs"
            elif letra.upper() == "H":
                buffer += letra
                estado = "ix_generacion_nxxxH"
            else:
                estado = "invalido"
                buffer = ""


        elif estado == "ix_generacion_nxxxH":
            print(f'Llego a ix_generacion_nxxxH : {buffer}')
            if letra == "\n" or letra == " ":
                buffer += letra
                estado = "final"
            elif letra.upper() == "Q":
                buffer += letra
                estado = "ix_generacion_nxxxHQ"
            else:
                estado = "invalido"
                buffer = ""     


        elif estado == "ix_generacion_nxxxHQ":
            print(f'Llego a ix_generacion_nxxxHQ : {buffer}')
            if letra == "\n" or letra == " ":
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
            ocurrencias.append({"fila": fila, "columna": columna, "texto": buffer})
            print(f"Cadena válida: {buffer}")
            buffer = ""
            estado = "inicial"
        elif estado == "invalido":
            buffer = ""
            estado = "inicial"

