class ADF:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_actual = estado_inicial
        self.estados_finales = estados_finales

    def procesar_simbolo(self, simbolo):
        if simbolo in self.alfabeto and (self.estado_actual, simbolo) in self.transiciones:
            self.estado_actual = self.transiciones[(self.estado_actual, simbolo)]
        else:
            self.estado_actual = "invalido"  # Si no hay transición válida

    def es_aceptado(self):
        return self.estado_actual in self.estados_finales

    def reiniciar(self):
        self.estado_actual = "inicial"

# Definimos los componentes del ADF

estados = {"inicial", "inicio_i", "ix", "ix_separador", "ix_generacion_1", "ix_generacion_n", "final", "invalido"}
alfabeto = set("i351079- ")  # Puedes expandir esto según los símbolos que quieras aceptar

# Definir las transiciones (estado_actual, simbolo) -> estado_siguiente
transiciones = {
    # Agrega más transiciones aquí según las reglas de tu ADF
    ("q0", "i"): "q1",
    ("q0", "c"): "q8",
    ("q0", "x"): "q9",
    ("q1", "n"): "q2",
    ("q1", "t"): "q15",
    ("q1", "3"): "q16",
    ("q1", "5"): "q16",
    ("q1", "7"): "q16",
    ("q1", "9"): "q16",
    ("q2", "t"): "q3",
    ("q3", "e"): "q4",
    ("q4", "l"): "q5",
    ("q5", " "): "q6",
    ("q6", "i"): "q7",
    ("q6", "c"): "q8",
    ("q6", "x"): "q9",
    ("q7", "t"): "q15",
    ("q7", "3"): "q16",
    ("q7", "5"): "q16",
    ("q7", "7"): "q16",
    ("q7", "9"): "q16",
    ("q8", "o"): "q10",
    ("q10", "r"): "q11",
    ("q11", "e"): "q12",
    ("q12", " "): "q13",
    ("q13", "x"): "q9",
    ("q13", "i"): "q14",
    ("q14", "t"): "q15",
    ("q14", "3"): "q16",  # I3 ESTADO FINAL ACEPTADOS
    ("q14", "5"): "q16",  # I5
    ("q14", "7"): "q16",  # I7
    ("q14", "9"): "q16",  # I9
    ("q16", " "): "q17",  # COMIENZAN LA LINEA DE PROCESADORES IX CON GENERACION Y SUFIJOS
    ("q16", "-"): "q17",
    ("q17", "1"): "q18",
    ("q18", "0"): "q21",
    ("q18", "1"): "q21",
    ("q18", "2"): "q21",
    ("q18", "3"): "q21",
    ("q18", "4"): "q21",
    ("q18", "5"): "q22",
    ("q18", "6"): "q22",
    ("q18", "7"): "q22",
    ("q18", "8"): "q22",
    ("q18", "9"): "q22",
    ("q18", "t"): "q19",  # Validar "th"
    ("q19", "h"): "q20",  # Th validado, Estado final :
    ("q20", "\n"): "final",  # Salto de línea
    ("q20", "\r"): "final",  # Retorno de carro
    ("q20", "\t"): "final",  # Tabulador
    ("q20", " "): "final",   # Espacio
    ("q20", "."): "final",   # Punto
    # ("q20", ""): "final",     # Fin de la cadena (cadena vacía)
    ("q21", "t"): "q19",
    ("q22", "0"): "q23",
    ("q22", "5"): "q23",  # Primera generacion de procesadores IX validada, estado final :
    ("q23", "\n"): "final",  # Salto de línea
    ("q23", "\r"): "final",  # Retorno de carro
    ("q23", "\t"): "final",  # Tabulador
    ("q23", " "): "final",   # Espacio
    ("q23", "."): "final",   # Punto
    # ("q23", ""): "final",     # Fin de la cadena (cadena vacía)
    ("q21", "1"): "q24",
    ("q21", "2"): "q24",
    ("q21", "3"): "q24",
    ("q21", "4"): "q24",
    ("q21", "5"): "q24",
    ("q21", "6"): "q24",
    ("q21", "7"): "q24",
    ("q21", "8"): "q24",
    ("q21", "9"): "q24", 
    ("q24", "0"): "q25",  
    ("q24", "1"): "q25",
    ("q24", "2"): "q25",
    ("q24", "3"): "q25",
    ("q24", "4"): "q25",
    ("q24", "5"): "q25",
    ("q24", "6"): "q25",
    ("q24", "7"): "q25",
    ("q24", "8"): "q25",
    ("q24", "9"): "q25",
    ("q25", "0"): "q29",
    ("q25", "5"): "q29",
    ("q17", "2"): "q26",
    ("q17", "3"): "q26", 
    ("q17", "4"): "q26",
    ("q17", "5"): "q26",
    ("q17", "6"): "q26",
    ("q17", "7"): "q26",
    ("q17", "8"): "q26",
    ("q17", "9"):"q26",
    ("q26","1"): "q27",   
    ("q26","2"): "q27",
    ("q26","3"): "q27", 
    ("q26","4"): "q27",
    ("q26","5"): "q27",
    ("q26","6"): "q27",
    ("q26","7"): "q27",
    ("q26","8"): "q27",
    ("q26","9"): "q27",
    ("q27","1"): "q28",   
    ("q27","2"): "q28",
    ("q27","3"): "q28", 
    ("q27","4"): "q28",
    ("q27","5"): "q28",
    ("q27","6"): "q28",
    ("q27","7"): "q28",
    ("q27","8"): "q28",
    ("q27","9"): "q28",
    ("q28","0"): "q29",
    ("q28","5"): "q29", # Procesadores con el siguiente formato valido : ix GeneracionModelo comenzara validar cadena final
    ("q29", "\n"): "final",  # Salto de línea
    ("q29", "\r"): "final",  # Retorno de carro
    ("q29", "\t"): "final",  # Tabulador
    ("q29", " "): "final",   # Espacio
    ("q29", "."): "final",   # Punto
    # ("q29", ""): "final",     # Fin de la cadena (cadena vacía) Procesadores con el siguiente formato valido : ix GeneracionModelo Sufijo comenzara validar cadena final
    ("q29","k"): "q30",
    ("q29","f"): "q30",
    ("q29","u"): "q30",
    ("q29","t"): "q30",
    ("q29","g"): "q30",
    ("q29","h"): "q31",
    ("q30", "\n"): "final",  # Salto de línea
    ("q30", "\r"): "final",  # Retorno de carro
    ("q30", "\t"): "final",  # Tabulador
    ("q30", " "): "final",   # Espacio
    ("q30", "."): "final",   # Punto
    # ("q30", ""): "final"     # Fin de la cadena (cadena vacía)
    ("q31","q"): "q32",
    ("q32", "\n"): "final",  # Salto de línea
    ("q32", "\r"): "final",  # Retorno de carro
    ("q32", "\t"): "final",  # Tabulador
    ("q32", " "): "final",   # Espacio
    ("q32", "."): "final",   # Punto
    # ("q32", ""): "final",    # Fin de la cadena (cadena vacía)    #LINEA ITANIUM 
    ("q15","a"): "q33",
    ("q33","n"): "q34",
    ("q34","i"): "q35", 
    ("q35","u"): "q36",
    ("q36","m"): "q37",
    ("q37"," "): "q38",
    ("q38","2"): "q39",
    ("q39"," "): "q40",
    ("q39","-"): "q40",
    ("q40","9"): "q41",
    ("q41"," "): "final", #Espacio Itanium 2-9 estado final aceptado
    ("q41", "\n"): "final",  # Salto de línea
    ("q41", "\r"): "final",  # Retorno de carro
    ("q41", "\t"): "final",  # Tabulador
    ("q41", "."): "final",   # Punto
    # ("q41", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q41","0"): "q42",
    ("q42","0"): "q43",
    ("q43"," "): "final", #Espacio Itanium 2-900 estado final aceptado
    ("q43", "\n"): "final",  # Salto de línea
    ("q43", "\r"): "final",  # Retorno de carro
    ("q43", "\t"): "final",  # Tabulador
    ("q43", "."): "final",   # Punto
 # ("q43", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q40","0"): "q44",
    ("q40","1"): "q44",
    ("q40","2"): "q44",
    ("q44","."): "q45",
    ("q45","0"): "q46",
    ("q45","1"): "q46",
    ("q45","2"): "q46",
    ("q45","3"): "q46",
    ("q45","4"): "q46",
    ("q45","5"): "q46",
    ("q45","6"): "q46",
    ("q45","7"): "q46",
    ("q45","8"): "q46",
    ("q45","9"): "q46",
    ("q46"," "): "final", # Espacio Itanium 2_2.5 estado final aceptado
    ("q46", "\n"): "final",  # Salto de línea
    ("q46", "\r"): "final",  # Retorno de carro
    ("q46", "\t"): "final",  # Tabulador
    ("q46", "."): "final",   # Punto
# ("q46", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q38","9"): "q47",
    ("q47","0"): "q48",
    ("q48","1"): "q49",
    ("q48","2"): "q49",
    ("q48","3"): "q49",
    ("q48","4"): "q49",
    ("q48","5"): "q49",
    ("q49","0"): "q50",
    ("q50"," "): "final", #Espacio Itanium 900 estado final aceptado
    ("q50", "\n"): "final",  # Salto de línea
    ("q50", "\r"): "final",  # Retorno de carro
    ("q50", "\t"): "final",  # Tabulador
    ("q50", "."): "final",   # Punto
    # ("q50", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q47","1"): "q51",
    ("q51","1"): "q52",
    ("q51","2"): "q52",
    ("q51","3"): "q52",
    ("q51","4"): "q52",
    ("q51","5"): "q52",
    ("q52","0"): "q53",
    ("q53", "\n"): "final",  # Salto de línea
    ("q53", "\r"): "final",  # Retorno de carro
    ("q53", "\t"): "final",  # Tabulador
    ("q53", "."): "final",   # Punto
    # ("q53", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q53"," "):"q54",
    ("q53","-"):"q54",
    ("q54","n"):"q55",
    ("q55"," "):"final", #Espacio Itanium 911 estado final aceptado
    ("q55", "\n"): "final",  # Salto de línea
    ("q55", "\r"): "final",  # Retorno de carro
    ("q55", "\t"): "final",  # Tabulador
    ("q55", "."): "final",   # Punto
    # ("q55", ""): "final",    # Fin de la cadena (cadena vacía)   
    ("q47","3"): "q56",
    ("q56","1"): "q57",
    ("q56","2"): "q57",
    ("q56","3"): "q57",
    ("q56","4"): "q57",
    ("q56","5"): "q57",
    ("q57","0"): "q58",
    ("q58"," "): "final", #Espacio Itanium 913 estado final aceptado
    ("q58", "\n"): "final",  # Salto de línea
    ("q58", "\r"): "final",  # Retorno de carro
    ("q58", "\t"): "final",  # Tabulador
    ("q58", "."): "final",   # Punto
    # ("q58", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q47","5"): "q59",
    ("q59","1"): "q60",
    ("q59","2"): "q60",
    ("q59","4"): "q60",
    ("q59","5"): "q60",
    ("q59","8"): "q60",
    ("q60","0"): "q61",
    ("q61"," "): "final", #Espacio Itanium 915 estado final aceptado
    ("q61", "\n"): "final",  # Salto de línea
    ("q61", "\r"): "final",  # Retorno de carro
    ("q61", "\t"): "final",  # Tabulador
    ("q61", "."): "final",   # Punto
    # ("q61", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q47","7"): "q62",
    ("q62","2"): "q63",
    ("q62","4"): "q63",
    ("q62","5"): "q63",
    ("q62","6"): "q63",
    ("q63","0"): "q64",
    ("q64"," "): "final", #Espacio Itanium 917 estado final aceptado
    ("q64", "\n"): "final",  # Salto de línea
    ("q64", "\r"): "final",  # Retorno de carro
    ("q64", "\t"): "final",  # Tabulador
    ("q64", "."): "final",   # Punto #ITANIUM FINALIZADO
    # ("q64", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q9","e"): "q65",
    ("q65","o"): "q66",
    ("q66","n"): "q67",
    ("q67"," "): "q68",
    ("q67","-"): "q68",
    ("q68","3"): "q69",
    ("q69","1"): "q70",
    ("q70","0"): "q71",
    ("q71","4"): "q72",
    ("q71","6"): "q72",
    ("q72"," "): "final", #Espacio Xeon 3104-3106 estado final aceptado
    ("q72", "\n"): "final",  # Salto de línea
    ("q72", "\r"): "final",  # Retorno de carro
    ("q72", "\t"): "final",  # Tabulador
    ("q72", "."): "final",   # Punto
    # ("q72", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q71","8"): "q73",   
    ("q73"," "): "final", #Espacio Xeon 3108 estado final aceptado
    ("q73", "\n"): "final",  # Salto de línea
    ("q73", "\r"): "final",  # Retorno de carro
    ("q73", "\t"): "final",  # Tabulador
    ("q73", "."): "final",   # Punto
    # ("q73", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q73","u"): "q74",
    ("q74"," "): "final", #Espacio Xeon 3108u estado final aceptado
    ("q74", "\n"): "final",  # Salto de línea
    ("q74", "\r"): "final",  # Retorno de carro
    ("q74", "\t"): "final",  # Tabulador
    ("q74", "."): "final",   # Punto
    # ("q74", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q69","2"): "q75",
    ("q75","0"): "q76",
    ("q76","4"): "q77",
    ("q77"," "): "final", #Espacio Xeon 3204 estado final aceptado
    ("q77", "\n"): "final",  # Salto de línea
    ("q77", "\r"): "final",  # Retorno de carro
    ("q77", "\t"): "final",  # Tabulador
    ("q77", "."): "final",   # Punto
    # ("q77", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q76","6"): "q78",
    ("q78"," "): "final", #Espacio Xeon 3206 estado final aceptado
    ("q78", "\n"): "final",  # Salto de línea
    ("q78", "\r"): "final",  # Retorno de carro
    ("q78", "\t"): "final",  # Tabulador
    ("q78", "."): "final",   # Punto
    # ("q78", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q78","r"): "q79",
    ("q69","4"): "q80",
    ("q69","5"): "q80", 
    ("q80","0"): "q81",
    ("q81","8"): "q73",
    ("q68","4"): "q82",
    ("q82","1"): "q83",
    ("q83","0"): "q84",
    ("q84","9"): "q85",
    ("q85"," "): "final", #Espacio Xeon 4109 estado final aceptado
    ("q85", "\n"): "final",  # Salto de línea
    ("q85", "\r"): "final",  # Retorno de carro
    ("q85", "\t"): "final",  # Tabulador
    ("q85", "."): "final",   # Punto
    # ("q85", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q85","t"): "q86",
    ("q86"," "): "final", #Espacio Xeon 4109t estado final aceptado
    ("q86", "\n"): "final",  # Salto de línea
    ("q86", "\r"): "final",  # Retorno de carro
    ("q86", "\t"): "final",  # Tabulador
    ("q86", "."): "final",   # Punto
    # ("q86", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q83","1"): "q87",
    ("q87","0"):"q88",
    ("q88"," "): "final", #Espacio Xeon 4110 estado final aceptado
    ("q88", "\n"): "final",  # Salto de línea
    ("q88", "\r"): "final",  # Retorno de carro
    ("q88", "\t"): "final",  # Tabulador
    ("q88", "."): "final",   # Punto
    # ("q88", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q87","4"):"q89",
    ("q87","6"):"q89",
    ("q89"," "): "final", #Espacio Xeon 411(4,6) estado final aceptado
    ("q89", "\n"): "final",  # Salto de línea
    ("q89", "\r"): "final",  # Retorno de carro
    ("q89", "\t"): "final",  # Tabulador
    ("q89", "."): "final",   # Punto
    # ("q89", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q89","t"):"q86",
    ("q82","2"):"q90",
    ("q90","0"):"q91",
    ("q91","8"): "q92", 
    ("q91","9"): "q92", 
    ("q92"," "): "final", #Espacio Xeon 4208-4209 estado final aceptado
    ("q92", "\n"): "final",  # Salto de línea
    ("q92", "\r"): "final",  # Retorno de carro
    ("q92", "\t"): "final",  # Tabulador
    ("q92", "."): "final",   # Punto
    # ("q92", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q92","t"):"q86",
    ("q90","1"):"q93",
    ("q93","0"):"q94",
    ("q93","4"):"q94",
    ("q93","5"):"q94",
    ("q93","6"):"q94",
    ("q94"," "): "final", #Espacio Xeon 4210-4216 estado final aceptado
    ("q94", "\n"): "final",  # Salto de línea
    ("q94", "\r"): "final",  # Retorno de carro
    ("q94", "\t"): "final",  # Tabulador
    ("q94", "."): "final",   # Punto
    # ("q94", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q94","r"):"q78",
    ("q82","3"):"q95",
    ("q95","1"):"q96",
    ("q96","0"):"q97",
    ("q96","4"):"q97", 
    ("q96","6"):"q97", 
    ("q97"," "): "final", #Espacio Xeon 4310-4316 estado final aceptado
    ("q97", "\n"): "final",  # Salto de línea
    ("q97", "\r"): "final",  # Retorno de carro
    ("q97", "\t"): "final",  # Tabulador
    ("q97", "."): "final",   # Punto
    # ("q97", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q97","t"):"q86",
    ("q82","4"):"q98",
    ("q98","1"):"q99",
    ("q99","0"):"q100",
    ("q99","6"):"q100",
    ("q100"," "): "final", #Espacio Xeon 4410-4416 estado final aceptado
    ("q100", "\n"): "final",  # Salto de línea
    ("q100", "\r"): "final",  # Retorno de carro
    ("q100", "\t"): "final",  # Tabulador
    ("q100", "."): "final",   # Punto
    # ("q100", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q100","y"):"q101",
    ("q101"," "): "final", #Espacio Xeon 4410-4416y estado final aceptado
    ("q101", "\n"): "final",  # Salto de línea
    ("q101", "\r"): "final",  # Retorno de carro
    ("q101", "\t"): "final",  # Tabulador
    ("q101", "."): "final",   # Punto
    ("q100","t"):"q86",
    ("q82","5"):"q102",
    ("q102","1"):"q103",
    ("q103","0"):"q104",
    ("q103","4"):"q104",
    ("q103","6"):"q104",
    ("q104"," "): "final", #Espacio Xeon 4510-4516 estado final aceptado
    ("q104", "\n"): "final",  # Salto de línea
    ("q104", "\r"): "final",  # Retorno de carro
    ("q104", "\t"): "final",  # Tabulador
    ("q104", "."): "final",   # Punto
    # ("q104", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q104","t"):"q86",
    ("q104","y"):"q101",
    ("q68","5"):"q105",
    ("q105","1"):"q106",
    ("q106","1"):"q107",
    ("q107","8"):"q108",
    ("q107","9"):"q108",
    ("q108"," "): "final", #Espacio Xeon 5118 estado final aceptado
    ("q108", "\n"): "final",  # Salto de línea
    ("q108", "\r"): "final",  # Retorno de carro
    ("q108", "\t"): "final",  # Tabulador
    ("q108", "."): "final",   # Punto
    # ("q108", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q108","t"):"q86",
    ("q106","2"):"q109",
    ("q109","0"):"q110",
    ("q110"," "): "final", #Espacio Xeon 5120 estado final aceptado
    ("q110", "\n"): "final",  # Salto de línea
    ("q110", "\r"): "final",  # Retorno de carro
    ("q110", "\t"): "final",  # Tabulador
    ("q110", "."): "final",   # Punto
    # ("q110", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q110","t"):"q86",
    ("q105","2"):"q111",
    ("q111","1"):"q112",
    ("q112","5"): "q113",
    ("q112","8"): "q113",
    ("q113"," "): "final", #Espacio Xeon 5215-5218 estado final aceptado
    ("q113", "\n"): "final",  # Salto de línea
    ("q113", "\r"): "final",  # Retorno de carro
    ("q113", "\t"): "final",  # Tabulador
    ("q113", "."): "final",   # Punto
    # ("q113", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q113","t"):"q86",
    ("q113","r"):"q79",
    ("q113","n"):"q114",
    ("q114"," "): "final", #Espacio Xeon 5215-5218n estado final aceptado
    ("q114", "\n"): "final",  # Salto de línea
    ("q114", "\r"): "final",  # Retorno de carro
    ("q114", "\t"): "final",  # Tabulador
    ("q114", "."): "final",   # Punto
    # ("q114", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q111","2"): "q115",
    ("q115","0"): "q116",
    ("q115","2"): "q116",
    ("q116","s"): "q117",
    ("q116"," "): "final", #Espacio Xeon 5220-5220s estado final aceptado
    ("q116", "\n"): "final",  # Salto de línea
    ("q116", "\r"): "final",  # Retorno de carro    
    ("q116", "\t"): "final",  # Tabulador
    ("q116", "."): "final",   # Punto
    # ("q116", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q117"," "): "final", #Espacio Xeon 5220-5220s estado final aceptado
    ("q117", "\n"): "final",  # Salto de línea
    ("q117", "\r"): "final",  # Retorno de carro
    ("q117", "\t"): "final",  # Tabulador
    ("q117", "."): "final",   # Punto
    # ("q117", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q105","3"):"q118",
    ("q118","1"):"q119",
    ("q119","5"):"q120",
    ("q119","7"):"q120",
    ("q119","8"):"q120",
    ("q120"," "): "final", #Espacio Xeon 5315-5318 estado final aceptado
    ("q120", "\n"): "final",  # Salto de línea
    ("q120", "\r"): "final",  # Retorno de carro
    ("q120", "\t"): "final",  # Tabulador
    ("q120", "."): "final",   # Punto
    # ("q120", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q120","y"):"q101",
    ("q120","n"):"q114",
    ("q120","s"): "q117",
    ("q120","h"): "q121",
    ("q121"," "): "final", #Espacio Xeon 5315-5318h estado final aceptado
    ("q121", "\n"): "final",  # Salto de línea
    ("q121", "\r"): "final",  # Retorno de carro
    ("q121", "\t"): "final",  # Tabulador
    ("q121", "."): "final",   # Punto
    # ("q121", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q118","2"):"q122",
    ("q122","0"):"q123",
    ("q123"," "): "final", #Espacio Xeon 5320 estado final aceptado
    ("q123", "\n"): "final",  # Salto de línea
    ("q123", "\r"): "final",  # Retorno de carro
    ("q123", "\t"): "final",  # Tabulador
    ("q123", "."): "final",   # Punto
    # ("q123", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q123","h"): "q121",
    ("q123","t"):"q86",
    ("q105","4"):"q124",
    ("q124","1"):"q125",
    ("q125","1"):"q126",
    ("q125","5"):"q126", 
    ("q125","6"):"q126", 
    ("q125","8"):"q126", 
    ("q126"," "): "final", #Espacio Xeon 5411-5418 estado final aceptado
    ("q126", "\n"): "final",  # Salto de línea
    ("q126", "\r"): "final",  # Retorno de carro
    ("q126", "\t"): "final",  # Tabulador
    ("q126", "."): "final",   # Punto
    # ("q126", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q126","n"):"q114",
    ("q126","s"):"q117",
    ("q126","t"):"q86",
    ("q124","2"):"q127",
    ("q124","3"):"q127",
    ("q127","3"):"q128",
    ("q128"," "): "final", #Espacio Xeon 5423 - 5433 estado final aceptado
    ("q128", "\n"): "final",  # Salto de línea
    ("q128", "\r"): "final",  # Retorno de carro
    ("q128", "\t"): "final",  # Tabulador
    ("q128", "."): "final",   # Punto
    # ("q128", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q128","n"):"q114",
    ("q105","5"): "q129", 
    ("q129","1"): "q130",
    ("q130","2"): "q131",
    ("q131"," "): "final", #Espacio Xeon 5122 estado final aceptado
    ("q131", "\n"): "final",  # Salto de línea
    ("q131", "\r"): "final",  # Retorno de carro
    ("q131", "\t"): "final",  # Tabulador
    ("q131", "."): "final",   # Punto
    # ("q131", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q131","u"): "q74",
    ("q130","5"): "q132",
    ("q132"," "): "final", #Espacio Xeon 5122 estado final aceptado
    ("q132", "\n"): "final",  # Salto de línea
    ("q132", "\r"): "final",  # Retorno de carro
    ("q132", "\t"): "final",  # Tabulador
    ("q132", "."): "final",   # Punto
    # ("q132", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q132","t"):"q86",
    ("q129","2"): "q133",
    ("q133","0"): "q134",
    ("q134"," "): "final", #Espacio Xeon 5220 estado final aceptado
    ("q134", "\n"): "final",  # Salto de línea
    ("q134", "\r"): "final",  # Retorno de carro
    ("q134", "\t"): "final",  # Tabulador
    ("q134", "."): "final",   # Punto
    # ("q134", ""): "final",    # Fin de la cadena (cadena vacía)
    ("q134","t"):"q86",
    
    
    
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}


estado_inicial = "q0"
estados_finales = {"final"}

# Crear el ADF
automata = ADF(estados, alfabeto, transiciones, estado_inicial, estados_finales)

# Procesar una cadena
cadena = "i3-10"
for simbolo in cadena:
    automata.procesar_simbolo(simbolo)
    if automata.estado_actual == "invalido":
        print(f"Cadena rechazada en el estado: {automata.estado_actual}")
        break

if automata.es_aceptado():
    print("Cadena aceptada.")
else:
    print("Cadena rechazada.")
