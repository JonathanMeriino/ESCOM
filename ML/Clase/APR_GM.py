#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 07:10:49 2022

@author: usuario
"""
import numpy as np

def Iter_MG(S,alpha,pi_0,m):
     
     r=S.shape
    
     G=alpha*S+ 1/6.0*(1.0-alpha)*np.ones(r)
     
     print(G)
     
     for i in range(0,m):
         
         pi_0=np.dot(pi_0,G)
         
         
     return pi_0    
    
    
S=np.array([[0.0, 1/2.0,1/2.0,0.0,0.0,0.0],
           [1/6.0,1/6.0,1/6.0,1/6.0,1/6.0,1/6.0],
           [1/3.0,1/3.0,0.0,0.0,1/3.0,0.0],
           [0.0,  0.0,0.0,0.0,1/2.0,1/2.0],
           [0.0,  0.0,0.0,1/2.0,0.0,1/2.0],
           [0.0,  0.0,0.0,1.0,0.0,    0.0]])
    
p0=np.array([1/6.0,1/6.0,1/6.0,1/6.0,1/6.0,1/6.0])

print(Iter_MG(S,0.9,p0,1000))