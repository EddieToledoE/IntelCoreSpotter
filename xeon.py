
# RECORDAR CHECAR QUE CUANDO VALIDAS EL ELSE: FINAL Y PONES EL BUFFER MAS LETRA PROBABLEMENTE ESTE MAL PQ ESA LETRA X QUE IGNORA PUES SE AGREGA AL BUFFER Y NO DEBERIA ()
# Función para procesar el texto letra por letra
def procesar_automata_xeon(texto,fila,ocurrencias):
    estado = "inicial"
    buffer = ""  # Almacenará las letras mientras se procesa
    for columna, letra in enumerate(texto, start=1):

        if estado == "inicial":
            if letra == "x":
                estado = "x"
                buffer += letra
            elif letra == "i":
                estado = "i"
                buffer += letra
            elif letra == "c":
                estado = "c"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra


        elif estado == "x":
            if letra == "e":
                estado = "xe"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xe":
            if letra == "o":
                estado = "xeo"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeo":
            if letra == "n":
                estado = "xeon"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon":
            if letra == " " or letra == "-":
                estado = "xeon_espacio"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "i":
            if letra == "n":
                estado = "in"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "in":
            if letra == "t":
                estado = "int"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "int":
            if letra == "e":
                estado = "inte"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "inte":
            if letra == "l":
                estado = "intel"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "intel":
            if letra == " " :
                estado = "intel_espacio"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "intel_espacio":
            if letra == "c":
                estado = "c"
                buffer += letra
            elif letra == "x":
                estado = "x"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "c":
            if letra == "o":
                estado = "co"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "co":
            if letra == "r":
                estado = "cor"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "cor":
            if letra == "e":
                estado = "core"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "core":
            if letra == " ":
                estado = "core_espacio"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "core_espacio":
            if letra == "x":
                estado = "x"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "xeon_espacio":
            if letra.isdigit():
                if letra == "3":
                    estado = "xeon 3"
                    buffer += letra
                elif letra == "4":
                    estado = "xeon 4"
                    buffer += letra
                elif letra == "5":
                    estado = "xeon 5"
                    buffer += letra
                elif letra == "6":
                    estado = "xeon 6"
                    buffer += letra
                elif letra == "8:":
                    estado = "xeon 8"
                    buffer += letra
                elif letra == "9":
                    estado = "xeon 9"
                    buffer += letra
                else: 
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra  
                
        elif estado == "xeon 3":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 31"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 32"
                    buffer += letra
                elif letra == "4" or letra == "5":
                    estado = "xeon 3n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
                    
        elif estado == "xeon 31":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 310"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 310":
            if letra.isdigit():
                if letra == "4" or letra == "6":
                    estado = "xeon 310n"
                    buffer += letra
                elif letra == "8":
                    estado = "xeon 3108"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra


        elif estado == "xeon 310n":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 3108":
            if letra == " " or letra == "-":
                estado = "xeon 3108_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
            
        elif estado == "xeon 3108_espacio":
            if letra == "u":
                estado = "xeon 3108u"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 3108u":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 32":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 320"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 320":
            if letra.isdigit():
                if letra == "4":
                    estado = "xeon 3204"
                    buffer += letra
                elif letra == "6":
                    estado = "xeon 3206"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 3204":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 3206":
            if letra == " " or letra == "-":
                estado = "xeon 3206_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 3206_espacio":
            if letra == "r":
                estado = "xeon 3206r"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 3206r":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 3n":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 3n0"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
               
        elif estado == "xeon 3n0":
            if letra.isdigit():
                if letra == "8":
                    estado = "xeon 3n08"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra 
                
        elif estado == "xeon 3n08":
            if letra == " " or letra == "-":
                estado = "xeon 3n08_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 3n08_espacio":
            if letra == "u":
                estado = "xeon 3n08u"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 3n08u":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 4":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 41"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 42"
                    buffer += letra
                elif letra == "3":
                    estado = "xeon 43"
                    buffer += letra
                elif letra == "4":
                    estado = "xeon 44"
                    buffer += letra
                elif letra == "5":
                    estado = "xeon 45"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 41":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 410"
                    buffer += letra
                if letra == "1":
                    estado = "xeon 411"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 410":
            if letra.isdigit():
                if letra == "9":
                    estado = "xeon 4109"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 4109":
            if letra == " " or letra == "-":
                estado = "xeon 4109_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
            
        elif estado == "xeon 4109_espacio":
            if letra == "t":
                estado = "xeon 4109t"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 4109t":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 411":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 4110"
                    buffer += letra
                elif letra == "4" or letra == "6":
                    estado = "xeon 411n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
            
        elif estado == "xeon 4110":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 411n":
            if letra == " " or letra == "-":
                estado = "xeon 411n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 411n_espacio":
            if letra == "t":
                estado = "xeon 411nt"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 411nt":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 42":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 420"
                    buffer += letra
                elif letra == "1":
                    estado = "xeon 421"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 420":
            if letra.isdigit():
                if letra == "8" or letra == "9":
                    estado = "xeon 420n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 420n":
            if letra == " " or letra == "-":
                estado = "xeon 420n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 420n_espacio":
            if letra == "t":
                estado = "xeon 420nt"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 420nt":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 421":
            if letra.isdigit():
                if letra == "0" or letra == "4" or letra == "5" or letra == "6":
                    estado = "xeon 421n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 421n":
            if letra == " " or letra == "-":
                estado = "xeon 421n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 421n_espacio":
            if letra == "r":
                estado = "xeon 421nr"
                buffer += letra
            else:
                estado = "final"
                buffer += letra     
                
        elif estado == "xeon 421nr":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra  
                
        elif estado == "xeon 43":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 431"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 431":
            if letra.isdigit():
                if letra == "0" or letra == "4" or letra == "6":
                    estado = "xeon 431n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 431n":
            if letra == " " or letra == "-":
                estado = "xeon 431n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 431n_espacio":
            if letra == "t":
                estado = "xeon 431nt"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 431nt":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 44":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 441"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 441":
            if letra.isdigit():
                if letra == "0" or letra == "6":
                    estado = "xeon 441n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 441n":
            if letra == " " or letra == "-":
                estado = "xeon 441n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 441n_espacio":
            if letra == "t" or letra == "y":
                estado = "xeon 441nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 441nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 45":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 451"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "xeon 451":
            if letra.isdigit():
                if letra == "0" or letra == "4" or letra == "6":
                    estado = "xeon 451n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 451n":
            if letra == " " or letra == "-":
                estado = "xeon 451n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 451n_espacio":
            if letra == "t" or letra == "y":
                estado = "xeon 451nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 451nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 51"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 52"
                    buffer += letra
                elif letra == "3":
                    estado = "xeon 53"
                    buffer += letra
                elif letra == "4":
                    estado = "xeon 54"
                    buffer += letra
                elif letra == "5":
                    estado = "xeon 55"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra 
        
        elif estado == "xeon 51":
            if letra.isdigit():
                if letra == "1" :
                    estado = "xeon 511"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 512"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra    
                
        elif estado == "xeon 511":
            if letra.isdigit():
                if letra == "8" or letra == "9":
                    estado = "xeon 511n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
                    
        elif estado == "xeon 511n":
            if letra == " " or letra ==  "-":
                estado = "xeon 511n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 511n_espacio":
            if letra == "t":
                estado = "xeon 511nt"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 511nt":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 512":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 5120"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5120":
            if letra == " " or letra == "-":
                estado = "xeon 5120_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 5120_espacio":
            if letra == "t":
                estado = "xeon 5120t"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 5120t":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 52":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 521"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 522"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra

        elif estado == "xeon 521":
            if letra.isdigit():
                if letra == "5" or letra == "8":
                    estado = "xeon 521n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 521n":
            if letra == " " or letra == "-":
                estado = "xeon 521n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 521n_espacio":
            if letra == "t" or letra == "r" or letra == "n" or letra == "b":
                estado = "xeon 521nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 521nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 522":
            if letra.isdigit():
                if letra == "0" or letra == "2":
                    estado = "xeon 522n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 522n":
            if letra == " " or letra == "-":
                estado = "xeon 522n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 522n_espacio":
            if letra == "t" or letra == "r" or letra == "s":
                estado = "xeon 522nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 522nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 53":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 531"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 532"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 531":
            if letra.isdigit():
                if letra == "5" or letra =="7" or letra == "8":
                    estado = "xeon 531n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 531n":
            if letra == " " or letra == "-":
                estado = "xeon 531n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 531n_espacio":
            if letra == "y" or letra == "n" or letra == "s" or letra == "h":
                estado = "xeon 531nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 531nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 532":
            if letra.isdigit():
                if letra == "0":
                    estado = "xeon 5320"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5320":
            if letra == " " or letra == "-":
                estado = "xeon 5320_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5320_espacio":
            if letra == "t" or letra == "h":
                estado = "xeon 5320x"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 5320x":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 54":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 541"
                    buffer += letra
                elif letra == "2" or letra == "3":
                    estado = "xeon 54n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 541":
            if letra.isdigit():
                if letra == "1" or letra == "5" or letra == "6" or letra == "8":
                    estado = "xeon 541n"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 541n":
            if letra == " " or letra == "-":
                estado = "xeon 541n_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 541n_espacio":
            if letra == "n" or letra == "s" or letra == "t":
                estado = "xeon 541nx"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 541nx":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 54n":
            if letra.isdigit():
                if letra == "3":
                    estado = "xeon 54n3"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 54n3":
            if letra == " " or letra == "-":
                estado = "xeon 54n3_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra        
                
        elif estado == "xeon 54n3_espacio":
            if letra == "n" :
                estado = "xeon 54n3n"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
                
        elif estado == "xeon 54n3n":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 55":
            if letra.isdigit():
                if letra == "1":
                    estado = "xeon 551"
                    buffer += letra
                elif letra == "2":
                    estado = "xeon 552"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 551":
            if letra.isdigit():
                if letra == "2":
                    estado = "xeon 5512"
                    buffer += letra
                elif letra == "5" :
                    estado = "xeon 5515"
                    buffer += letra
                else:
                    estado = "invalido"
                    buffer += letra
            else:
                estado = "invalido"
                buffer += letra
        
        elif estado == "xeon 5512":
            if letra == " " or letra == "-":
                estado = "xeon 5512_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5512_espacio":
            if letra == "u":
                estado = "xeon 5512u"
                buffer += letra
            else:
                estado = "final"
                buffer += letra

        elif estado == "xeon 5512u":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5515":
            if letra == " " or letra == "-":
                estado = "xeon 5515_espacio"
                buffer += letra
            elif letra == "\n" or letra == "\t" or letra == ".":
                estado = "final"
                buffer += letra
            else:
                estado = "invalido"
                buffer += letra
                
        elif estado == "xeon 5515_espacio":
            if letra == "t":
                estado = "xeon 5515t"
                buffer += letra
            else:
                estado = "final"
                buffer += letra
        
        elif estado == "xeon 5515t":
            if letra == " " or letra == "\n" or letra == "\t" or letra == ".":
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