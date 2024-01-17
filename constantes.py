ALTO_GRILLA = 10 # Cantidad de celdas de alto que hay en la grilla 
ANCHO_GRILLA = 15 # cantidad de celdas de ancho que hay en la grilla

TAMANIO_CELDA = 30 # Tamaño de la celda en píxeles

DISTANCIA_CELDA = TAMANIO_CELDA // 5 # Distancia de los símbolos ('X', 'O') en píxeles respecto de la celda



INICIO_GRILLA = 50 # Pixel en el que inicia la grilla

ALTURA_PIXELES_GRILLA = TAMANIO_CELDA * ALTO_GRILLA # Altura de la grilla en píxeles
ANCHO_PIXELES_GRILLA = TAMANIO_CELDA * ANCHO_GRILLA # Ancho de la grilla en píxeles

FINAL_GRILLA = INICIO_GRILLA + ALTURA_PIXELES_GRILLA  # Pixel en el que termina la grilla

ANCHO_VENTANA = TAMANIO_CELDA * ANCHO_GRILLA # Ancho de la ventana en píxeles
ALTO_VENTANA = INICIO_GRILLA * 2 + ALTURA_PIXELES_GRILLA # Alto de la ventana en píxeles

CRUZ = 'X'
CIRCULO = 'O'
VACIO = ''
