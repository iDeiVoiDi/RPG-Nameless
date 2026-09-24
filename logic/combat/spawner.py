#============================================================
# Creacion de los enemigos con su nivel y variante
#============================================================

# | FUNCIONES |
# Elegir_variante → Se elige una variante random
# Elegir_clase → Se elige una clase de enemigo que sea igual o menor al nivel del jugador
# Elegir_nivel → Se elige un nivel de enemigo que sea igual o menor al nivel del jugador
# Crear_enemigo → Crea un enemigo con su clase, nivel y variante

import random
from logic.combat.variants import VARIANTES
from logic.classes import ENEMIGO
from logic.stats import aplicar_variante, variar, escalar_por_nivel, escalar_recompensas
from logic.entity import Entidad

# Se elige una variante random
def elegir_variante():
    r = random.random()
    acumulado = 0
    for nombre, datos in VARIANTES.items():
        acumulado += datos["prob"] 
        if r < acumulado: # r=0.08 → acumulado=0.06 ✘ → acumulado=0.09 ✔ solo hubo 3%
            return nombre  
    return "normal"

# Se elige una clase de enemigo que sea igual o menor al nivel del jugador
def elegir_clase(nivel_jugador):
    posibles = [nombre for nombre, datos in ENEMIGO.items() if nivel_jugador >= datos["lvl"]]
    if posibles:
        return random.choice(posibles)
    return "trasgo"

# Se elige un nivel de enemigo que sea igual o menor al nivel del jugador
def elegir_nivel(nivel_jugador):
    margen = 2 # Edita los niveles de diferencia que puede tener el enemigo respecto al jugador

    return random.randint(max(1, nivel_jugador - margen), nivel_jugador)

# Crea un enemigo con su clase, nivel y variante
def crear_enemigo(nivel_jugador):
    clase = elegir_clase(nivel_jugador)
    nivel = elegir_nivel(nivel_jugador)
    variante = elegir_variante()
    
    base = variar(ENEMIGO[clase])
    base = escalar_por_nivel(base, nivel)
    base = escalar_recompensas(base, nivel)
    base = aplicar_variante(base, VARIANTES[variante])

    if variante != "normal":
        nombre = f"{clase.capitalize()}: {variante.capitalize()}"
    else:
        nombre = clase.capitalize() 

    return Entidad(nombre, False, clase, base)
    
    

