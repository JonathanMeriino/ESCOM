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

listaFenotipo=CreacionPoblacionAleaticia()
listaGenotipo = creaciongenotipo(listaFenotipo)
listafitness = funcionfit(listaFenotipo)
poblacion=todo(listaFenotipo)
probabilidad_sel = Probabilidades(listafitness)

dataframe['Genotipo'] = listaGenotipo
dataframe['Fenotipo'] = listaFenotipo
dataframe['f(x)'] = listafitness
dataframe ['Prob. sele'] = probabilidad_sel[0]
dataframe['Prob. acum'] = probabilidad_sel[1]
print(dataframe)

print("Seleccion de Padres",seleciontwopadres(probabilidad_sel[1]), sep='\n')
print(cruza(seleciontwopadres(probabilidad_sel[1])))
print("Hijos en valor decimal: ",ToDecimal(cruza(seleciontwopadres(probabilidad_sel[1]))))
hijos=ToDecimal(cruza(seleciontwopadres(probabilidad_sel[1])))
print("Mutacion de los hijos",mutacion(hijos),sep='\n')

for i in range(0,10):
   print(f"Generacion {i} :{poblacion}")
   poblacion=todo(poblacion)
    
