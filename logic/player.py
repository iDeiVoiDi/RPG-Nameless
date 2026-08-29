#============================================================
# Creacion del jugador
#============================================================

# | FUNCIONES |
# Preguntar_player → Pregunta al jugador su nombre y clase
# Pregunta_clase → Pregunta al jugador su clase y valida la respuesta
# Info_clase → Muestra la informacion de la clase seleccionada |GUI|
# Crear_personaje → Crea el objeto jugador con su nombre, clase y estadisticas base

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

# AUXILIAR pregunta para la clase del jugador y valida la respuesta
def pregunta_clase(texto_pregunta, texto_fallo):
    while True:
        print(texto_pregunta)
        clase = input("> ").lower()

        if clase in JUGADOR:
            return clase
        else:
            print(texto_fallo)
        
# Muestra la informacion de la clase seleccionada |GUI|
def info_clase(clase):
    print(TEXTOS["clases_info"][clase])
    #! ESTO MANDARA A LA GUI A PONER EN PANTALLA EL TEXTO Y A MOSTRAR SUS STATS
    
# Crea el objeto jugador con su nombre, clase y estadisticas base
def crear_personaje(nombre, clase):
    base = variar(JUGADOR[clase])
    return Entidad(nombre, True, clase, base)
