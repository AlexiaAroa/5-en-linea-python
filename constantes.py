ALTO_GRILLA = 10 # Cantidad de celdas de alto que hay en la grilla 
ANCHO_GRILLA = 10 # cantidad de celdas de ancho que hay en la grilla

TAMANIO_CELDA = 30 # Tamaño de la celda en píxeles



# TODO: Yo recomendaría hacer esta constante en función a TAMANIO_CELDA, para que al cambiarla también las X y O escalen!
DISTANCIA_CELDA = 7 # Distancia de los símbolos ('X', 'O') en píxeles respecto de la celda



INICIO_GRILLA = TAMANIO_CELDA # Pixel en el que inicia la grilla

ALTURA_PIXELES_GRILLA = TAMANIO_CELDA * ALTO_GRILLA # Altura de la grilla en píxeles
ANCHO_PIXELES_GRILLA = TAMANIO_CELDA * ANCHO_GRILLA # Ancho de la grilla en píxeles

FINAL_GRILLA = INICIO_GRILLA + ALTURA_PIXELES_GRILLA  # Pixel en el que termina la grilla

ANCHO_VENTANA = TAMANIO_CELDA * ANCHO_GRILLA # Ancho de la ventana en píxeles
ALTO_VENTANA = INICIO_GRILLA * 2 + ALTURA_PIXELES_GRILLA # Alto de la ventana en píxeles

CRUZ = 'X'
CIRCULO = 'O'
VACIO = ''
