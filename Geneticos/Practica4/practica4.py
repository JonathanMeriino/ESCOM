"""
Benitez Merino Leonardo Jonathan
Realizar la minimizacion de la funcion x**2 + y**2 en el intervalo de valores 
(-5,5) para x y y
version de PSO: Global
Numero de particulas: 20
iteraciones: 50
w = 0.8 -> inercia
c1 = 0.7
c2=1 
"""
import numpy as np
import pandas as pd


datos = pd.DataFrame()

particulas = 20
dimension = 2
iteraciones = 50
#creacion de las particulas
arr = np.random.uniform(low=-5,high=5,size=(particulas,dimension))

parti=[]

for i,j in enumerate(arr):
    aux=j
    parti.append(aux)

gbest = [0,0,0,0,0]

#funcion de evaluacion
def eval_P(parti):
    eval_P=[]
    for i in parti:
        aux = sum(i*i)
        eval_P.append(aux)
    return eval_P



def valorMinimo():




datos['Particulas']=parti
datos ['Eval_P']= eval_P
print(datos)