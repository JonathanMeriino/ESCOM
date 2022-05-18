import tkinter 
from gramaticas import *


izquierda=[]
derecha=[]
"""def entradas():
    
    opc = int(input("Desea ingresar una derivacion? 1=Si ,2=No: "))
    
    if opc ==1:
        aux1 = cajaTexto.get()
        aux2 = cajaTexto2.get()
        izquierda.append(aux1)
        derecha.append(aux2)
        #entradas(izquierda,derecha)
        etiqueta["text"], etiqueta["text"] = derecha,izquierda
    else: 
        print("Selecciono la opcion 2")"""

    

ventana = tkinter.Tk()
ventana.geometry("700x300")

#etiqueta = tkinter.Label(ventana)
#etiqueta.pack()

etiquetaTitulo = tkinter.Label(ventana, text="Tipos de gramatica")
etiquetaTitulo.grid(row=0, column=0)

#boton1= tkinter.Button(ventana, text="OK" , padx=40, pady=50, command = main)
#boton1.pack()
etiqRI = tkinter.Label(ventana, text="Izquierda")
etiqRI.grid(row=2,column=3)

cajaTexto = tkinter.Entry(ventana, font="Helvetica 20")
cajaTexto.grid(row=3, column=3)

etiqRD = tkinter.Label(ventana, text="Derecha")
etiqRD.grid(row=2,column=4)
cajaTexto2 = tkinter.Entry(ventana, font="Helvetica 20")
cajaTexto2.grid(row=3, column=4)


etiqRP = tkinter.Label(ventana, text="Reglas de produccion")
etiqRP.grid(row=4,column=0)
#boton1 = tkinter.Button(ventana , text="click", command= entradas)
#boton1.pack()
"""boton1 = tkinter.Button(ventana, text="boton1", width=10, height = 5)
boton2 = tkinter.Button(ventana, text="boton2", width=10, height = 5)
boton3 = tkinter.Button(ventana, text="boton3", width=10, height = 5)

boton1.grid(row=0, column = 0)
boton2.grid(row=1, column=0)
boton3.grid(row=2, column =0)"""
ventana.mainloop() #Registro de todo lo que sucede en la ventana

