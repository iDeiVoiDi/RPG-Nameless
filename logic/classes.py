#============================================================
# Creacion de las clases y estadisticas bases
#============================================================

# | EJEMPLO |
# "clase": { "hp": X, "daño": X, "defensa": X, "agilidad": X, "magia": X, "mana": X, "critico": X, "lvl": ENE, "exp": ENE, "dinero": ENE }

# HP → Vida                         | DAÑO → Daño                  | Defensa → Reduccion del daño  | 
# AGILIDAD → Posibilidad de esquive | MAGIA → Daño de la magia     | MANA → Puntos para usar magia |
# CRITICO → Multiplicador 

# |ENEMIGOS| 
# LVL → Nivel del JUGADOR a partir del que aparece        | EXP → Experiencia que suelta | DINERO → Dinero que suelta    |

JUGADOR = {
    "guerrero": { "hp": 12, "daño":  6, "defensa":  5, "agilidad": 3, "magia": 2, "mana": 5, "critico": 1.5  },
    "arquero":  { "hp":  7, "daño":  8, "defensa":  4, "agilidad": 8, "magia": 3, "mana": 5, "critico": 1.75 },
    "asesino":  { "hp":  5, "daño": 10, "defensa":  3, "agilidad": 9, "magia": 3, "mana": 3, "critico": 2.0  },
    "mago":     { "hp": 10, "daño":  3, "defensa":  4, "agilidad": 4, "magia": 7, "mana": 7, "critico": 1.5  },
    "tanque":   { "hp": 15, "daño":  5, "defensa": 10, "agilidad": 2, "magia": 1, "mana": 1, "critico": 1.25 }
}

ENEMIGOS = {
    "trasgo":       { "hp":  4, "daño":  2, "defensa":  2, "agilidad": 2, "magia": 0, "mana":  0, "critico": 1.2 , "lvl":  1, "exp":  3, "dinero": 0 },
    "diablillo":    { "hp":  7, "daño":  4, "defensa":  3, "agilidad": 3, "magia": 4, "mana":  5, "critico": 1.3, "lvl":  5, "exp":  5, "dinero": 2 },
    "necomante":    { "hp":  6, "daño":  3, "defensa":  3, "agilidad": 4, "magia": 5, "mana":  7, "critico": 1.3 , "lvl": 10, "exp": 10, "dinero": 3 },
    "dragon_joven": { "hp":  8, "daño":  5, "defensa":  5, "agilidad": 4, "magia": 5, "mana": 10, "critico": 1.3 , "lvl": 12, "exp": 20, "dinero": 7 },
    "golem":        { "hp": 12, "daño":  6, "defensa": 10, "agilidad": 2, "magia": 1, "mana":  1, "critico": 1.2, "lvl": 14, "exp": 25, "dinero": 8 }
}

