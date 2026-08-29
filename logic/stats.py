#============================================================
# Variacion de estadisticas
#============================================================

import random

STATS_COMBATE = ["hp", "daño", "defensa", "agilidad", "magia", "mana", "critico"]
RECOMPENSAS   = ["exp", "dinero"]

# 'base' es el diccionario de estadisticas base ejemplo JUGADOR["mago"] o ENEMIGO["golem"]

# Variacion de las estadisticas bases
# 'margen' es el porcentaje de variacion, por defecto es 0.1 (10%)
def variar(base, margen=0.1):
    resultado = dict(base)
    for k in STATS_COMBATE:
        if k in resultado:
            resultado[k] = round(resultado[k] * random.uniform(1 - margen, 1 + margen), 2)
    return resultado

# Escalado de estadisticas por nivel
# 'factor' es el porcentaje de escalado por nivel, por defecto es 0.08 (8%)
def escalar_por_nivel(base, nivel, factor=0.08):
    escala = 1 + (nivel - 1) * factor
    resultado = dict(base)
    for k in STATS_COMBATE:
        if k in resultado:
            resultado[k] = round(resultado[k] * escala, 2)
    return resultado

# Escalado de recompensas por nivel solo para ENEMIGOS
# ↓'factor' es el porcentaje de escalado por nivel, por defecto es 0.08 (8%)
# | Varia con las variantes de logic/combat/variants.py
def escalar_recompensas(base, nivel, factor=0.08):
    escala = 1 + (nivel - 1) * factor
    resultado = dict(base)
    for k in RECOMPENSAS:
        if k in resultado:
            resultado[k] = round(resultado[k] * escala)
    return resultado

# Funciones para manejar la experiencia y el nivel de una entidad
def ganar_exp(entidad, cantidad, base):
    entidad.exp += cantidad
    # Subir de nivel si la experiencia supera el umbral
    while entidad.exp >= exp_para_nivel(entidad.nivel + 1):
        entidad.exp -= exp_para_nivel(entidad.nivel + 1)
        subir_nivel(entidad, base)

# Calculo de experiencia necesaria para subir de nivel
# 'base' es la experiencia base para el primer nivel, por defecto es 30
def exp_para_nivel(nivel, base=30, exponente=1.25):
    return int(base * (nivel ** exponente))

# Función para subir de nivel a una entidad
def subir_nivel(entidad, base):
    entidad.nivel += 1
    nuevas = escalar_por_nivel(base, entidad.nivel)
    entidad.hp_max = nuevas["hp"]
    entidad.mana_max = nuevas["mana"]
    entidad.daño = nuevas["daño"]
    entidad.defensa = nuevas["defensa"]
    entidad.agilidad = nuevas["agilidad"]
    entidad.magia = nuevas["magia"]
    entidad.critico = nuevas["critico"]

    entidad.hp = entidad.hp_max
    entidad.mana = entidad.mana_max

# Función para aplicar una variante a las estadísticas de un ENEMIGO
def aplicar_variante(base, datos_variante):
    resultado = dict(base)
    for stat, mult in datos_variante["multiplicadores"].items():
        if stat in resultado:
            resultado[stat] = round(resultado[stat] * mult, 2)
    return resultado
