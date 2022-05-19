# https://github.com/Jonatandb/DotCSV-Juego-de-la-vida
# -*- coding: utf-8 -*-
#
# Librerías
import pygame
import numpy as np
import time

from pygame.constants import K_ESCAPE

pygame.init()

# Ancho y alto de la pantalla.
width, height = 1000, 1000

# Creación de la pantalla.
screen = pygame.display.set_mode((height, width))

# Color del fondo = Casi negro, casi oscuro.
bg = 25, 25, 25

# Pintamos el fondo con el color elegido.
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Viva = 1 Muere = 0.
gameState = np.zeros((nxC, nyC))

#Estados
gameState[11, 11] = 1
gameState[12, 12] = 1
gameState[12, 13] = 1
gameState[11, 13] = 1
gameState[10, 13] = 1

gameState[3, 3] = 1
gameState[3, 4] = 1
gameState[3, 5] = 1
gameState[4, 5] = 1
gameState[20, 23] = 1
pauseExect = False

# Bucle de ejecución.
while True:

    newGameState = np.copy(gameState)
    #limpiar la pantalla
    screen.fill(bg)

    time.sleep(0.1) #delay entre cada fotograma

    # Registramos enventos de teclado y ratón.
    evento = pygame.event.get()

    for event in evento:
        #Detecta si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        #Detecta si se presiona el raton
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

        if event.type == pygame.QUIT:
            pygame.quit()
    for y in range (0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

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
                   newGameState[x, y] = 1

                # Regla #2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere".
                elif gameState[x, y] == 1 and (vecinos < 2 or vecinos > 3):
                    newGameState[x, y] = 0

                # Creamos el polígono de cada celda a dibujar.
                poly = [((x)    * dimCW, y      * dimCH),
                        ((x+1)  * dimCW, y      * dimCH),
                        ((x+1)  * dimCW, (y+1)  * dimCH),
                        ((x)    * dimCW, (y+1)  * dimCH)]
                # Dibujamos la celda para cada x,y
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    #Actualizamos la pantalla.
    pygame.display.flip()