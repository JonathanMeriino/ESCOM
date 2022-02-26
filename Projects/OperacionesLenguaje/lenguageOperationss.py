#ingreso de las cadenas
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
    return 0

def concat():
    return 0

def cerrKleene(lenguage):
    
    
    return lenguage   

def cerrPos():
    return 0


lenguage1=[]
lenguage2=[]
inverso1=[]
inverso2=[]
intersec=[]
uni=[]
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

cerrKleene(lenguage1)
cerrKleene(lenguage2)


print("el primer lenguaje es:")
print(lenguage1)
print("el segundo lenguaje es:")
print(lenguage2)
print("El inverso del primer lenguaje es:")
print(inverso1)
print("El inverso del segundo lenguaje es:")
print(inverso2)
print("La interseccion de los lenguajes es:")
print(intersec)
print("La union de los lenguages es")
print(uni)
print("La diferencia tipo A-B es:")
print(diferencia1)
print("La diferencia tipo B-A es:")
print(diferencia2)


print("Cerradura de Kleene: ")
print(cerrKleene)
print("Cerradura Positiva: ")

print("Concatenacion: ")

print("Potencia de lenguaje: ")

