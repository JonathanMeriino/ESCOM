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
print(p_jxkThet([0.1,0.2],0.4,[0.8,0.9],0.5,[0.4,0.2],0.3,1))
    
def N2(x,mu):
    
    x=x-mu
    x=x*x
    r= sum(x)
    
    return r
    
    
def ItFunc(X,n,p,sigma1,mu1,sigma2,mu2):
    r=X.shape 
    
    N0= r[0]
    l = r[1]
    print(N0,l)
    for i in range(n):
        
        s11= 0.0
        s12= 0.0
        s21= np.array([0.0, 0.0])
        s22= np.array([0.0, 0.0])
        for j in range(N0):
           s11= s11+p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,1)
           #print(p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,1))                         
           s12= s12+p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,2)
           #print(p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,2))
           s21= s21+p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,1)*X[j,:]
           #print(p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,1)*X[j,:])
           s22= s22+p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,2)*X[j,:]   
           #print(p_jxkThet(X[j,:],sigma1,mu1,sigma2,mu2,p,2)*X[j,:])  
        p= s11/N0
        mu1= s21/s11
        mu2= s22/s12
     
    s31= 0.0
    s32= 0.0
    for h in range(N0):
            
            s31= s31+p_jxkThet(X[h,:],sigma1,mu1,sigma2,mu2,p,1) *N2(X[h,:],mu1)
            s32= s32+p_jxkThet(X[h,:],sigma1,mu1,sigma2,mu2,p,2) *N2(X[h,:],mu2)
        
    sigma1= s31/(l*s11)
    sigma2= s32/(l*s12) 
           
    return p, mu1, mu2, sigma1, sigma2     
X=np.array([[1.0,2.0],
   [3.0,4.0],
   [5.0,6.0],
   [5.6,7.8]])  
    
print(ItFunc(X,10,0.8,0.663324,[1.37,1.2],0.663324,[1.9,2.08]))        

import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

mean1 = np.array([1.0, 1.0])
cov1  = np.array([[0.1, 0.0], [0.0, 0.1]])
x1    = multivariate_normal.rvs(mean1, cov1, 80)

mean2 =  np.array([2.0, 2.0])
cov2  = np.array([[0.1, 0.0], [0.0, 0.1]])
x2    = multivariate_normal.rvs(mean2, cov2, 20)
plt.scatter(x1[:,0],x1[:,1])
plt.scatter(x2[:,0],x2[:,1])

plt.show()
x= np.concatenate((x1, x2))

plt.scatter(x[:,0],x[:,1])
plt.show()
           
print(ItFunc(x,100,0.5,0.663324,[1.37, 1.20],0.663324,[1.81, 1.62]))        
        
        
    
        
        
    