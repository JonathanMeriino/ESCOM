from itertools import product
lenguage1=[]
lenguage2=[]

def introduceLenguages(lenguage,len,index):
    if len==0:
        lenguage=[]
    if index<len:
      aux=input("Ingresa la cadena: ")
      lenguage.append(aux)
    if index<len-1:
        introduceLenguages(lenguage,len,index+1)

def concatenar(lenguage1,lenguage2,index1, index2,uni):
    if lenguage1[index1]!=lenguage2[index2]: #si lenguaje1(i1) es diferente a lenguaje2[i2]
        if lenguage1[index1] not in uni:
            uni.append(lenguage1[index1]+lenguage2[index2])
        if lenguage2[index2] in uni:
            uni.append(lenguage2[index2]+lenguage2[index2])
    
    if lenguage1[index1]==lenguage2[index2]: #si lenguaje1(i1) es igual a lenguaje2[i2]
        if lenguage1[index1] not in uni:
            uni.append(lenguage1[index1]+lenguage2[index2])
    

    if index1<len(lenguage1)-1:             #si (i1) es menor a longitud de lenguaje1-1
        concatenar(lenguage1, lenguage2, index1+1, index2, uni)
    if index2<len(lenguage2)-1:             #si (i2) es menor a longitud de lenguaje2-12
        concatenar(lenguage1, lenguage2, index1, index2+1, uni)

        



uni=[]

len1=int(input("Cuantas cadenas tiene el primer lenguaje 1: "))
introduceLenguages(lenguage1,len1,0)
len1=int(input("Cuantas cadenas tiene el segundo lenguaje 2: "))
introduceLenguages(lenguage2,len1,0)
print("el primer lenguaje es:")
print(lenguage1)
print("el segundo lenguaje es:")
print(lenguage2)

concatenar(lenguage1, lenguage2, 0,0, uni)
print("La concatenacion de los lenguages es ", uni , sep="\n")


