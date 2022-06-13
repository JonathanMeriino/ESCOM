import random as rn
import numpy as np
from numpy.random import choice as np_choice
from math import sqrt
import matplotlib.pyplot as plt
import json


class AntColony(object):

    def __init__(self, distancias, n_hormigas, n_best, iteraciones, decay, alpha=1, beta=1):
        """
        Args:
            distancias (2D numpy.array): Square matrix of distancias. Diagonal is assumed to be np.inf.
            n_hormigas (int): numero de hormigas por iteracion
            n_best (int): numero de las mejores hormigas para depositar la feromona
            n_iteration (int): numero de itercaciones 
            decay (float): Rate it which feromona decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1
        Example:
            ant_colony = AntColony(distancias, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distancias  = distancias
        self.feromona = np.ones(self.distancias.shape) / len(distancias)
        self.all_inds = range(len(distancias))
        self.n_hormigas = n_hormigas
        self.n_best = n_best
        self.iteraciones = iteraciones
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        distance_logs=[]
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.iteraciones):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            distance_logs.append(all_time_shortest_path[1])                      
        return all_time_shortest_path,distance_logs

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.feromona[move] += 1.0 / self.distancias[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distancias[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_hormigas):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distancias) - 1):
            move = self.pick_move(self.feromona[prev], self.distancias[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, feromona, dist, visited):
        feromona = np.copy(feromona)
        feromona[list(visited)] = 0

        row = (feromona ** self.alpha) * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move




"""#Presolved TSP Instance
with open("TSP_Data/gr120.json", "r") as tsp_data:
    tsp = json.load(tsp_data)

distancias = tsp["DistanceMatrix"]
tour_size=tsp["TourSize"]
for i in range(tour_size):
  distancias[i][i]=np.inf
distancias=np.array(distancias)
"""



