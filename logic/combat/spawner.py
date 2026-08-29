import random
from logic.combat.variants import VARIANTES

#! EDITAR EN EL FUTURO
def elegir_variante():
    r = random.random()
    acumulado = 0
    for nombre, datos in VARIANTES.items():
        acumulado += datos["prob"]
        if r < acumulado:
            return nombre
    return "normal"