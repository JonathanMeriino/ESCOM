#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import numpy as np

#Funcion de disimilitud euclidiana

def d2(x,y):
    """
    Las lineas 13 y 14, no se implementaron en el codigo previo
    """
    x=np.array(x)
    y=np.array(y)
    d2=(x-y)**2.0
    #x=[1,2], y=[3,4]
    #x-y=[-2,-2]
    #d2=[4,4]
    r= sum(d2)**(0.5)    
        
    
    return r


#d(x,C)= min_{y in C} d(x,y)

def dis_min(x,C):
    
    
    r= d2(x, C[0])
    
    
    for i in C: 
        
        l= d2(x,i)
        
        if l<r:            
            
            r= l
        
    return r    
        

def dis_max(x,C):
    
    
    r= d2(x, C[0])
    
    
    for i in C: 
        
        l= d2(x,i)
        
        if l>r:            
            
            r= l
        
    return r        
    
def dis_avg(x,C):
    
    l= 0.0
    
    
    for i in C:
        
        l= l +d2(x,i)
        
    r= l/len(C)

    return r



def BSAS(X,Umb):

    C =[[X[0]]]        
    len_X=len(X)
    for i in range(1,len_X):
    
       lC= len(C)
       r = dis_min(X[i],C[0]) 
       l = 0
       for h in range(0,lC):
           
           dist= dis_min(X[i], C[h])
           if dist< r:
               
               r=dist
               l= h 
       
       
       if dist<= Umb:
           
           C[l].append(X[i])
       
       else:
           
           C.append([X[i]])
           
    return C      


def BSAS1(X,Umb,q):

    C =[[X[0]]]        
    len_X=len(X)
    m=1
    
    for i in range(1,len_X):
         
       lC= len(C)
       r = dis_min(X[i],C[0]) 
       l = 0
       for h in range(0,lC):
           
           dist= dis_min(X[i], C[h])
           if dist< r:
               
               r=dist
               l= h 
       
       
       if dist<= Umb or m>=q:
           
           C[l].append(X[i])
       
       else:
           
           C.append([X[i]])
           m=m+1
           print(m)
    return C      

X=[[234.0,12.0],[0.0,0.0],[1.0,0.0],[0.5,0.8],[12.0,23.0],[102.0,12.01]]
X1=[[-96.0,1.0],[-100.0,2.0],[-103.0,0.0],    
    [100.0,0.0],[101.0,1.0],
    [1001.0,1003.0],[1000.0,1002.0],
    [1.0,0.0],[0.0,0.0],[3.0,1.0]]
R=BSAS(X1,4)
R1=BSAS1(X1,4,3)
print(R1,len(R1))



















