#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:30:51 2022

@author: usuario
"""
import math as m
import numpy as np
"""
PARAMETERS:
    MU1.-Arreglo con la inicilizacion de MU1 al tiempo t=0
    MU2.-Arreglo con la inicilizacion de MU2 al tiempo t=0
    s1 .-Parametro de inicializacion, donde s1**2.0I es la matriz de covarianza de
       la primer variable aleatoria
    s2 .-Parametro de inicializacion, donde s2**2.0I es la matriz de covarianza de
       la segunda variable aleatoria
    P.- Probabilidad qie tiene la primer variable aleatoria de ser escogida          
"""


#def f0(x,s1,mu):
def f0(x,s1,mu):
  x = np.array(x)
  mu= np.array(mu) 
  l=len(x)  
  x1= (1.0/(2.0*m.pi*(s1**2.0))**(l/2.0))
  x2=m.e**(-sum((mu-x)**2.0)/(2.0*(s1**2.0)))  
  r= x1*x2
  
  return r

print(f0([0.1,0.2],0.5,[0.3,0.4]))

def p_xkThet(x,mu1,mu2,sigma1, sigma2,p):
    
    s= f0(x,sigma1,mu1)*p+f0(x,sigma2,mu2)*(1.0-p)
    
    return s
    
print(p_xkThet([0.1,0.2],[0.3,0.4],[0.8,0.9],0.5, 0.7,0.8))


def p_jxkThet(x,sigma1,mu1,sigma2,mu2,p,j):
    if j==1:
        
        pj=p
        sigmaj=sigma1
        muj=mu1
    elif j==2:    
        pj=1-p
        sigmaj=sigma2
        muj=mu2
    
    r= (f0(x,sigmaj,muj)*pj)/p_xkThet(x,mu1,mu2,sigma1,sigma2,p)
    
    return r
