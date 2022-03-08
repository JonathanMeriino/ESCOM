#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:00:09 2022

@author: usuario
"""

import numpy as np
import math

def d_2(x,y):
    """
    INPUT:
        x,y: Vectores con estructura de arreglo de numpy
    OUTPUT:
        r= Distancia euclidiana entre x, y.
        
    """
    x=np.array(x)
    y=np.array(y)
    
    d2=(x-y)**2.0
    
    r= sum(d2)**0.5
    
    return r

def d_SS(X,Y):
    
    """
    INPUT:
        X,Y: Listas que contienen a las listas de vectores 
        de caracteristicas
        
    OUTPUT:
        r: Distancia entre X y Y.
    
    """
    r= np.Infinity
    
    for i in X:
        
        
        for j in Y:
    
            h=d_2(np.array(i),np.array(j))# Se les da estructura de arrego de numoy a i,j 
                                          #como prerrequisito para ser evaluados en "d_2"
            
            if h<r:
                
               r=h
               
    return r           

def MUAS(X,a1,a2,b,c):
    """
    
    """
    
    L=[] # Clusterings creados
    L_0=[]
    
    
    for i in X:                
        
        L_0.append([i]) #Clustering de inicializacion
        
    L.append(L_0)  # Conjunto de todos los clusterings anidados    
    lengh_L0=len(L_0) #Longitud de cada clustering creado en cada iteracion    
    h=np.Infinity
    
    H=np.zeros((lengh_L0,lengh_L0))
    for i in range(0,lengh_L0):
        
        for j in range(i+1,lengh_L0):
            
             r=d_SS(L_0[i],L_0[j])
             H[i,j]=r
             if (r<h):
                 
                 h=r
                 KI=L_0[i].copy() #Cluster C_i
                 KJ=L_0[j].copy() #Cluster C_j
    print(H)
    print(KI,KJ)
    L_0.append(KI+KJ)
    L_0.remove(KI)
    L_0.remove(KJ)
    print(L_0,"Inicializacion")
    
    lengh_L0=len(L_0)
    
    L.append(L_0)
    
    
    while (len(L_0)>1):# Crearemos iterativamente clusterings anidados
        
        
        h= np.Infinity
        
        H=np.zeros((lengh_L0,lengh_L0))
        for i in range(0,lengh_L0):
            
            for j in range(i+1,lengh_L0):
                
                if (j==lengh_L0-1):
                
                   r=a1*d_SS(KI,L_0[i])+a2*d_SS(KJ,L_0[i])+b*d_SS(KI,KJ)+c*math.fabs(d_SS(KI,L_0[i])-d_SS(KJ,L_0[i]))       #d(Ci,Cj)
                   print(KI,KJ,L_0[i], "Clusters")
                   print(d_SS(KI,L_0[i]),d_SS(KJ,L_0[i]),d_SS(KI,KJ),"Parameters")
                else :
                   r=d_SS(L_0[i],L_0[j])
                
                H[i,j]=r
                if r<h:
                    h=r
                    KII=L_0[i].copy()    
                    KJJ=L_0[j].copy()
        KI=KII.copy()
        KJ=KJJ.copy()
        print(H)
        print(KI,KJ)            
        L_0.append(KI+KJ) #L_0u{C_q}
        L_0.remove(KI)  #L_0\{C_i}
        L_0.remove(KJ)  #L_0\{C_j}
        print(L_0,"Main Loop")
    
        
        lengh_L0=len(L_0)
    
        L.append(L_0)
                          
                    
    return L


X=[[1.0,2.0],[3.5,10],[4.0,5.0],[100.0,99.0]]

print(MUAS(X,0.5,0.5,0.0,-0.5))



                