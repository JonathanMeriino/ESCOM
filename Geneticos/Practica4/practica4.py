"""
Realizar la minimizacion de la funcion x**2 + y**2 en el intervalo de valores 
(-5,5) para x y y
version de PSO: Global
Numero de parti: 20
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

#funcion de evaluacion
def eval_P(parti):
    eval_P=[]
    for i in parti:
        aux = sum(i*i)
        eval_P.append(aux)
    return eval_P

def pso (parti, iteraciones):


    no_iteracion=[]
    for iteracion in range(iteraciones):
    
        #Valor minimo
        pbest=np.copy(parti)
        func_eval=eval_P(parti)
        of_gbest=func_eval[0]
        
        for pos in range(len(func_eval)):
            if func_eval[pos]<of_gbest:
                of_gbest=func_eval[pos]
                index_gbest=pos
        
        gbest=[]
        gbest.append(parti[index_gbest][0])
        gbest.append(parti[index_gbest][1])
        
        no_iteracion.append(iteracion)
        #Actualizacion de velocidades
        n_particulas=[]
        vel_gbest=[]
        if iteracion==0:
            velocidad=np.zeros((20,2))
        else:
            velocidad=velocidad_nueva
        velocidad_nueva=np.zeros((20,2))
        for i in range(20):
            n_particulas.append(i+1)
        for i in pbest:
            vel_gbest.append(i)
        
        w=0.8  #inercia
        c1=0.7 #cognitiva (particula)
        c2=1    # social (swarm)
        for i in range(20):
            for j in range(2):
                r=np.random.uniform(0,1,size=2)
                
                velocidad_nueva[i][j]=w*velocidad[i][j]+c1*r[0]*(pbest[i][j]-parti[i][j])+c2*r[1]*(gbest[j]-parti[i][j])

         #Actualizacion de particulas

        nueva_particula=np.add(parti,velocidad_nueva)

        nueva_OF=eval_P(nueva_particula)

        #Comparacion

        for  i in range(20):
            if nueva_OF[i]<func_eval[i]:
                parti[i]=nueva_particula[i]

        val_gbest=[]   
        pbest=np.copy(parti)
        for i in pbest:
            val_gbest.append(i)
        
        fit_gbest=[] 
        func_eval = eval_P(parti)
        for i in func_eval:
            fit_gbest.append(i)
        
        
        print(f"Numero de Iteracion: {iteracion} ", "-------------------------------", sep='\n')
        
        datos["Velocidad"] = vel_gbest
        datos["gbest"] = val_gbest
        datos["Fitness"] = fit_gbest

        print(datos)
 

pso(parti, iteraciones)