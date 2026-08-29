#============================================================
# Variantes posibles de enemigos, cada una con sus multiplicadores y probabilidad de aparición
#============================================================

# | EJEMPLO |
# "variante": { "multiplicadores": { X }, "prob": X }

VARIANTES = {
    "normal": {
        "multiplicadores": {},
        "prob": 0.90,
    },
    "plata": {
        "multiplicadores": {"defensa": 1.4, "exp": 1.3},
        "prob": 0.07,
    },
    "oro": {
        "multiplicadores": {"dinero": 3.0},
        "prob": 0.02,
    },
    "arcano": {
        "multiplicadores": {"magia": 1.6, "mana": 1.3},
        "prob": 0.01,
    },
}