#============================================================
# Cargador de los textos
#============================================================

import json

def cargar_textos(ruta="text/textos.json"):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)