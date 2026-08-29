#============================================================
# Creacion de las entidades ya sean JUGADOR o ENEMIGO 
#============================================================

# Hacemos una clase para la entidad, esta sirve tanto para JUGADOR como para ENEMIGO
class Entidad:

    # Atrributos → | NOMBRE ej→ "iDeiVoiDi"       | PLAYER ej→ True                 | CLASE ej→ "mago"    | BASE ej→ JUGADOR["mago"]  |
    #              | Nombre del jugador o enemigo | True o False si es o no JUGADOR | Clase del JUG o ENE | Clase dentro de JUG o ENE |
    def __init__(self, nombre, player, clase, base):

        # Datos bases
        self.nombre = nombre
        self.clase = clase
        self.player = player
        self.vivo = True
        self.inventario = []

        # Estadisticas bases de la entidad
        self.hp = base["hp"]
        self.daño = base["daño"]
        self.defensa = base["defensa"]
        self.agilidad = base["agilidad"]
        self.mana = base["mana"]
        self.magia = base["magia"]
        self.critico = base["critico"]

        self.hp_max = base["hp"]
        self.mana_max = base["mana"]

        if player:
            self.exp = 0
            self.nivel = 1
            self.dinero = 0
            self.puntuacion = 0
            self.enemigos_derrotados = {}

        else:
            self.exp = base["exp"]
            self.dinero = base["dinero"]