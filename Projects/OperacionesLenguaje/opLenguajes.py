#ingreso de las cadenas
import re


def introduceLenguages(lenguage,len,index):
    if len==0:
        lenguage=[]
    if index<len:
      aux=input("Ingresa la cadena: ")
      lenguage.append(aux)
    if index<len-1:
        introduceLenguages(lenguage,len,index+1)
#inversa de la cadena
def reverseString(cadena):
    if len(cadena)==0 or len(cadena)==1:
        inversa=cadena
    else:
        inversa=cadena[-1]+reverseString(cadena[:-1])
    return inversa
#inversa del lenguaje
def reverseLenguage(lenguage,inverse,index):
    if len(lenguage)==0:
        inverse=[]
    if index<len(lenguage):
        inverse.append(reverseString(lenguage[index]))
    if index<len(lenguage)-1:
        reverseLenguage(lenguage,inverse,index+1)
#interseccion
def intersection(lenguage1,lenguage2,index1, index2,intersec):
    if lenguage1[index1]==lenguage2[index2] and lenguage1[index1] not in intersec:
        intersec.append(lenguage1[index1])
    if index1<len(lenguage1)-1:
        intersection(lenguage1, lenguage2, index1+1, index2, intersec)
    if index2<len(lenguage2)-1:
        intersection(lenguage1, lenguage2, index1, index2+1, intersec)
#union
def union(lenguage1,lenguage2,index1, index2,uni):
    if lenguage1[index1]!=lenguage2[index2]:
        if lenguage1[index1] not in uni:
            uni.append(lenguage1[index1])
        if lenguage2[index2] not in uni:
            uni.append(lenguage2[index2])
    if lenguage1[index1]==lenguage2[index2]:
        if lenguage1[index1] not in uni:
            uni.append(lenguage1[index1])
    if index1<len(lenguage1)-1:
        union(lenguage1, lenguage2, index1+1, index2, uni)
    if index2<len(lenguage2)-1:
        union(lenguage1, lenguage2, index1, index2+1, uni)
#diferencia de la cadena
def difference(lenguage1, lenguage2, index1, index2, dif):
    if lenguage1[index1] not in lenguage2 and lenguage1[index1] not in dif:
        dif.append(lenguage1[index1])
    if index1<len(lenguage1)-1:
        difference(lenguage1, lenguage2, index1+1, index2, dif)

def potencia():

    pot = int(input("Ingrese el valor de la potencia: "))
    cadena = input("Ingrese cadena: ")
    pote=[]

    for line in range(pot+1):
        if line == 0:
            aux="E"
            pote.append(aux)
        
        elif line>0 and line<10:
            aux=cadena*line
            pote.append(aux)
    print("Potencia de la cadena: ", pote, sep='\n')

    return '\n'
    
    

def concatenar(lenguage1,lenguage2,index1, index2,concat):
    if lenguage1[index1]!=lenguage2[index2]: #si lenguaje1(i1) es diferente a lenguaje2[i2]
        if lenguage1[index1] not in concat:
            concat.append(lenguage1[index1]+lenguage2[index2])
        if lenguage2[index2] in concat:
            concat.append(lenguage2[index2]+lenguage2[index2])
    
    if lenguage1[index1]==lenguage2[index2]: #si lenguaje1(i1) es igual a lenguaje2[i2]
        if lenguage1[index1] not in concat:
            concat.append(lenguage1[index1]+lenguage2[index2])
    

    if index1<len(lenguage1)-1:             #si (i1) es menor a longitud de lenguaje1-1
        concatenar(lenguage1, lenguage2, index1+1, index2, concat)
    if index2<len(lenguage2)-1:             #si (i2) es menor a longitud de lenguaje2-12
        concatenar(lenguage1, lenguage2, index1, index2+1, concat)

def cerrKleene():
    
    n=10
    cadena = input("Ingrese cadena: ")
    klenne=[]

    for line in range(n+1):
        if line == 0:
            aux="E"
            klenne.append(aux)
        
        elif line>0 and line<10:
            aux=cadena*line
            klenne.append(aux)
    klenne.append('...')
    print("Cerradura de Kleene",klenne, sep='\n')

    return '\n'
        
    
def cerrPos():
    
    cadena = input("Ingrese cadena: ")
    pos=[]

    for line in range(1,n+1):
        aux=cadena*line
        pos.append(aux)
    pos.append('...')
    print("Cerradura Positiva",pos, sep='\n')

    return '\n'


lenguage1 =[]

lenguage2=[]
inverso1=[]
inverso2=[]
intersec=[]
uni=[]
concat = []
diferencia1=[]
diferencia2=[]
kleene1=[]
kleene2=[]

len1=int(input("Cuantas cadenas tiene el primer lenguaje: "))
introduceLenguages(lenguage1,len1,0)

len2=int(input("Cuantas cadenas tiene el segundo lenguaje: "))
introduceLenguages(lenguage2,len2,0)

reverseLenguage(lenguage1,inverso1,0)
reverseLenguage(lenguage2,inverso2,0)

intersection(lenguage1, lenguage2,0,0,intersec)

union(lenguage1, lenguage2, 0,0, uni)

difference(lenguage1, lenguage2, 0, 0, diferencia1)
difference(lenguage2, lenguage1, 0, 0, diferencia2)

#cerrKleene(lenguage1,kleene1)
#cerrKleene(lenguage2,kleene2)

concatenar(lenguage1, lenguage2, 0,0,concat)

print("el primer lenguaje es:", lenguage1, sep='\n')

print("el segundo lenguaje es:", lenguage2, sep='\n')

print("El inverso del primer lenguaje es:",inverso1, sep='\n')

print("El inverso del segundo lenguaje es:",inverso2,sep='\n')

print("La interseccion de los lenguajes es:", intersec, sep='\n')

print("La union de los lenguages es", uni, sep='\n')

print("La diferencia tipo A-B es:", diferencia1, sep='\n')

print("La diferencia tipo B-A es:", diferencia2, sep='\n')

#len1=int(input("Ingresa el valor de la potencia"))
#print("Potencia de lenguaje: ", potencia , sep='\n')

concat = list(dict.fromkeys(concat))

print("La concatenacion es:", concat , sep='\n')

#print("Cerradura de Kleene del primer lenguaje es: ",cerrKleene, sep='\n')

#print("Cerradura de Kleene del segundo lenguaje es: ")

#print(cerrKleene(lenguage1))

#print("Cerradura Positiva: ", cerrPos(lenguage1))

print(potencia())

print(cerrKleene())

print(cerrPos())

