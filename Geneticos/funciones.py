
import pandas as pd
import random
import math

#funcion de  primerageneracion aleatoria
def CreacionPoblacionAleaticia():
    bandera=0
    banderalistaFenotipo=0
    while(bandera==0):
        listaFenotipo=[]
        for i in range(0,5):
            listaFenotipo.append(random.randint(0,15))

        for i in range(len(listaFenotipo)):
            if(listaFenotipo.count(listaFenotipo[i])==1):
                banderalistaFenotipo+=1
        if (banderalistaFenotipo==5):
            bandera=1
        else:
            banderalistaFenotipo=0
            listaFenotipo=[]
    return listaFenotipo


#regresa genotipo (lista de bits)
def creaciongenotipo(listaFenotipo):
    listagenotipo=[]
    for i in listaFenotipo:
        temp="{:04b}".format(i)
        listagenotipo.append(temp)
    return listagenotipo

def funcionfit(listaFenotipo):
    listafit=[]
    for x in listaFenotipo:
        sin = math.sin(x)
        f_x=(x-5)/(2+sin)
        f_x=abs(f_x)
        listafit.append(f_x)

    return listafit

def Probabilidades(listafit):
    total=sum(listafit)
    listaproba=[]
    for i in listafit:
            listaproba.append(i/total)
    
    aux=0
    listaprobAcum=[]
    for i in listaproba:
        aux+=i
        listaprobAcum.append(aux)
    return listaproba,listaprobAcum
    

def seleciontwopadres(listaacu):
    
    bandera=0
    valoresaleatorios=[random.random(),random.random()]
    while(bandera==0):
        posicionespadres=[]
        valoresaleatorios.sort()
        for i in valoresaleatorios:
            for j in listaacu:
                
                if (i<j):
                    posicionespadres.append(listaacu.index(j))
                    break
        if(posicionespadres[0]!=posicionespadres[1]):
            bandera=1
        else:
            valoresaleatorios[1]=random.random()
        
    return posicionespadres

def cruza(listade2padres):
    hijos=[]
    gen=creaciongenotipo(listade2padres)
    y=random.randint(1,3)

    cadena11=gen[0][:y]
    cadena12=gen[0][y:]   
    
    cadena21=gen[1][:y]
    cadena22=gen[1][y:]
    hijos.append(cadena11+cadena22)
    hijos.append(cadena21+cadena12)
    
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
    hijos=creaciongenotipo(hijos)
    hijo1=hijos[0]
    hijo2=hijos[1]
    hijos.pop()
    hijos.pop()
    p_m=0.1
    for index, valor in enumerate(hijo1):
        num=random.random()
        
        if(p_m>num):
            if (valor=='0'):
                valorNew='1'
                hijo1 = hijo1[:index]+valorNew+hijo1[index+1:]
            elif (valor=='1'):
                valorNew1='0'
                hijo1 = hijo1[:index]+valorNew1+hijo1[index+1:]
        		
        
    for index, valor in enumerate(hijo2):
        num=random.random()
        
        if(p_m>num):
            if(valor=='0'):
                valorNew2='1'
                hijo2 = hijo2[:index]+valorNew2+hijo2[index+1:]
            elif (valor=='1'):
                valorNew3='0'
                hijo2 = hijo2[:index]+valorNew3+hijo2[index+1:]
    hijos.append(hijo1)
    hijos.append(hijo2)
    
    hijos=ToDecimal(hijos)
    return hijos

def todo(listaFenotipo):

  
    listaGenotipo=creaciongenotipo(listaFenotipo)
    listafit=funcionfit(listaFenotipo)
    listaproba,listaacu=Probabilidades(listafit)
    
    mejores=[]
   
     
    for i in range(3):
        bandera=0
        while(bandera==0):
            listade2padres=seleciontwopadres(listaacu)
            listade2padres=[listaFenotipo[listade2padres[0]],listaFenotipo[listade2padres[1]]]
            probadecruza=0.85
            numalprobacruza=random.random()
            if (probadecruza>numalprobacruza):
                listade2hijos=cruza(listade2padres)
                listade2hijos=mutacion(listade2hijos)
                print(listade2padres)
                nuevalista=listade2padres+listade2hijos
                funcionfitdenuevalista=funcionfit(nuevalista)
                
                for i in range(2):
                    max_value = max(funcionfitdenuevalista)
                    posiciondemax=(funcionfitdenuevalista.index(max_value))
                    mejores.append(nuevalista[posiciondemax])
                    nuevalista.pop(posiciondemax)
                    funcionfitdenuevalista.pop(posiciondemax)
                
            
                bandera=1
            
    mejores.pop(-1)
    poblacion = mejores
    return poblacion