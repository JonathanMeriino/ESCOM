import tkinter as tk
from proyecto3 import *

producciones = [[],[]]

def agregar():
  izquierda = entry1.get()
  derecha = entry2.get()
  producciones[0].append(izquierda)
  producciones[1].append(derecha)
  aux = derecha.split('|')
  for index, value in enumerate(aux):
    if value == '':
      aux[index] = 'ε'

  derecha = "|".join(aux)
  regla = izquierda+"  -->  "+derecha

  lista.insert(tk.END, regla)        
  return 0

def eliminar():  
  indice = lista.curselection()
  if indice != ():
    indice = indice[0]
    print(indice)
    producciones[0].pop(indice)
    producciones[1].pop(indice)
    lista.delete(tk.ACTIVE)
    lista.selection_set(0)
  return 0

def evaluar():
  if len(producciones[0]) != 0:
    for i in range(len(producciones[0])):
      print(f"{producciones[0][i]} --> {producciones[1][i]}")

    resp = eval(producciones)
    resultado.config(text = resp)
    #print(respuesta)
    #
  return 0

alto = 500
ancho = 800

#creacuib de la ventana
ventana = tk.Tk()
canvas1 = tk.Canvas(ventana, width = ancho, height = alto, relief = "raised")
canvas1.pack()


#Titulo de la interfaz grafica
etiquetaTitulo = tk.Label(ventana, text='Tipos de gramaticas', font=('italic',14))
canvas1.create_window(ancho/2, 30, window = etiquetaTitulo)

#Etiqueta y caja de texto reglas por la izquierda 
etiqRI = tk.Label(ventana, text="Izquierda", font="bold")
canvas1.create_window((ancho-200)*(2/3), 80, window = etiqRI)

entry1 = tk.Entry(ventana, font="Helvetica 12") 
canvas1.create_window((ancho-200)*(2/3), 110, window = entry1)

#Etiqueta y caja de texto reglas por la derecha
etiqRD = tk.Label(ventana, text="Derecha", font="bold")
canvas1.create_window((ancho-200)*(3/3), 80, window = etiqRD)

entry2 = tk.Entry(ventana, font="Helvetica 12") 
canvas1.create_window((ancho-200)*(3/3), 110, window = entry2)

#boton para agregar derivaciones
button1 = tk.Button(text = 'Agregar', padx=20, pady=5, command = (lambda: agregar()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window((ancho-200)*(5/6), 150, window = button1)

#Mostar las reglas de produccion
etiqRP = tk.Label(ventana, text="Reglas de produccion", font="bold")
canvas1.create_window((ancho-200)*(1/4), 80, window = etiqRP)

lista = tk.Listbox(ventana, width = 35,height=15)
canvas1.create_window((ancho-200)*(1/4), 230, window = lista)

#boton para eliminar derivaciones
buttonDel = tk.Button(text = 'Borrar', padx=20, pady=5, command = (lambda: eliminar()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window((ancho-200)*(1/4), 380, window = buttonDel)

#boton para evaluacion
botonEval = tk.Button(text = 'Evaluar Reglas', padx=20, pady=5, command = (lambda: evaluar()), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window((ancho-200)*(5/6), 250, window = botonEval)

#Mostar el resultado de la evaluacion
resultado = tk.Label(ventana, text="sa", font="bold, 15")
canvas1.create_window((ancho-200)*(5/6), 310, window = resultado)

#Registro de todo lo que sucede en la ventana
ventana.mainloop() 