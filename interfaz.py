import gamelib
import interfaz
from constantes import DISTANCIA_CELDA, TAMANIO_CELDA, ANCHO_PIXELES_GRILLA, INICIO_GRILLA, FINAL_GRILLA, ANCHO_VENTANA, ALTO_VENTANA, CRUZ, CIRCULO
from five_in_line import obtener_coordenadas_pixel

def dibujar_cruz(x1, y1):
    """Dibuja una cruz en la celda donde el usuario hizo click."""
    gamelib.draw_line(x1 + DISTANCIA_CELDA, y1 + DISTANCIA_CELDA, x1 + TAMANIO_CELDA - DISTANCIA_CELDA, y1 + TAMANIO_CELDA - DISTANCIA_CELDA, fill='white', width=1) 
    gamelib.draw_line(x1 + DISTANCIA_CELDA, y1 + TAMANIO_CELDA - DISTANCIA_CELDA, x1 + TAMANIO_CELDA - DISTANCIA_CELDA, y1 + DISTANCIA_CELDA, fill='white', width=1)

def dibujar_circulo(x1, y1):
    """Dibuja un círculo en la celda donde el usuario hizo click."""
    gamelib.draw_oval(x1 + DISTANCIA_CELDA, y1 + DISTANCIA_CELDA, x1 + TAMANIO_CELDA - DISTANCIA_CELDA, y1 + TAMANIO_CELDA - DISTANCIA_CELDA, outline='white', fill='black')

def dibujar_grilla():
    """Dibuja la grilla del juego."""
    #Líneas verticales
    for i in range(0, ANCHO_PIXELES_GRILLA + 1, TAMANIO_CELDA):
        gamelib.draw_line(i, INICIO_GRILLA, i, FINAL_GRILLA, fill='white', width=1)

    #Líneas horizontales
    for i in range(INICIO_GRILLA, FINAL_GRILLA + 1, TAMANIO_CELDA):
        gamelib.draw_line(0, i, ANCHO_VENTANA, i, fill='white', width=1)

def juego_mostrar(juego):
    """Actualizar la ventana."""
    grilla, jugador = juego
    gamelib.draw_text('5 en línea', ANCHO_VENTANA // 2, INICIO_GRILLA // 2)
    gamelib.draw_text(f'Turno: {jugador}', ANCHO_VENTANA // 2, (FINAL_GRILLA + ALTO_VENTANA) // 2)
    dibujar_grilla()

    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            x, y = obtener_coordenadas_pixel(j, i)

            if grilla[i][j] == CRUZ:
                interfaz.dibujar_cruz(x, y)
            elif grilla[i][j] == CIRCULO:    
                interfaz.dibujar_circulo(x, y)
