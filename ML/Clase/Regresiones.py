#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 07:37:24 2022

@author: usuario
"""
import numpy as np

def RegPol(Z,m):
    
    """
    INPUT: 
        Z.- Contiene las observaciones (x_i,y_i),i=1,...,n
        m.- Grado del polinomio 
    
    OUTPUT:
        M.-Matriz de coeficientes de regresion lineal
        b.-Vector del lado derecho de la regresion lineal         
    """
    
    s= Z.shape # vector de dimensiones de Z
    
    n= s[0] #Numeros de filas de Z
    
    M= np.zeros((m+1,m+1))
    
    lista=[n] 
    
    aux=np.ones(n)
    
    for i in range(1,2*m+1):
        
        aux= aux*Z[:,0]
        
        lista.append(np.sum(aux))
        
    lista=np.array(lista)   
    
    for i in range(0,m+1):
        
        M[i,:]=lista[i:m+1+i] 
        
    
    aux1=Z[:,1].copy()

    b=[np.sum(aux1)]


    for i in range(0,m):

       aux1=aux1*Z[:,0]
       
       b.append(np.sum(aux1))
       
       
    return M,b   
       
Z0=np.array([[1.0,2.0],
             [3.0,4.0],
             [2.0,3.0]])       
         
        
print(RegPol(Z0,2))    
    