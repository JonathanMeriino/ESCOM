"""
un click izquierdo para que una celda 0, pase a 1
un click derecho para que una celda 1, pase a 0
Barra espaciadora se pone pausa

"""
# Bibliotecas
import pygame
import numpy as np
import time

from pygame.constants import K_ESCAPE

pygame.init()

# Ancho y alto de la pantalla.
ancho=600
alto = 600

# Creación de la pantalla.
pantalla = pygame.display.set_mode((alto, ancho))

# color del fondo
pantalla.fill((200,0,0))
#tamaño del arreglo
nxC, nyC = 25, 25

dimCW = ancho / nxC
dimCH = alto / nyC

# Estado de las celdas. Viva = 1 Muere = 0.
gameState = np.zeros((nxC, nyC))

#Estados

gameState[11, 11] = 1
gameState[12, 12] = 1
gameState[12, 13] = 1
gameState[11, 13] = 1
gameState[10, 13] = 1


gameState[23,5]=1
gameState[23,6]=1
gameState[23,7]=1
gameState[5, 5] = 1
gameState[5, 6] = 1
gameState[5, 7] = 1
gameState[6, 7] = 1
pausa = False
jugando = True
# Bucle de ejecución.
while jugando:

    nuevoEstado = np.copy(gameState)
    #limpiar la pantalla
    pantalla.fill((200,0,0))

    time.sleep(0.5) #delay entre cada fotograma

    # Registramos enventos de teclado y ratón.
    evento = pygame.event.get()

    for ev in evento:
        #Detecta si se presiona una tecla
        if ev.type == pygame.KEYDOWN:
            pausa = not pausa
        #Detecta si se presiona el raton
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            nuevoEstado[celX, celY] = not mouseClick[2]

        if ev.type == pygame.QUIT:
            pygame.quit()
    for y in range (0, nxC):
        for x in range (0, nyC):

            if not pausa:

                # Calculamos el número de vecinos cercanos.
                vecinos =   gameState[(x-1)%nxC,(y-1)% nyC] + \
                            gameState[(x)% nxC,(y - 1)% nyC] + \
                            gameState[(x + 1)% nxC,(y - 1)% nyC] + \
                            gameState[(x - 1)% nxC, (y)% nyC] + \
                            gameState[(x + 1)% nxC,(y)% nyC] + \
                            gameState[(x - 1)% nxC, (y + 1)% nyC] + \
                            gameState[(x)% nxC, (y + 1)% nyC] + \
                            gameState[(x + 1)% nxC, (y + 1)% nyC]

                # Regla #1: Una célula muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x, y] == 0 and vecinos == 3:
                   nuevoEstado[x, y] = 1

                # Regla #2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere".
                elif gameState[x, y] == 1 and (vecinos < 2 or vecinos > 3):
                    nuevoEstado[x, y] = 0

                # Creamos el polígono de cada celda a dibujar.
                poligono = [((x)* dimCW, y*dimCH),((x+1)*dimCW, y*dimCH),
                            ((x+1)*dimCW,(y+1)*dimCH),((x)*dimCW,(y+1) * dimCH)]
                # Dibujamos la celda para cada x,y
                if nuevoEstado[x, y] == 0:
                    pygame.draw.polygon(pantalla, (128, 128, 128), poligono, 1)
                else:
                    pygame.draw.polygon(pantalla, (128, 128, 128), poligono, 0)

    # Actualizacion del estado
    gameState = np.copy(nuevoEstado)

    #Actualizacion de pantalla
    pygame.display.flip()