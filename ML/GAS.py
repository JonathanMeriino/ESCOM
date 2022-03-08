#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 07:16:43 2022

@author: usuario
"""
import numpy as np

def d_2(x,y):
    """
    INPUT:
        x,y: Vectores con estructura de arreglo de numpy
    OUTPUT:
        r= Distancia euclidiana entre x, y.
        
    """
    
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
               
    
    
x=np.array([0.0,0.0])
y=np.array([1.0,1.0])

X=[[1.0,2.0],[3.5,10]]
Y=[[0.0,0.0],[4.0,5.0],[100.0,99.0]]

def EAG(X):
    """
    INPUT: 
        X.- Lista de vectores de caracteristicas(listas).
    OUTPUT:    
        L.- Conjunto de clusterings anidados R_0,...,R_(N_1)
    """
    L=[]
    
    L_0=[]
    
    
    for i in X:
        
        L_0.append([i])
        
    L.append(L_0)    
    
    while(len(L_0)>1):    
        J=[] 
        K=[]
        h=np.Infinity
        
        for i in L_0:
            
            for  j in L_0:
            
                if i==j:
                    r=h
                    
                else:
                    r=d_SS(i,j)
                    
                if r<h:
                   h=r
                   J=i.copy()
                   K=j.copy()
                   
        L_0.append(J+K)
        L_0.remove(J)
        L_0.remove(K)
        
        L.append(L_0.copy())
   
    return L    
        
X=[[1.0,2.0],[3.5,10],[0.0,0.0],[4.0,5.0],[100.0,99.0]]    
    
print(EAG(X))    
for i in EAG(X):
    
    print(i,len(i))
    
#print(d_2(x,y),d_SS(X,Y))