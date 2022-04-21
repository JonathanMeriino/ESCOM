import re
""" inicial = input("Ingrese el simbolo inicial: ")
elementos = input("Ingrese los elementos del alfabeto: ")
snt = input("Ingrese los simbolos no terminales: ")
listaelementos = list(elementos)
listasnt = list(snt)


gramatica = [inicial, listaelementos, listasnt]

print("Simbolo Inicial , Vocabulario, Simbolos Terminales  }",f"Gramatica = {gramatica}" , sep='\n') """


def entradas(izquierda,derecha):
    opc = int(input("Desea ingresar una derivacion? 1=Si ,2=No: "))
    
    if opc ==1:
        aux1 = input("Ingrese valor izquierda: ")
        aux2 = input("Ingrese valor derecha: ")
        izquierda.append(aux1)
        derecha.append(aux2)
        entradas(izquierda,derecha)
    else: 
        print("Selecciono la opcion 2")

    return izquierda, derecha



def mostrar(izquierda,derecha):
    print("Tabla de derivacion: ")
    for i, j in zip(izquierda,derecha):
        print(f"{i}-->{j}")
    print("-----------------------------")
    

izquierda=[]
derecha=[]
entradas(izquierda,derecha)
print("-----------------------------")
mostrar(izquierda,derecha)
"""
Gramaticas regulares
Reglas de produccion
    Lado izquierdo -> Un solo simbolo no terminal
    Lado derecho -> maximo dos simbolos terminales o no terminales,
    1 terminal seguido de un SNT
    1 terminal 
    cadena vacia

"""
def gramRegular(izquierda, derecha):
    patron=re.compile("[a-z]?[A-Z]?")
    print("Evaluacion de gramatica regular")
    print("Gramatica lineal por la derecha")
    for i, j in zip(izquierda,derecha):
        if len(i)==1:
            if i.isupper():
                if patron.search(j)!=None:
                    print("Cumple la derivacion")
    
        else:
            print("No cumple con la derivacion")
            print("No es de tipo regular por la derecha ")
            break
    print("---------------------------------")
    patronDer=re.compile("[A-Z]?[a-z]?")
    print("Gramatica lineal por la izquierda")
    for i, j in zip(izquierda,derecha):
        if len(i)==1:
            if i.isupper():
                if patronDer.search(j)!=None:
                    print("Cumple la derivacion")
    
        else:
            print("No cumple con la derivacion")
            print("No es de tipo regular por la izquierda ")
            break
    print("-----------------------------")

gramRegular(izquierda,derecha)
"""
gramatica independiente del contexto
Reglas de produccion
    Lado izquierdo -> un simbolo no terminal 
    lado derecho -> Cualquier secuencia de terminales o no terminales 


"""
def independiente(izquierda,derecha): #Tipo 2
    patronIzq = re.compile("[A-Z]?")
    terminal1 = re.compile("[0-9]+")
    print("Evaluacion independiente del contexto")
    for i, j in zip(izquierda,derecha):
        if len(i)==1:
            if patronIzq.search(i)!=None:
                if not (i.islower() and j.islower()):
                    if terminal1.search(i)!=None:
                        print("Cumple la derivacion")
        else:
            print("No cumple con la derivacion")
            print("No es de tipo 2 ")
            break
    return "-----------------------------"

print(independiente(izquierda,derecha))

"""
gramatica dependiente del contexto 
    Lado izquierdo -> Solo tiene un simbolo No terminal se reemplaza por otro simbolo, mientras el resto sigue igual
    Lado derecho -> No tiene restriccion
"""
def dependiente(izquierda,derecha): #Tipo 1
    patronIzq = re.compile("[a-z]*[A-Z]+[a-z]*")
    print("Evaluacion dependiente del contexto")
    for i, j in zip(izquierda,derecha):
        if len(i) <= len(j):
            if patronIzq.search(i)!=None:
                print("Cumple la derivacion")
        else:
            print("No cumple con la derivacion")
            print("No es de tipo 1 ")
            break
    return "-----------------------------"
print(dependiente(izquierda,derecha))
"""
gramatica sin restricciones
    Lado izquierdo -> Debe tener por lo menos un simbolo terminal
    Lado derecho -> No tienes restricciones

 """

def sinRestricciones(izquierda,derecha): #Tipo 0
    patronIzq = re.compile("[a-z]*[A-Z]+[a-z]*")
    print("Evaluacion sin restriccion")
    for i in izquierda:
        
        if patronIzq.search(i)!=None:
            print("Cumple la derivacion")
        else:
            print("No cumple la derivacion")
            print("No es de Tipo 0")
            break
    return "----------------------------"
print(sinRestricciones(izquierda,derecha))

