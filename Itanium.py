
# Función para procesar el texto letra por letra
def procesar_automata_itanium(texto,fila,ocurrencias):
    estado = "inicial"
    buffer = ""  # Almacenará las letras mientras se procesa
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
            if letra == "t":
                buffer += letra
                estado = "it"
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
            if letra == "t":
                buffer += letra
                estado = "ix"
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
            if letra == "t":
                buffer += letra
                estado = "it"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "it":
            if letra == "a":
                buffer += letra
                estado = "ita"
            else:
                estado = "invalido"
                buffer = ""
                
        elif estado == "ita":
            if letra == "n":
                buffer += letra
                estado = "itan"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "itan":
            if letra == "i":
                buffer += letra
                estado = "itani"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "itani":
            if letra == "u":
                buffer += letra
                estado = "itaniu"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "itaniu":
            if letra == "m":
                buffer += letra
                estado = "itanium"
            else:
                estado = "invalido"
                buffer = ""
        
        elif estado == "itanium":
            print("Llego a itanium : "+ buffer)
            if letra == "-" or letra == " ": 
                buffer += letra
                estado = "itanium-"
            else:
                estado = "invalido"
                buffer = ""

        elif estado == "itanium-":
            if letra.isdigit():
                if letra == "2":
                    estado = "itanium-2"
                    buffer += letra
                elif letra == "9":
                    estado = "itanium-9"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
       
        elif estado == "itanium-2":
            if letra == " " or letra == "-":
                estado = "itanium-2-"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra    


        elif estado == "itanium-2-":
            if letra.isdigit():
                if letra == "0" or letra == "1" or letra == "2" :
                    estado = "itanium-2-n"
                    buffer += letra
                elif letra == "9":
                    estado = "itanium-2-9"
                    buffer += letra    
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-2-n":
            if letra == ".":
                estado = "itanium-2-n."
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-2-n.":
            if letra.isdigit():
                if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9":
                    estado = "itanium-2-n.n"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra        

        elif estado == "itanium-2-n.n":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-2-9":
            if letra.isdigit():
                if letra == "0" :
                    estado = "itanium-2-90"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra    
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-2-90":        
            if letra.isdigit():
                if letra == "0" :
                    estado = "itanium-2-900"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra    
            else:
                estado = "invalido"
                buffer += letra


        elif estado == "itanium-2-900":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra 


        elif estado == "itanium-9":
            if letra.isdigit():
                if letra == "0":
                    estado = "itanium-90"
                    buffer += letra
                elif letra == "1":
                    estado = "itanium-91"
                    buffer += letra   
                elif letra == "3":
                    estado = "itanium-93"
                    buffer += letra
                elif letra == "5":
                    estado = "itanium-95"
                    buffer += letra
                elif letra == "7":
                    estado = "itanium-97"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra     
                        

        elif estado == "itanium-90":
            if letra.isdigit():
                if letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" :
                    estado = "itanium-90n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra      

        elif estado == "itanium-90n":
            if letra == "0":
                estado = "itanium-90n0"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra      

        elif estado == "itanium-90n0":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-91":
            if letra.isdigit():
                if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5":
                    estado = "itanium-91n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra          

        elif estado == "itanium-91n":
            if letra == "0":
                estado = "itanium-91n0"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-91n0":
            if letra == " " or letra == "-":
                estado = "itanium-91n0-"
                buffer += letra
            elif letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra        

        elif estado == "itanium-91n0-":
            if letra == "n":
                estado = "itanium-91n0-n"
                buffer += letra    
            elif letra.isdigit():
                estado = "invalido"
                buffer += letra
            else:
                estado = "final"
                buffer += letra

        elif estado == "itanium-91n0-n":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-93":
            if letra.isdigit():
                if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5":
                    estado = "itanium-93n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra

        elif estado == "itanium-93n":
            if letra == "0":
                estado = "itanium-93n0"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "itanium-93n0":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "itanium-95":
            if letra.isdigit():
                if letra == "0" or letra == "1" or letra == "2" or letra == "4" or letra == "6" or letra == "8":
                    estado = "itanium-95n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra          

        elif estado == "itanium-95n":
            if letra == "0":
                estado = "itanium-95n0"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "itanium-95n0":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra


        elif estado == "itanium-97":
            if letra.isdigit():
                if letra == "2" or letra == "4" or letra == "5" or letra == "6":
                    estado = "itanium-97n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra      

        elif estado == "itanium-97n":
            if letra == "0":
                estado = "itanium-97n0"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra   

        elif estado == "itanium-97n0":
            if letra == " " or letra == "\n" or letra == "\t":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        
        # Si llega al estado final, significa que la cadena es válida
        if estado == "final":
            ocurrencias.append({"fila": fila, "columna": columna, "texto": buffer})
            print(f"Cadena válida: {buffer}")
            buffer = ""
            estado = "inicial"  # Reiniciar el autómata para procesar nuevas cadenas
        elif estado == "invalido":
            buffer = ""
            estado = "inicial"

