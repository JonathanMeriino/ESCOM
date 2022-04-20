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

izquierda=[]
derecha=[]
entradas(izquierda,derecha)
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
def gramRegular(izquierda,derecha):
    x=10



"""
gramatica independiente del contexto
Reglas de produccion
    Lado izquierdo -> un simbolo no terminal 
    lado derecho -> Cualquier secuencia de terminales o no terminales 


"""
"""
gramatica dependiente del contexto 
    Lado izquierdo -> Solo tiene un simbolo No terminal se reemplaza por otro simbolo, mientras el resto sigue igual
    Lado derecho -> No tiene restriccion
"""



"""
gramatica sin restricciones
    Lado izquierdo -> Debe tener por lo menos un simbolo terminal
    Lado derecho -> No tienes restricciones

 """

def sinRestricciones(izquierda,derecha):
    patronIzq = re.compile("[a-z]*[A-Z]+[a-z]*")
    
    for i in izquierda:
        
        if patronIzq.search(i)!=None:
            print("Cumple la derivacion")
        else:
            print("No cumple la derivacion")
            print("No es de Tipo 0")
            break

sinRestricciones(izquierda,derecha)

