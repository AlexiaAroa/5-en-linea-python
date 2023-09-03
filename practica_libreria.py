import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 420
CELL_SIZE = 10

# def draw_arc():
#     gamelib.draw_arc(10, 10, 20, 20, outline='white', fill='red')

def juego_crear():
    """Inicializar el estado del juego"""
    # En las funciones juego_crear y juego_actualizar tenemos que manipular el estado del juego.
    # Esto es similar a lo que hicimos en el TP1, y no debería involucrar llamadas a funciones de Gamelib.
    grilla = []
    for i in range(10):
        grilla.append(list(' ' * 10))
    return grilla

def obtener_coordenadas_matriz(x, y):
    coor_1 = x
    coor_2 = y
    return coor_1, coor_2

def obtener_coordenadas_pixel(m1, m2):
    coor_pixel_1 = m1
    coor_pixel_2 = m2
    return coor_pixel_1, coor_pixel_2

def dibujar_cruz(coordenada_1, coordenada_2):
    gamelib.draw_line(0, 0, 0, 350, fill='white', width=1)

def juego_actualizar(juego, x, y):
    # En las funciones juego_crear y juego_actualizar tenemos que manipular el estado del juego.
    # Esto es similar a lo que hicimos en el TP1, y no debería involucrar llamadas a funciones de Gamelib.
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    return juego

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)

def main():
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    juego = juego_crear()


    gamelib.draw_begin()
    juego_mostrar(juego)

    

    #VERTICALES
    gamelib.draw_line(0, 0, 0, 350, fill='white', width=1) # este no se nota jeje
    gamelib.draw_line(30, 50, 30, 350, fill='white', width=1)
    gamelib.draw_line(60, 50, 60, 350, fill='white', width=1)
    gamelib.draw_line(90, 50, 90, 350, fill='white', width=1)
    gamelib.draw_line(120, 50, 120, 350, fill='white', width=1)
    gamelib.draw_line(150, 50, 150, 350, fill='white', width=1)
    gamelib.draw_line(180, 50, 180, 350, fill='white', width=1)
    gamelib.draw_line(210, 50, 210, 350, fill='white', width=1)
    gamelib.draw_line(240, 50, 240, 350, fill='white', width=1)
    gamelib.draw_line(270, 50, 270, 350, fill='white', width=1)
    gamelib.draw_line(300, 50, 300, 350, fill='white', width=1)

    #HORIZONTALES
    gamelib.draw_line(0, 50, 300, 50, fill='white', width=1)
    gamelib.draw_line(0, 80, 300, 80, fill='white', width=1)
    gamelib.draw_line(0, 110, 300, 110, fill='white', width=1)
    gamelib.draw_line(0, 140, 300, 140, fill='white', width=1)
    gamelib.draw_line(0, 170, 300, 170, fill='white', width=1)
    gamelib.draw_line(0, 200, 300, 200, fill='white', width=1)
    gamelib.draw_line(0, 230, 300, 230, fill='white', width=1)
    gamelib.draw_line(0, 260, 300, 260, fill='white', width=1)
    gamelib.draw_line(0, 290, 300, 290, fill='white', width=1)
    gamelib.draw_line(0, 320, 300, 320, fill='white', width=1)
    gamelib.draw_line(0, 350, 300, 350, fill='white', width=1)

    # gamelib.draw_oval(10, 10, 30, 20, outline='white', fill='red') # CIRCULO

    gamelib.draw_text('Turno: ', 150, 375)
    
    gamelib.draw_end()

    gamelib.wait(gamelib.EventType.KeyPress)


# gamelib.init(main)

print(juego_crear())