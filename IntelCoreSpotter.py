class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_actual = estado_inicial
        self.estados_finales = estados_finales
        self.buffer = "" 
        self.cadena_larga = "" 
        self.posiciones = []  

    def procesar_simbolo(self, simbolo, fila, columna):
        if simbolo in self.alfabeto and (self.estado_actual, simbolo) in self.transiciones:
            self.estado_actual = self.transiciones[(self.estado_actual, simbolo)]
            self.buffer += simbolo

           
            if self.estado_actual in self.estados_finales:
                self.cadena_larga = self.buffer

        else:
           
            if self.cadena_larga:
                self.posiciones.append((fila, columna - len(self.cadena_larga), self.cadena_larga))
                print(f"Cadena válida encontrada: {self.cadena_larga} en fila {fila}, columna {columna - len(self.cadena_larga)}")
            self.reiniciar()  # Reiniciar el autómata

    def es_aceptado(self):
        return self.estado_actual in self.estados_finales

    def reiniciar(self):
        self.estado_actual = "q0" 
        self.buffer = ""
        self.cadena_larga = "" 



#componentes del AFD

estados = {
    "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", 
    "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", 
    "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39", 
    "q40", "q41", "q42", "q43", "q44", "q45", "q46", "q47", "q48", "q49", "q50", "q51", "q52", 
    "q53", "q54", "q55", "q56", "q57", "q58", "q59", "q60", "q61", "q62", "q63", "q64", "q65", 
    "q66", "q67", "q68", "q69", "q70", "q71", "q72", "q73", "q74", "q75", "q76", "q77", "q78", 
    "q79", "q80", "q81", "q82", "q83", "q84", "q85", "q86", "q87", "q88", "q89", "q90", "q91", 
    "q92", "q93", "q94", "q95", "q96", "q97", "q98", "q99", "q100", "q101", "q102", "q103", 
    "q104", "q105", "q106", "q107", "q108", "q109", "q110", "q111", "q112", "q113", "q114", 
    "q115", "q116", "q117", "q118", "q119", "q120", "q121", "q122", "q123", "q124", "q125", 
    "q126", "q127", "q128", "q129", "q130", "q131", "q132", "q133", "q134","invalido"
}

alfabeto = set("intelxeoncoreitanium- 0123456789kfutghqnsry") 

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
    ("q21", "t"): "q19",
    ("q22", "0"): "q23",  # Primera generacion de procesadores IX validada, estado final :
    ("q22", "5"): "q23",  # Primera generacion de procesadores IX validada, estado final :
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
    ("q25", "0"): "q29", # Procesadores con el siguiente formato valido : ix GeneracionModelo Ejemplo i5-10400
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
    ("q26","t"):"q19",
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
    ("q28","5"): "q29",  # Procesadores con el siguiente formato valido : ix GeneracionModelo Ejemplo i5-10400
    ("q29","k"): "q30",
    ("q29","f"): "q30",
    ("q29","u"): "q30",
    ("q29","t"): "q30",
    ("q29","g"): "q30", # Procesadores con el siguiente formato valido : ix GeneracionModeloSufijo  Ejemplo i5-10400K
    ("q29","h"): "q31", # Procesadores con el siguiente formato valido : ix GeneracionModeloSufijoH  Ejemplo i5-10400H
    ("q31","q"): "q32",# Procesadores con el siguiente formato valido : ix GeneracionModeloSufijoHQ  Ejemplo i5-10400HQ
    ("q15","a"): "q33",
    ("q33","n"): "q34",
    ("q34","i"): "q35", 
    ("q35","u"): "q36",
    ("q36","m"): "q37",
    ("q37"," "): "q38",
    ("q38","2"): "q39",
    ("q39"," "): "q40",
    ("q39","-"): "q40",
    ("q40","9"): "q41", #Itanium 2-9 estado final aceptado, exemplo los itanium 2 9 son una generacion de procesadores ...
    ("q41","0"): "q42",
    ("q42","0"): "q43", #Itanium 2 900 estado final aceptado ejemplo, 2 900 es un modelo de procesador, se refiere a 900 mhz
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
    ("q45","9"): "q46", #Itanium 2 4.5 estado final aceptado, ejemplo 2 0.5 es un modelo de procesador, se refiere a 4.5 ghz
    ("q38","9"): "q47",
    ("q47","0"): "q48",
    ("q48","1"): "q49",
    ("q48","2"): "q49",
    ("q48","3"): "q49",
    ("q48","4"): "q49",
    ("q48","5"): "q49",
    ("q49","0"): "q50", #Itanium 90(1-5)0 estado final aceptado
    ("q47","1"): "q51",
    ("q51","1"): "q52",
    ("q51","2"): "q52",
    ("q51","3"): "q52",
    ("q51","4"): "q52",
    ("q51","5"): "q52",
    ("q52","0"): "q53", #Itanium 91(1-5)0 estado final aceptado
    ("q53"," "):"q54",
    ("q53","-"):"q54",
    ("q54","n"):"q55", #Itanium 91(1-5)0N estado final aceptado con sufijo N
    ("q47","3"): "q56",
    ("q56","1"): "q57",
    ("q56","2"): "q57",
    ("q56","3"): "q57",
    ("q56","4"): "q57",
    ("q56","5"): "q57",
    ("q57","0"): "q58", #Itanium 93(1-5)0 estado final aceptado
    ("q47","5"): "q59",
    ("q59","1"): "q60",
    ("q59","2"): "q60",
    ("q59","4"): "q60",
    ("q59","5"): "q60",
    ("q59","8"): "q60",
    ("q60","0"): "q61", #Itanium 95(1,2,4,6,8)0 estado final aceptado
    ("q47","7"): "q62",
    ("q62","2"): "q63",
    ("q62","4"): "q63",
    ("q62","5"): "q63",
    ("q62","6"): "q63",
    ("q63","0"): "q64", #Itanium 97(2,4,5,6)0 estado final aceptado
    ("q9","e"): "q65",
    ("q65","o"): "q66",
    ("q66","n"): "q67",
    ("q67"," "): "q68",
    ("q67","-"): "q68",
    ("q68","3"): "q69",
    ("q69","1"): "q70",
    ("q70","0"): "q71",
    ("q71","4"): "q72",
    ("q71","6"): "q72", #Xeon 3104-3106 estado final aceptado
    ("q71","8"): "q73", #Xeon 3108 estado final aceptado
    ("q73","u"): "q74", #Xeon 3108u estado final aceptado
    ("q69","2"): "q75",
    ("q75","0"): "q76",
    ("q76","4"): "q77", #Xeon 3204 estado final aceptado
    ("q76","6"): "q78", #Xeon 3206 estado final aceptado
    ("q78","r"): "q79", #Xeon 3206r estado final aceptado
    ("q69","4"): "q80",
    ("q69","5"): "q80", 
    ("q80","0"): "q81",
    ("q81","8"): "q73", #Xeon 3408 O 3508 O con sufijo r estados finales aceptados
    ("q68","4"): "q82",
    ("q82","1"): "q83",
    ("q83","0"): "q84",
    ("q84","9"): "q85", # Xeon 4109 estado final aceptado
    ("q85","t"): "q86", # Xeon 4109t estado final aceptado
    ("q83","1"): "q87",
    ("q87","0"):"q88", # Xeon 4110 estado final aceptado
    ("q87","4"):"q89", # Xeon 4114 estado final aceptado
    ("q87","6"):"q89",  # Xeon 4116 estado final aceptado
    ("q89","t"):"q86", # Xeon 4114t O 4116t estado final aceptado
    ("q82","2"):"q90",
    ("q90","0"):"q91",
    ("q91","8"): "q92", 
    ("q91","9"): "q92", # Xeon 4208 O 4209 estado final aceptado
    ("q92","t"):"q86",
    ("q90","1"):"q93",
    ("q93","0"):"q94",
    ("q93","4"):"q94",
    ("q93","5"):"q94",
    ("q93","6"):"q94", # Xeon 4210, 4214, 4215, 4216 estado final aceptado
    ("q94","r"):"q78", # Xeon 4210r, 4214r, 4215r, 4216r estado final aceptado
    ("q82","3"):"q95",
    ("q95","1"):"q96",
    ("q96","0"):"q97", # Xeon 4310,estado final aceptado
    ("q96","4"):"q97", # Xeon 4314 estado final aceptado
    ("q96","6"):"q97", # Xeon 4316 estado final aceptado
    ("q97","t"):"q86", # Xeon 4310t, 4314t, 4316t estado final aceptado
    ("q82","4"):"q98", 
    ("q98","1"):"q99",
    ("q99","0"):"q100", # Xeon 4410 estado final aceptado
    ("q99","6"):"q100", # Xeon 4416 estado final aceptado
    ("q100","y"):"q101", # Xeon  4410y,4416y estado final aceptado
    ("q100","t"):"q86", # Xeon   4410t,4416t estado final aceptado
    ("q82","5"):"q102",
    ("q102","1"):"q103",
    ("q103","0"):"q104", # Xeon 4510 estado final aceptado
    ("q103","4"):"q104", # Xeon 4514 estado final aceptado
    ("q103","6"):"q104", # Xeon 4516 estado final aceptado
    ("q104","t"):"q86", # Xeon 4510t,4514t,4516t estado final aceptado
    ("q104","y"):"q101", # Xeon 4510y,4514y,4516y estado final aceptado
    ("q68","5"):"q105", 
    ("q105","1"):"q106",
    ("q106","1"):"q107",
    ("q107","8"):"q108",
    ("q107","9"):"q108", # Xeon 5118, 5119 estado final aceptado
    ("q108","t"):"q86", # Xeon 5118t, 5119t estado final aceptado
    ("q106","2"):"q109",
    ("q109","0"):"q110", # Xeon 5120 estado final aceptado
    ("q110","t"):"q86", # Xeon 5120t estado final aceptado
    ("q105","2"):"q111",
    ("q111","1"):"q112",
    ("q112","5"): "q113", # Xeon 5215 estado final aceptado
    ("q112","8"): "q113", # Xeon 5218 estado final aceptado
    ("q113","t"):"q86", # Xeon 5215t, 5218t estado final aceptado
    ("q113","r"):"q79", # Xeon 5215r, 5218r estado final aceptado
    ("q113","n"):"q114", # Xeon 5215n, 5218n estado final aceptado
    ("q111","2"): "q115",
    ("q115","0"): "q116", # Xeon 5220 estado final aceptado
    ("q115","2"): "q116", # Xeon 5222 estado final aceptado
    ("q116","s"): "q117", # Xeon 5220s, 5222s estado final aceptado
    ("q105","3"):"q118",
    ("q118","1"):"q119",
    ("q119","5"):"q120", # Xeon 5315 estado final aceptado
    ("q119","7"):"q120", # Xeon 5317 estado final aceptado
    ("q119","8"):"q120", # Xeon 5318 estado final aceptado
    ("q120","y"):"q101", # Xeon 5315y, 5317y, 5318y estado final aceptado
    ("q120","n"):"q114", # Xeon 5315n, 5317n, 5318n estado final aceptado
    ("q120","s"): "q117", # Xeon 5315s, 5317s, 5318s estado final aceptado
    ("q120","h"): "q121", # Xeon 5315h, 5317h, 5318h estado final aceptado
    ("q118","2"):"q122",
    ("q122","0"):"q123", # Xeon 5320 estado final aceptado
    ("q123","h"): "q121", # Xeon 5320h estado final aceptado
    ("q123","t"):"q86", # Xeon 5320t estado final aceptado
    ("q105","4"):"q124",
    ("q124","1"):"q125",
    ("q125","1"):"q126", # Xeon 5411 estado final aceptado
    ("q125","5"):"q126", # Xeon 5415 estado final aceptado
    ("q125","6"):"q126",  # Xeon 5416 estado final aceptado
    ("q125","8"):"q126",  # Xeon 5418 estado final aceptado
    ("q126","n"):"q114", # Xeon 5411n, 5415n, 5416n, 5418n estado final aceptado
    ("q126","s"):"q117", # Xeon 5411s, 5415s, 5416s, 5418s estado final aceptado
    ("q126","t"):"q86", # Xeon 5411t, 5415t, 5416t, 5418t estado final aceptado
    ("q124","2"):"q127", 
    ("q124","3"):"q127",
    ("q127","3"):"q128", # Xeon 5423, 5433 estado final aceptado
    ("q128","n"):"q114", # Xeon 5423n, 5433n estado final aceptado
    ("q105","5"): "q129", 
    ("q129","1"): "q130",
    ("q130","2"): "q131", # Xeon 5512 estado final aceptado
    ("q131","u"): "q74", # Xeon 5512u estado final aceptado
    ("q130","5"): "q132", # Xeon 5515 estado final aceptado
    ("q132","t"):"q86", # Xeon 5515t estado final aceptado
    ("q129","2"): "q133",
    ("q133","0"): "q134", # Xeon 5520 estado final aceptado
    ("q134","t"):"q86", # Xeon 5520t estado final aceptado   
}


estado_inicial = "q0"
estados_finales = {"q16","q20","q23","q29","q30","q31","q32","q41","q43","q46","q50","q53","q55", "q58","q61","q64","q72","q73","q74","q77","q78","q79","q85","q86","q88","q89","q92","q94","q97","q100","q101","q104","q108","q110","q113","q114","q116","q117","q120","q121","q123","q126","q128","q131","q132","q134"}


automata = AFD(estados, alfabeto, transiciones, estado_inicial, estados_finales)

# # Procesar una cadena
# cadena = "i3 9th"
# for simbolo in cadena:
#     automata.procesar_simbolo(simbolo.lower(), 1, cadena.index(simbolo))
# if automata.es_aceptado():
#     print("Cadena aceptada:", automata.buffer)
# else:
#     print("Cadena rechazada.")
