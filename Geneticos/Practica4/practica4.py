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
arr = np.random.uniform(low=-5,high=5,size=(particulas,dimension))

P=[]

for i,j in enumerate(arr):
    aux=j
    P.append(aux)

#print(P)
gbest = [0,0,0,0,0]


#res = sum(map(lambda i : i * i, P))

#print(res)
eval_P=[]

for i in P:
    aux = sum(i*i)
    eval_P.append(aux)

#print(eval_P)

# seleccionar el gbest 
print("Valor maximo: ", max(eval_P))
print("Valor minimo: ", min(eval_P))




datos['Particulas']=P
datos ['Eval_P']= eval_P
print(datos)