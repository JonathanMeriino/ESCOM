#from lenguageOperationss import *

def introduceLenguages(lenguage,len,index):
    if len==0:
        lenguage=[]
    if index<len:
      aux=input("Ingresa la cadena: ")
      lenguage.append(aux)
    if index<len-1:
        introduceLenguages(lenguage,len,index+1)
#  x* = {E, x,xx, xxx,...}  0 - inf
def cerrKleene(lenguaje1):

    return 0



# x+ = {x,xx,xxx,...} 1-inf  
def cerrPos(lenguaje2):
    return 0



lenguage1=[]
lenguage2=[]
kleene1=[]
kleene2=[]

len1=int(input("Cuantas cadenas tiene el primer lenguaje: "))
introduceLenguages(lenguage1,len1,0)

len2=int(input("Cuantas cadenas tiene el segundo lenguaje: "))
introduceLenguages(lenguage2,len2,0)


cadena1 =  "x"

print(cadena1*2)

n= 10
milista=[]
for line in range(1,n):
  
    algo=cadena1*line
    milista.append(algo)
        
    
    

print(milista)