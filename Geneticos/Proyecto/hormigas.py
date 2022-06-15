from functools import total_ordering
import numpy as np
from numpy.random import choice as np_choice
class colonia_hormigas(object):

    def __init__(self, distancias, n_hormigas, n_best, iteraciones, rho, alpha=1, beta=2):
        
        self.distancias  = distancias
        self.feromona = np.ones(self.distancias.shape) / len(distancias) # Matriz de unos divididos entre la distancias
        
        self.indices = range(len(distancias))
        self.n_hormigas = n_hormigas
        self.n_best = n_best  # n_best es el numero de hormigas que deposita ferormonas 
        self.iteraciones = iteraciones
        self.rho = rho
        self.alpha = alpha
        self.beta = beta

    def propagacion_feromona(self, caminos, n_best, camino_corto):
        caminos_sort = sorted(caminos, key=lambda x: x[1])
        print(f"Caminos ordenados: {caminos_sort}")
        
        for sendero, dist in caminos_sort[:n_best]:
            for movimiento in sendero:
                self.feromona[movimiento] += 1.0 / self.distancias[movimiento]

    def distancias_camino(self, sendero):
        total_dist = 0
        for i in sendero:
            total_dist += self.distancias[i]

        #print(f"Distancia total {total_dist}")    
        return total_dist

    def generar_caminos(self):
        caminos = []
        #generar un ciclo para cada hormiga
        for _ in range(self.n_hormigas):
            sendero = self.generar_sendero(0)
            caminos.append((sendero, self.distancias_camino(sendero)))

        #print(f"Funcion caminos:{caminos} ")    
        return caminos

    def generar_sendero(self, inicio): # se para como parametro el nodo donde va a comenzar
        #No tiene restriccion en que nodo va a iniciar
        sendero = []
        visitado = set() #los conjuntos no dejan agregar datos que ya estan adentro
        visitado.add(inicio) # se añade el nodo de inicio
        prev = inicio
        #ciclo hasta completar el tamaño del tour
        for _ in range(len(self.distancias) - 1):
            movimiento = self.elegir_movimiento(self.feromona[prev], self.distancias[prev], visitado)
            sendero.append((prev, movimiento))
            prev = movimiento
            visitado.add(movimiento)
        sendero.append((prev, inicio)) # vuelve a donde empezo    
        #print(f"Funcion de sendero: {sendero}")
        return sendero

    def elegir_movimiento(self, feromona, dist, visitado):
        feromona = np.copy(feromona) # crea una copia de las ferormonas
        #print(f"Ferormona: {feromona}")
        feromona[list(visitado)] = 0 #reset de todas las ferormonas visitadas en cero

        vector = (feromona ** self.alpha) * (( 1.0 / dist) ** self.beta)
        print(f"Vector: {vector}")
        vec_norm = vector / vector.sum()
        print(f"Vector normalizada: {vec_norm}")
        #escogiendo de manera probabilistica
        movimiento = np_choice(self.indices, 1, p=vec_norm)[0]
        #print(f"Movimientos: {movimiento}")
        return movimiento

    def main(self):
        camino_corto = None
        desempeno_distancias=[]
        camino_mas_corto = ("placeholder", np.inf) # placeholder para indicar que esta vacio -> iran las rutas
        for _ in range(self.iteraciones):
            caminos = self.generar_caminos()
            self.propagacion_feromona(caminos, self.n_best, camino_corto=camino_corto) # esparcion de las ferormonas
            camino_corto = min(caminos, key=lambda x: x[1])  # cual de todos tuvo el mejor desempeño (el mejor camino)
            #actualizar cual ha sido el mejor camino
            if camino_corto[1] < camino_mas_corto[1]:
                camino_mas_corto = camino_corto
            desempeno_distancias.append(camino_mas_corto[1])
        #print(desempeno_distancias)                      
        return camino_mas_corto,desempeno_distancias
