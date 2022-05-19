#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:16:42 2022

@author: usuario
"""

import numpy as np
import Inversa as IM


x=np.array([[0.038,0.05  ],
            [0.194,0.127 ],
            [0.425,0.094 ],
            [0.626,0.2122],
            [1.253,0.2729],
            [2.5,  0.2665],
            [3.740, 0.3317]
            ])


 


X=x[:,0]
Y=x[:,1]

def f1(a_1, x_i):
    
    r= -x_i/(a_1+x_i)
    
    return r


def f2(a_0, a_1, x_i):
        
    r=(a_0*x_i)/(a_1+x_i)**2.0
    
    return r



def J_r(a,X):
    """
    INPUT:
        a.- El conjunto de parametros a^{k}, que se van actualizando
            por medio del algoritmo de Gauss-Newton.
            
            Arreglo de n filas y una columna
            
        x.- Arreglo de observaciones x=[x_i]
    """
    r= X.shape
    
    Jr=np.zeros((r[0],2))
    
    for i in range(0,r[0]):
        
        Jr[i,0]= f1(a[1,0],X[i])
        Jr[i,1]= f2(a[0,0],a[1,0], X[i])
        
    return Jr    
        
def r(a,X,Y):
    
    s= X.shape
    
    r= np.zeros((s[0],1))
    
    for i in range(0,s[0]):
        
        r[i,0]=Y[i]-a[0,0]*(X[i]/(a[1,0]+X[i]))
        
        
    return r    
        
    
def Met_GN(X,Y,a,n):


   for i in range(n):
       Jrr=J_r(a,X)
       rr= r(a,X,Y)
       #print(Jrr,rr,Jrr.shape, rr.shape,"Hola")
       Jrr1= Jrr.copy()
       rr1= rr.copy()
       #print(Jrr1,rr1,Jrr1.shape, rr1.shape,"Hola11")
       #print(Jrr1.shape,rr1.shape, np.transpose(Jrr1).shape)
       k1=np.dot(np.transpose(Jrr1),Jrr1)
       k1= IM.INV(k1)
       k2=np.dot(np.transpose(Jrr1),rr1)
       #print(k1,k2)
       a= a-np.dot(k1,k2)
       
   return a    
a= np.array([[0.9],
             [0.2]])       
#print(X.shape,Y.shape)
print(Met_GN(x[:,0],x[:,1],a,1000))       