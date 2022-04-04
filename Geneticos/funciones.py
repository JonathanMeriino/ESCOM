import numpy as np
import random
import math


def poblacionInicial():
    
    individuos = [np.random.randint(0,15)for i in range (5)]
    Fenotipo  =individuos
    return Fenotipo



def createGen(Fenotipo):
    Genotipo=[]
    for i in Fenotipo:
        aux="{:04b}".format(i)
        Genotipo.append(aux)
    return Genotipo

def funcionfit(Fenotipo):
    fitness=[]
    for x in Fenotipo:
        fx=abs((x-5)/(2+math.sin(x)))
        fitness.append(fx)

    return fitness

def probabilidadSeleccion(fitness):
    prob_sel=[]
    total=sum(fitness)
    for i in fitness:
            prob_sel.append(i/total)
    
    return prob_sel
    
def probabilidadAcumulada(prob_sel):
    aux=0
    prob_acum=[]
    for i in prob_sel:
        aux+=i
        prob_acum.append(aux)
    return prob_acum

def seleccionPadres(prob_acum):
    
    aux=0
    posicion=[]
    valorAleatorio=[random.random(),random.random()]
    while(aux==0):
        valorAleatorio.sort()
        for i in valorAleatorio:
            for j in prob_acum:    
                if (i<j):
                    posicion.append(prob_acum.index(j))
                    break
        if(posicion[0]!=posicion[1]):
            aux=1
        else:
            valorAleatorio[1]=random.random()
        
    return posicion

def cruza(Padres):
    
    
    hijos=[]
    puntoCruce=random.randint(1,3)
    gen=createGen(Padres)

    cad1A=gen[0][:puntoCruce]
    cad1B=gen[0][puntoCruce:]   
    
    cad2A=gen[1][:puntoCruce]
    cad2B=gen[1][puntoCruce:]
    hijos.append(cad1A+cad2B)
    hijos.append(cad2A+cad1B)
    
    hijos=ToDecimal(hijos)
    
    
    return hijos
   
def ToDecimal(hijos):
    decimal=[]
    for n in hijos:
        n=int(n)
        aux=0
        i=0
        while( n >= 1):
            d=n%10
            n=int(n/10)
            aux=aux+d*pow(2,i)
            i=i+1

        
        decimal.append(aux)
    return decimal

def mutacion(hijos):
    hijos=createGen(hijos)
    hijo1=hijos[0]
    hijo2=hijos[1]
    hijos.pop()
    hijos.pop()
    
    p_m=0.1
    for i, valor in hijo1:
        numHijo1=random.random()
        
        if(p_m>numHijo1):
            if (valor=='0'):
                valor='1'
                hijo1 = hijo1[:i]+valor+hijo1[i+1:]
            elif (valor=='1'):
                valor='0'
                hijo1 = hijo1[:i]+valor+hijo1[i+1:]
        		
        
    for i, valor in hijo2:
        numHijo2=random.random()
        
        if(p_m>numHijo2):
            if(valor=='0'):
                valor='1'
                hijo2 = hijo2[:i]+valor+hijo2[i+1:]
            elif (valor=='1'):
                valor='0'
                hijo2 = hijo2[:i]+valor+hijo2[i+1:]
    
    hijos.append(hijo1)
    hijos.append(hijo2)
    
    hijos=ToDecimal(hijos)
    return hijos

def todo(Fenotipo):

  
    Genotipo=createGen(Fenotipo)
    fitness=funcionfit(Fenotipo)
    prob_sel=probabilidadSeleccion(fitness)
    prob_acum = probabilidadAcumulada(prob_sel)
    mejores=[]
   
    
    probadecruza=0.85
    for i in range(3):
        aux=0
        while(aux==0):
            Padres=seleccionPadres(prob_acum)
            Padres=[Fenotipo[Padres[0]],Fenotipo[Padres[1]]]
            numalprobacruza=random.random()
            if (probadecruza>numalprobacruza):
                listade2hijos=cruza(Padres)
                listade2hijos=mutacion(listade2hijos)
                print(Padres)
                nuevalista=Padres+listade2hijos
                funcionfitdenuevalista=funcionfit(nuevalista)
                
                for i in range(2):
                    valorMaximo = max(funcionfitdenuevalista)
                    posicionMaxima=(funcionfitdenuevalista.index(valorMaximo))
                    mejores.append(nuevalista[posicionMaxima])
                    nuevalista.pop(posicionMaxima)
                    funcionfitdenuevalista.pop(posicionMaxima)
                
            
                aux=1
            
    mejores.pop(-1)
    poblacion = mejores
    return poblacion


    
