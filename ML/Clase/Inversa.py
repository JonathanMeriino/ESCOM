#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:14:50 2021

@author: usuario
"""

#import sys
import numpy as np
import math

def INV(M):
    
    """
    INPUT: 
        M.-Matriz aumentada de n filas a la cual intentaremos calcular su inversa
    OUTPUT:
        M^{-1} en caso de que M sea invertible.
        
        Un  mensaje de alerta si la matriz no es invertible
    
    [A|I]
    """
   
    r=M.shape
    n= r[0]
    i=0
    k1=1
    IM=np.zeros((n,n))
    
    for t in range(n):
       IM[t,t]=1.0
    #print(IM,M)
    while(0<= i <=n-1 and k1 != 0.0): # Corre sobre las columnas
        
        #print(i)
        lista1=[] 
        
        for j in range(i,n): # Investigamos desde la entrada i-esima hasta la n-1-esima
                             # de la comuna i-esima
            
            
           if M[j,i] !=0.0 :
                
                lista1.append(j)
                
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           
           
        if len(lista1)==0:   
        
            k1=0.0
           # print(k1)
            
        else: 
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           jj=lista1[0]
           mx=math.fabs(M[lista1[0],i])
           
           for h in lista1:
           #Consideramos lista1=[2=lista1[0],-3= lista1[1],47=lista1[2],-8=lista[3]], podemos declarar un ciclo for
           # en la iteracion i-esima h=lista1[i-1]                   
           # que corra sobre los elemento de la lista1, la sintaxis es como en
           # la linea 144
           
           
              
               if(math.fabs(M[h,i])>=mx ):   
                  mx = math.fabs(M[h,i])
                  jj = h     
               
            
           MI=M[i,:].copy() #Copia
           M[i,:]=M[jj,:]
           M[jj,:]=MI
          
           MI2=IM[i,:].copy()
           IM[i,:]=IM[jj,:]
           IM[jj,:]=MI2
           
           #for h in range(0,len(lista1)):         
              #if(math.fabs(M[lista1[h],i])>=mx ):   
               #   mx = math.fabs(M[lista1[h],i])
               #   jj = lista1[h]    
               
           
           #MI=M[i,:].copy() #Copia
           #M[i,:]=M[lista1[jj],:]
           #M[lista1[jj],:]=MI
           
           # En este codigo las lineas  144-159 son equivalentes a las lineas
           # 161-169
           for j in range(i+1,n):
            
               IM[j,:]=IM[j,:]-(M[j,i]/M[i,i])*IM[i,:]
           
               M[j,:] = M[j,:]-(M[j,i]/M[i,i])*M[i,:]
               
           
            #print(M)
     
        i=1+i
    #print(M, IM)
    if k1==0:

       print("La matriz dada no tiene inversa")

    else:
       
       for i in range(0,n-1):
           
           
           for j in range(i,n-1):
                
                IM[n-2-j,:]= IM[n-2-j,:]-(M[n-2-j,n-1-i]/M[n-1-i,n-1-i])* IM[n-1-i,:] 
                
                M[n-2-j,:]= M[n-2-j,:]-(M[n-2-j,n-1-i]/M[n-1-i,n-1-i])* M[n-1-i,:] 
       
           IM[n-1-i,:]=IM[n-1-i,:]/M[n-1-i,n-1-i]
           M[n-1-i,:]=M[n-1-i,:]/M[n-1-i,n-1-i]
       IM[0,:]=IM[0,:]/M[0,0]
       
       M[0,:]=M[0,:]/M[0,0]
               
       return  IM


A1=np.array( [[1.0, 2.0, -1.0],
              [2.0, 1.0,   0.0,],
              [-1.0, 1.0,   2.0]])

A2=np.array( [[1.0, 3.0, -2.0],
              [2.0, 8.0,   -3.0,],
              [1.0, 7.0,   1.0]])
    
A3=np.array( [[2.0, 1.0, -1.0],
              [5.0, 2.0,   -3.0,],
              [0.0, 2.0,   1.0]])
    
A4=np.array( [[1.0, 2.0, 1.0,    0.0],
              [0.0, 1.0,   -1.0, 1.0],
              [1.0, 3.0,   1.0, -2.0],
              [1.0, 4.0, -2.0,   4.0]])
       
A5=np.array( [[4.0, 2.0,      6.0],
              [3.0, 0.0,     7.0,],
              [-2.0, -1.0,   -3.0]])
    
A6=np.array( [[-1.0, 3.0,      2.0],
              [3.0, -4.0,     1.0,],
              [2.0, 5.0,   -2.0]])
E=np.array( [[1.0, 2.0,      1.0, 0.0],
              [0.0, 1.0,     -1.0,1.0],
              [1.0, 3.0,   1.0, 2.0],
              [1.0, 4.0,   -2.0, 4.0]])
AA=INV(E)       
#print(AA )
E=np.array( [[1.0, 2.0,      1.0, 0.0],
              [0.0, 1.0,     -1.0,1.0],
              [1.0, 3.0,   1.0, 2.0],
              [1.0, 4.0,   -2.0, 4.0]])

#print(np.dot(AA,E))
#%%%%%
#,INV(A3),INV(A4), INV(A5))

A7=np.array( [[1.0, 3.0,      5.0],
              [4.0, 15.0,     16.0,],
              [-3.0, -7.0,   -10.0]])


def LU(M):
    
    """
    INPUT: 
        M.-Matriz aumentada de n filas a la cual intentaremos calcular su inversa
    OUTPUT:
        M^{-1} en caso de que M sea invertible.
        
        Un  mensaje de alerta si la matriz no es invertible
    
    [A|I]
    """
   
    r=M.shape
    n= r[0]
    i=0
    k1=1
    IM=np.zeros((n,n))
    
    for t in range(n):
       IM[t,t]=1.0
    #print(IM,M)
    while(0<= i <=n-1 and k1 != 0.0): # Corre sobre las columnas
        
        #print(i)
        lista1=[] 
        
        for j in range(i,n): # Investigamos desde la entrada i-esima hasta la n-1-esima
                             # de la comuna i-esima
            
            
           if M[j,i] !=0.0 :
                
                lista1.append(j)
                
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           
           
        if len(lista1)==0:   
        
            k1=0.0
           # print(k1)
            
        else: 
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           jj=lista1[0]
           #mx=math.fabs(M[lista1[0],i])
           
           #for h in lista1:
           #Consideramos lista1=[2=lista1[0],-3= lista1[1],47=lista1[2],-8=lista[3]], podemos declarar un ciclo for
           # en la iteracion i-esima h=lista1[i-1]                   
           # que corra sobre los elemento de la lista1, la sintaxis es como en
           # la linea 144
           
           
              
               #if(math.fabs(M[h,i])>=mx ):   
                 # mx = math.fabs(M[h,i])
                 # jj = h     
               
            
           MI=M[i,:].copy() #Copia
           M[i,:]=M[jj,:]
           M[jj,:]=MI
          
           MI2=IM[i,:].copy()
           IM[i,:]=IM[jj,:]
           IM[jj,:]=MI2
           #print(IM,M)
           #for h in range(0,len(lista1)):         
              #if(math.fabs(M[lista1[h],i])>=mx ):   
               #   mx = math.fabs(M[lista1[h],i])
               #   jj = lista1[h]    
               
           
           #MI=M[i,:].copy() #Copia
           #M[i,:]=M[lista1[jj],:]
           #M[lista1[jj],:]=MI
           
           # En este codigo las lineas  144-159 son equivalentes a las lineas
           # 161-169
           for j in range(i+1,n):
            
               IM[:,i]=IM[:,i]+(M[j,i]/M[i,i])*IM[:,j]
           
               M[j,:] = M[j,:]-(M[j,i]/M[i,i])*M[i,:]
               #print(IM,M)
           
            #print(M)
     
        i=1+i
    #print(M, IM)
               
    return  IM,M

#print(LU(A7))



def LDL(M):
    
    """
    INPUT: 
        M.-Matriz aumentada de n filas a la cual intentaremos calcular su inversa
    OUTPUT:
        M^{-1} en caso de que M sea invertible.
        
        Un  mensaje de alerta si la matriz no es invertible
    
    [A|I]
    """
   
    r=M.shape
    n= r[0]
    i=0
    k1=1
    IM=np.zeros((n,n))
    
    for t in range(n):
       IM[t,t]=1.0
    #print(IM,M)
    while(0<= i <=n-1 and k1 != 0.0): # Corre sobre las columnas
        
        #print(i)
        lista1=[] 
        
        for j in range(i,n): # Investigamos desde la entrada i-esima hasta la n-1-esima
                             # de la comuna i-esima
            
            
           if M[j,i] !=0.0 :
                
                lista1.append(j)
                
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           
           
        if len(lista1)==0:   
        
            k1=0.0
           # print(k1)
            
        else: 
           #Pi={M[i,j]| j esta en la lista " lista1"}     
           #MaxPi= M[i,j*], j* esta en lista1
           #M[j*,:]
           jj=lista1[0]
           #mx=math.fabs(M[lista1[0],i])
           
           #for h in lista1:
           #Consideramos lista1=[2=lista1[0],-3= lista1[1],47=lista1[2],-8=lista[3]], podemos declarar un ciclo for
           # en la iteracion i-esima h=lista1[i-1]                   
           # que corra sobre los elemento de la lista1, la sintaxis es como en
           # la linea 144
           
           
              
               #if(math.fabs(M[h,i])>=mx ):   
                 # mx = math.fabs(M[h,i])
                 # jj = h     
               
            
           MI=M[i,:].copy() #Copia
           M[i,:]=M[jj,:]
           M[jj,:]=MI
          
           MI2=IM[i,:].copy()
           IM[i,:]=IM[jj,:]
           IM[jj,:]=MI2
           #print(IM,M)
           #for h in range(0,len(lista1)):         
              #if(math.fabs(M[lista1[h],i])>=mx ):   
               #   mx = math.fabs(M[lista1[h],i])
               #   jj = lista1[h]    
               
           
           #MI=M[i,:].copy() #Copia
           #M[i,:]=M[lista1[jj],:]
           #M[lista1[jj],:]=MI
           
           # En este codigo las lineas  144-159 son equivalentes a las lineas
           # 161-169
           for j in range(i+1,n):
            
               IM[:,i]=IM[:,i]+(M[j,i]/M[i,i])*IM[:,j]
           
               M[j,:] = M[j,:]-(M[j,i]/M[i,i])*M[i,:]
               #print(IM,M)
           
            #print(M)
     
        i=1+i
    
    T=np.transpose(IM)
    D=np.zeros((n,n))
    
    for i in range(n):
    
       D[i,i]=M[i,i]  
                
    return  IM,D,T

A8=np.array( [[2.0, -1.0,      2.0],
              [-1.0, 4.0,     3.0,],
              [2.0, 3.0,   -5.0]])



def Ch(A):
    
    m=A.shape
    n=m[0]
    L= np.zeros((n,n))
    
    L[0,0]= A[0,0]**(1/2.0)

    for j in range(1,n):
        
        L[j,0]=A[j,0]/L[0,0]
        
    for i in range(1,n-1):

     s1=0.0
     for h in range(0,i):
         s1= s1 + L[i,h]**2.0   
             
     L[i,i]=(A[i,i]-s1)**(1/2.0)
     
     for k in range(i+1,n):
        s2=0.0
        for t in range(0,i):
          s2=s2+L[k,t]*L[i,t]    
       

        L[k,i]= (A[k,i]-s2)/L[i,i]
        
        
    s3=0.0    
    for z in range(n-1):
       s3= s3+L[n-1,z]**2.0 
        
    L[n-1,n-1]=(A[n-1,n-1]-s3)**(1/2.0)


    return L

A8= np.array( [[4.0, -1.0,      1.0],
              [-1.0, 4.25,     2.75,],
              [1.0, 2.75,   3.5]])
#print(Ch(A8))