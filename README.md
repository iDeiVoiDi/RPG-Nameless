RPG/
├── main.py                    # Arranca Pygame, bucle principal, llama al game_manager
├── requirements.txt
├── README.md
├── utils.py                   # Helpers genéricos (cargar imágenes/sonidos, funciones auxiliares)
│
├── core/                      # NUEVO — orquestación del flujo del juego
│   ├── __init__.py
│   └── game_manager.py        # Máquina de estados: menú → creación personaje → mapa → combate
│
├── logic/
│   ├── __init__.py
│   ├── entity.py               # Clase base Entity: hp, nivel, stats, nombre, recibir_daño(), etc.
│   ├── player.py                # Player(Entity) + lógica de creación/selección de personaje
│   ├── clases.py                 # Clases concretas: Guerrero, Mago, tipos de enemigo, heredan de Entity
│   ├── stats.py                   # Cálculo/actualización de stats según clase y nivel
│   │
│   ├── attacks/
│   │   ├── __init__.py
│   │   └── ...                       # Cada ataque o categoría de ataque como módulo/clase
│   │
│   ├── combat/
│   │   ├── __init__.py
│   │   ├── variants.py                  # Variantes de los enemigos
│   │   ├── battle.py                    # Motor de combate: orden de turnos, aplicar daño, victoria/derrota
│   │   └── spawner.py                   # NUEVO — decide qué enemigo puede salir según nivel/zona
│   │
│   └── map/
│       ├── __init__.py
│       └── ...                          # Zonas/mapas, qué encuentros hay en cada una
│
├── gui/
│   ├── __init__.py
│   ├── screens/
│   │   ├── menu_screen.py                # Pantalla de menú principal
│   │   ├── character_creation_screen.py  # Pantalla de creación de personaje
│   │   ├── map_screen.py                 # Pantalla de exploración/mapa
│   │   └── battle_screen.py              # Pantalla de combate
│   └── widgets/
│       ├── hp_bar.py                     # Barra de HP reutilizable
│       └── battle_menu.py                # Menú de selección de ataque/objeto/huir
│
├── assets/                    # NUEVO — sprites, fuentes, sonidos (sácalo de gui/)
│
├── text/
│   ├── __init__.py
│   └── ...                    # Diálogos, nombres de ataques, textos de eventos
│
└── tests/                     # NUEVO (opcional) — tests de logic/ sin abrir ventana