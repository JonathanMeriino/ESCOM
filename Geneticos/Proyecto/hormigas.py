import numpy as np
from numpy.random import choice as np_choice

"""
        Argumentos:
            distancias (2D numpy.array): Matriz cuadrada de distancias. Diagonal es infinito: np.inf.
            n_hormigas (int): numero de hormigas por iteracion
            n_best (int): numero de las mejores hormigas para depositar la feromona
            n_iteration (int): numero de itercaciones 
            decay (float): Valor por el que se descompone la feromona. El valor de la feromona se multiplica por la descomposición, por lo que 0,95 conducirá a la descomposición, 0,5 a una descomposición mucho más rápida.
            alpha (int or float): exponente de la feromona, un alfa más alto le da más peso a la feromona. Predeterminado=1
            beta (int or float): exponente de la distancia, una beta más alta da más peso a la distancia. Predeterminado=1
        Example:
            ant_colony = AntColony(distancias, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
class colonia_hormigas(object):

    def __init__(self, distancias, n_hormigas, n_best, iteraciones, decay, alpha=1, beta=1):
        
        self.distancias  = distancias
        self.feromona = np.ones(self.distancias.shape) / len(distancias)
        self.all_inds = range(len(distancias))
        self.n_hormigas = n_hormigas
        self.n_best = n_best
        self.iteraciones = iteraciones
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def main(self):
        distance_logs=[]
        camino_corto = None
        camino_mas_corto = ("placeholder", np.inf)
        for _ in range(self.iteraciones):
            caminos = self.generar_caminos()
            self.propagacion_feromona(caminos, self.n_best, camino_corto=camino_corto)
            camino_corto = min(caminos, key=lambda x: x[1])
            if camino_corto[1] < camino_mas_corto[1]:
                camino_mas_corto = camino_corto
            distance_logs.append(camino_mas_corto[1])                      
        return camino_mas_corto,distance_logs

    def propagacion_feromona(self, caminos, n_best, camino_corto):
        caminos_sort = sorted(caminos, key=lambda x: x[1])
        for sendero, dist in caminos_sort[:n_best]:
            for movimiento in sendero:
                self.feromona[movimiento] += 1.0 / self.distancias[movimiento]

    def distancias_camino(self, sendero):
        total_dist = 0
        for ele in sendero:
            total_dist += self.distancias[ele]
        return total_dist

    def generar_caminos(self):
        caminos = []
        for _ in range(self.n_hormigas):
            sendero = self.generar_sendero(0)
            caminos.append((sendero, self.distancias_camino(sendero)))
        return caminos

    def generar_sendero(self, start):
        sendero = []
        visitado = set()
        visitado.add(start)
        prev = start
        for _ in range(len(self.distancias) - 1):
            movimiento = self.elegir_movimiento(self.feromona[prev], self.distancias[prev], visitado)
            sendero.append((prev, movimiento))
            prev = movimiento
            visitado.add(movimiento)
        sendero.append((prev, start)) # vuelve a donde empezo    
        return sendero

    def elegir_movimiento(self, feromona, dist, visitado):
        feromona = np.copy(feromona)
        feromona[list(visitado)] = 0

        row = (feromona ** self.alpha) * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        movimiento = np_choice(self.all_inds, 1, p=norm_row)[0]
        return movimiento
