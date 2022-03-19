"""
    Benitez Merino Leonardo Jonathan
    Practica 1 - Algoritmos bioinspirados
"""
from posixpath import split
import numpy as np
import random
import math
import pandas as pd
def main():
    return 0
#1. Generar una poblacion inicial

    def poblacion_inicial():
        
        individuos = [np.random.randint(0,15) for i in range(5)]
        print(individuos)
        
        return individuos

        pob_inicial = []
        pobInicial_bin = []
        for i in individuos:
        
            aux2 = format(i,'b')
            pobInicial_bin.append(aux2)
            
        

        print("Individuos: ",pob_inicial)
        print("Individuos binario: ",pobInicial_bin)
    
    poblacion_inicial()

    def fitness(individuos):
        print("Proceso de Funcion Fitness")

        for i in individuos:
            print(i)

        
    fitness()



#2. Realizar la seleccion de padres usando el metodo de la ruleta


#3. Realizar la cruza de los padres usando el metodo recombincaion de 1 punto

#4. Reakuzar la mutacion 


#5. Realizar el remplazo del padre mas debil


main()
#6.La condicion de paro

dataframe = pd.DataFrame()
individuos = [np.random.randint(0,15) for i in range(5)]
#print(individuos)

#convercion a binario
pobInicial_bin=[]
for i in range(5):
    binario = np.random.randint(2,size=4)
    pobInicial_bin.append(binario)

print(pobInicial_bin[0])

individuo1 = ''.join(pobInicial_bin[0])
print(individuo1)
#Funcion fitness  f(x) = |(x-5)/(2+sinx)|
fitness = []
for i in individuos:
    fx = abs((i-5)/(2+math.sin(i)))
    fitness.append(float(fx))

#print(fitness)

#dataframe['Individuo'] = [for i in x print(f'Individuo{i}')]
dataframe['Genotipo'] = pobInicial_bin
dataframe['Fenotipo'] = None#individuos
dataframe['f(x)'] = fitness

print(dataframe)

#Seleccion de padres 
"""
1. SUmar el total de f(x)
2. Sacar las prob de sele
3. Sacar la proba de acum

"""