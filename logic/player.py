#============================================================
# Creacion del jugador
#============================================================

from text.textos import cargar_textos
TEXTOS = cargar_textos()

from entity import Entidad
from stats import variar
from classes import JUGADOR

#Creacion del jugador con su nombre y calse
def preguntar_player():
    print(TEXTOS["presentacion"])
    print(TEXTOS["pedir_nombre"])
    nombre = input("> ")

    while not nombre.strip():
        print(TEXTOS["fallo_nombre"])
        nombre = input("> ")

    while True:
        clase = pregunta_clase(TEXTOS["pedir_clase"], TEXTOS["fallo_clase"])
        info_clase(clase)

        confirmar = input(TEXTOS["confirmar_clase"].format(clase=clase) + " > ").lower()
        if confirmar in ("si", "sí", "s"):
            return nombre, clase

def pregunta_clase(texto_pregunta, texto_fallo):
    while True:
        print(texto_pregunta)
        clase = input("> ").lower()

        if clase in JUGADOR:
            return clase
        else:
            print(texto_fallo)
        

def info_clase(clase):
    print(TEXTOS["clases_info"][clase])
    #! ESTO MANDARA A LA GUI A PONER EN PANTALLA EL TEXTO Y A MOSTRAR SUS STATS
    

def crear_personaje(nombre, clase):
    base = variar(JUGADOR[clase])
    return Entidad(nombre, True, clase, base)