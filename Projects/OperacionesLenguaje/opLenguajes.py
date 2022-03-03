#ingreso de las cadenas
def introduceLenguages(lenguage,len,index):
    if len==0:
        lenguage=[]
    if index<len:
      aux=input("Cadena: ")
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

    print("Operacion potencia","-----------------", sep='\n')
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
    
def concatenar(lenguage1,lenguage2,longitud):
    nuevo=[]    #cadena auxiliar que almacena todos los valores nuevos
    for i in lenguage2: # para i en lenguage2
        cadena=str(lenguage1[0])+i  #cadena almacena lenguaje1 en almacenamiento i
        nuevo.append(cadena)    #se agrega la cadena a auxiliar nuevo
    if longitud>1:              # si longitud es mayor a 1 
        longitud=longitud-1     #lomgitud se redue en una unidad
        lenguage1.remove(lenguage1[0])  #lenguage1 se remueve  la posicion 0
        aux=lenguage1               #aux toma valor de lenguage1
        nuevo=nuevo+concatenar(aux,lenguage2,longitud)      #se hace recursividad
    return nuevo

def cerrKleene():
    
    n=10
    print("Operacion Cerradura Kleene","-------------------------", sep='\n')
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
    
    n=10
    print("Operacion Cerradura Positiva","-----------------------", sep='\n')
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

len1=int(input("No. cadenas del primer lenguaje: "))
introduceLenguages(lenguage1,len1,0)

len2=int(input("No. cadenas del segundo lenguaje: "))
introduceLenguages(lenguage2,len2,0)

reverseLenguage(lenguage1,inverso1,0)
reverseLenguage(lenguage2,inverso2,0)

intersection(lenguage1, lenguage2,0,0,intersec)

union(lenguage1, lenguage2, 0,0, uni)

difference(lenguage1, lenguage2, 0, 0, diferencia1)
difference(lenguage2, lenguage1, 0, 0, diferencia2)

print("El primer lenguaje es: ", lenguage1)
print("El segundo lenguaje es: ", lenguage2, "\n")

print("Operacion Union","-----------------", sep='\n')
print("La union de los lenguages es", uni,"\n", sep='\n')

print("Operacion Interseccion","-----------------", sep='\n')
print("La interseccion de los lenguajes es:", intersec,"\n", sep='\n')

print("Operacion diferencia","-----------------", sep='\n')
print("La diferencia tipo A-B es:", diferencia1, sep='\n')
print("La diferencia tipo B-A es:", diferencia2,"\n", sep='\n')

print("Operacion Inverso","-----------------", sep='\n')
print("El inverso del primer lenguaje es:",inverso1, sep='\n')
print("El inverso del segundo lenguaje es:",inverso2,"\n",sep='\n')

longitud=len(lenguage1)
nuevo=concatenar(lenguage1,lenguage2,longitud)
print("Operacion Concatenacion","-----------------", sep='\n')
print("La concatenacion es: ", nuevo, "\n",sep='\n')

print(potencia())
print(cerrKleene())
print(cerrPos())

