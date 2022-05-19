#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 07:19:26 2022

@author: usuario
"""
import numpy as np
def RMEsc(M):
    
    """
    INPUT:
    
     M.- Matriz de coeficientes de los coeficientes de cada realizacion.
     La i-esima fila de M contiene la informacion de la i-esima observacion 
     del experimento
     
      i-esima fila : (x_i1 x_i2    x_im y_i)
    En las primeras entradas esta la informacion de las variables independientes
    y en la ultima la observacion de la variable de estudio.
    
    OUTPUT:
      A.-Matriz de coeficientes de regresion lineal
      b.-Vector del lado derecho de la regresion lineal 
    
    """
    
    r= M.shape # (n,m+1)
    
    n= r[0]    # Numero de observaciones
    
    m= r[1]    # 
    
    A= np.zeros((m,m)) 
    
    A[0,0]= n
    
    c= np.zeros((m,1))
    
    for i in range(1,m):
        
        
        b=np.sum(M[:,i-1])
        A[0,i]=b
        A[i,0]=b
    
    c[0]=np.sum(M[:,m-1])
    
    for i in range(1,m):
        
        c[i]= np.sum(M[:,m-1]*M[:,i-1])
        
        A[i,i]=np.sum(M[:,i-1]*M[:,i-1])
        
        
        for j in range(i+1,m):
            
            b=np.sum(M[:,i-1]*M[:,j-1])
            print(M[:,i-1],M[:,j-1],i,j)
            
            A[i,j],A[j,i]=b,b
            
        
    return A,c    
        
        
M=np.array([[1.0, 2.0, 3.0, 5.0],
            [1.5, 2.3, 3.1, 4.3],
            [2.8, 3.2,  5.4, 3.2]])       
    
    
    
    
print(RMEsc(M))    