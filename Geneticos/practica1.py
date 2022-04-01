"""
    Benitez Merino Leonardo Jonathan
    Practica 1 - Algoritmos bioinspirados
"""
import numpy as np
import random
import math
import pandas as pd
from posixpath import split
from funciones import *



dataframe = pd.DataFrame()
    
Fenotipo=poblacionInicial()
Genotipo = createGen(Fenotipo)
fitness = funcionfit(Fenotipo)
poblacion=todo(Fenotipo)
probabilidad_sel = probabilidadSeleccion(fitness)
probabilidad_acumulada = probabilidadAcumulada(probabilidad_sel)
dataframe['Genotipo'] = Genotipo
dataframe['Fenotipo'] = Fenotipo
dataframe['f(x)'] = fitness
dataframe ['Prob. sele'] = probabilidad_sel
dataframe['Prob. acum'] = probabilidad_acumulada
print(dataframe)

print("Seleccion de Padres",seleccionPadres(probabilidad_acumulada), sep='\n')
print(cruza(seleccionPadres(probabilidad_acumulada)))
print("Hijos en valor decimal: ",ToDecimal(cruza(seleccionPadres(probabilidad_acumulada))))
hijos=ToDecimal(cruza(seleccionPadres(probabilidad_acumulada)))
print("Mutacion de los hijos",mutacion(hijos),sep='\n')

for i in range(0,10):
   print(f"Generacion {i} :{poblacion}")
   poblacion=todo(poblacion)
    
