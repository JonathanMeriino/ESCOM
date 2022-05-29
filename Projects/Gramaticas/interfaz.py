import tkinter 
from gramaticas import *
# epsilon -> ε
izquierda=[]
derecha=[]

def agregar(izquierda, derecha):
        
    return izquierda, derecha
def delete():
    return 0

def mostrar():
    """
    #Se imprimen las reglas ingresadas
    print("Reglas de producción")
    for i in range(len(producciones[0])):
    print(f"{producciones[0][i]} --> {producciones[1][i]}")
    
    """
    return 0

    
#creacuib de la ventana
ventana = tkinter.Tk()
ventana.geometry("800x350")

#Titulo de la interfaz grafica
etiquetaTitulo = tkinter.Label(ventana, text="Tipos de gramatica", font="italic")
etiquetaTitulo.grid(row=0, column=0)
#boton para agregar derivaciones
botonAdd = tkinter.Button(ventana , text="Agregar",padx=20, pady=20,command=agregar(izquierda, derecha))
botonAdd.grid(row=5, column=3)
#boton para eliminar derivaciones
botonDel= tkinter.Button(ventana, text="Borrar" , padx=20, pady=20, command = agregar(izquierda, derecha))
botonDel.grid(row=5, column=4)
#boton para evaluacion
botonEval= tkinter.Button(ventana, text="Evaluacion" , padx=20, pady=20, command =evaluacion(izquierda, derecha))
botonEval.grid(row=3, column=0)

#Etiqueta y caja de texto reglas por la izquierda 
etiqRI = tkinter.Label(ventana, text="Izquierda", font="bold")
etiqRI.grid(row=2,column=3)
cajaTexto = tkinter.Entry(ventana, font="Helvetica 20")
cajaTexto.grid(row=3, column=3)
#Etiqueta y caja de texto reglas por la derecha
etiqRD = tkinter.Label(ventana, text="Derecha", font="bold")
etiqRD.grid(row=2,column=4)
cajaTexto2 = tkinter.Entry(ventana, font="Helvetica 20")
cajaTexto2.grid(row=3, column=4)

#Mostar las reglas de produccion
etiqRP = tkinter.Label(ventana, text="Reglas de produccion", font="bold")
etiqRP.grid(row=4,column=0)
lista = tkinter.Listbox(ventana,width=20,height=15)
lista.place(x=25,y=120)
#Mostar el resultado de la evaluacion
resultado = tkinter.Listbox(ventana,width=70, height=5)
resultado.place(x=250, y=200)

ventana.mainloop() #Registro de todo lo que sucede en la ventana

