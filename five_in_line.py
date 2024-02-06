from constantes import ANCHO_GRILLA, ALTO_GRILLA, TAMANIO_CELDA, INICIO_GRILLA, CRUZ, CIRCULO, VACIO

def juego_crear():
    """Inicializar el estado del juego: devuelve una grilla vacía y el turno del jugador."""
    return [[VACIO for _ in range(ANCHO_GRILLA)] for _ in range(ALTO_GRILLA)], CIRCULO

def obtener_coordenadas_matriz(x, y):
    """Recibe coordenadas en píxeles y devuelve coordenadas adaptadas a la matriz."""
    columna, fila = x // TAMANIO_CELDA, (y - INICIO_GRILLA) // TAMANIO_CELDA
    return columna, fila

def obtener_coordenadas_pixel(columna, fila):
    """Recibe coordenadas de la matriz y devuelve coordenadas adaptadas en píxeles."""
    return columna * TAMANIO_CELDA, fila * TAMANIO_CELDA + INICIO_GRILLA

def actualizar_turno(jugador):
    """Actualiza el turno del jugador."""
    return CRUZ if jugador == CIRCULO else CIRCULO

def movimiento_es_valido(juego, x, y):
    '''Devuelve True si la posición donde se hizo click es una celda vacía de la grilla.'''
    columna, fila = obtener_coordenadas_matriz(x, y)
    toca_linea_vertical = x % TAMANIO_CELDA == 0
    toca_linea_horizontal = (y - INICIO_GRILLA) % TAMANIO_CELDA == 0
    return not toca_linea_vertical and not toca_linea_horizontal and esta_dentro_de_la_grilla(fila, columna) and juego[fila][columna] == VACIO

def esta_dentro_de_la_grilla(fila, columna):
    return 0 <= columna < ANCHO_GRILLA and 0 <= fila < ALTO_GRILLA

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    grilla, jugador = juego
    if movimiento_es_valido(grilla, x, y):
        columna, fila = obtener_coordenadas_matriz(x, y)
        grilla[fila][columna], jugador = jugador, actualizar_turno(jugador)
    
    return grilla, jugador
