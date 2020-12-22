#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image                                                           # funciones para cargar y manipular imágenes
import numpy as np                                                              # funciones numéricas (arrays, matrices, etc.)
import os                                                                       # para funcion de limpiar pantalla


def creaMatriz(i):                                                              #es una funcion secundaria que llamara la funcion principal
    imagenNombre = input ("Inserta el nombre de la imagen : ")                  #pide el nombre de la imagen y la guarda
    local = f"C:\\Users\\leo61\\Downloads\\{imagenNombre}.bmp"                #crea la direcion de la imagen y la guarda en local
    print(f"la direccion es {local}")                                           #imprime la direcion
    I = Image.open(local)                                                       #abre la imagen y la guarda en I
    print("tamaño en pixeles,modo,formato")                                     #imprime en pantalla
    print(I.size, I.mode, I.format)                                             #imprime el formato modo y el tamano
    I = I.convert("L")                                                          #convierte a blanco y negro
    archivo = open(f"ImagenNo_{i}.txt","w+")                                    #abre o crea un archivo con permiso de escritura
    Igray=np.asarray(I)                                                         #crea la imagen un arreglo
    for i in range(len(Igray)):										            #recorremos la imagen pixel a pixel por posición
        for j in range(len(Igray[i])):
            archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(Igray[i][j])+"")	#guardamos el pixel en el archivo nuevo
        archivo.write("\n")

    return Igray                                                                        #retorna el arreglo


def menu():                                                                     #imprime el menu

	os.system('cls') # limpia panatalla
	print ("\tRecuerda que las imagenes tienen que estar en la carpeta de descargas y con terminacion .bmp")
	print ("\n")
	print ("\t\t\t*****MENU PRINCIPAL*****")
	print ("\t1 - Suma de imagenes y creacion de documento con valores int")
	print ("\t2 - Multiplicacion de imagenes y creacion de documento con valores int")
	print ("\t3 - Resta de imagenes 1 a 1")
	print ("\t4 - Suma de imagenes creacion de documento con valores unit8 y creacion de la nueva imagen")
	print ("\t5 - Multiplicacion de imagenes creacion de documento con valores unit8 y creacion de la nueva imagen")
	print ("\t9 - Salir")


while True:                                                                     #mientras no precione 9 seguira ejecutando la funcion principal
    menu()                                                                      #llama la funcion menu

    opcionMenu = input("Selecciona una opcion >> ")                           #guarda el numero digitado

    if opcionMenu=="1":                                                         #si el numero es 1 entra en esta seccion
        listaresultadoSuma = np.zeros((128,128))                                                 #crea los arreglos vacios
        print (listaresultadoSuma)
        matricesfotossuma=[]
        cantidadimagenes = int(input("Inserte la cantidad de imagenes :"))      #guarda la cantidad de imagenes

       # for i in range (128):                                                   #hace un arreglo de tamano 128x128
           # listaresultadoSuma.append( [0] * 128)

        print("\nNota:no debes poner la extension solo coloca el nombre de la imagen\n")#imprime en pantalla
        for i in range(cantidadimagenes):                                       #ejecuta la creaMatriz Y GUARDA CADA UNA EN el arreglo que nos sobra
            matricesfotossuma.append(creaMatriz(i))

        for z in range(cantidadimagenes):                                       #recorre los arreglos y los suma el que le colocamos 0
            for x in range(128):
                for y in range (128):
                    listaresultadoSuma[x][y] += int(matricesfotossuma[z][x][y])

        archivo = open("matrizSumaEnteros.txt","w+")                            #crea un archivo

        for i in range(len(listaresultadoSuma)):								#recorremos la imagen pixel a pixel por posición
            for j in range(len(listaresultadoSuma[i])):
                archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadoSuma[i][j])+"")	#guardamos el pixel en el archivo nuevo
            archivo.write("\n")

        print("\nTu archivo fue creado buscalo en la carpeta donde esta este ejecutable\n")	#imprime en pantalla

        input("Precione Enter para continuar")                           #preciona enter y vuelve al menu




    elif opcionMenu == "2":                                                     #si el numero es 2 entra en esta seccion
        listaresultadomul = []                                                  #crea arrglos vacios
        matricesfotosmul=[]
        cantidadimagenesmul = int(input("inserte la cantidad de imagenes :"))   #pide la cantidad de imagenes y lo guarda
        for i in range (128):                                                   #hace el arreglo 128x128 pixeles
            listaresultadomul.append( [0] * 128)

        print("\nnota:no debes poner la extension solo coloca el nombre de la imagen\n") #imprime una nota
        for i in range(cantidadimagenesmul):                                    #llama la funcion creaMatriz y guarda las matrices
            matricesfotosmul.append(creaMatriz(i))
        if cantidadimagenesmul == 1:                                            #pregunta si la cantidadimagenes es 1 entra

            listaresultadomul = matricesfotosmul[0]                             #guarda la unica matriz en el arreglo de 0
            archivo = open("matrizMultiplicacionEnteros.txt","w+")              #crea un archivo


            for i in range(len(listaresultadomul)):								#recorremos la imagen pixel a pixel por posición
                for j in range(len(listaresultadomul[i])):
                    archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadomul[i][j])+"")	#guardamos el pixel en el archivo nuevo
                archivo.write("\n")
            input("Precione Enter para continuar")                                             #pide poner enter para regresar al menu


        else:                                                                   #si es diferente de 1


            for w in range(128):                                                #recorre las dos primeras imagenes, las multiplica y las guarda
                for x in range(128):
                    for y in range (128):
                        listaresultadomul[w][x] += (int(matricesfotosmul[0][w][y]))*(int(matricesfotosmul[1][y][x]))

            cantidadimagenesmul-=2
            for z in range(cantidadimagenesmul):                                #si son mas de 2 imagenes multiplica el resultado de arriba y lo multiplica hasta terminar
                for w in range(128):
                    for x in range(128):
                        for y in range(128):
                            listaresultadomul[w][x] = (int(listaresultadomul[w][y]))*(int(matricesfotosmul[z+2][y][x]))

            archivo = open("matrizMultiplicacionEnteros.txt","w+")              #crea un archivo


            for i in range(len(listaresultadomul)):								#recorremos la imagen pixel a pixel por posición
                for j in range(len(listaresultadomul[i])):
                    archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadomul[i][j])+"")	#guardamos el pixel en el archivo nuevo
                archivo.write("\n")


            print("\nTu archivo fue creado buscalo en la carpeta donde esta este ejecutable\n")	#imprime en pantalla
            input("Precione Enter para Continuar")                                             #te regresa al menu


    elif opcionMenu=="3":                                                       #si el numero es 3 entra en esta seccion
        listaresultadoResta = []                                                #crea dos arreglos vacios
        matricesfotosResta=[]

        for i in range (128):                                                   #vuelve uno de los arreglos de 128x128 pixeles
            listaresultadoResta.append( [0] * 128)

        print("\nnota:no debes poner la extension solo coloca el nombre de la imagen\n") #imprime una nota
        for i in range(2):                                                      #crea las dos matrices de las imagenes
            matricesfotosResta.append(creaMatriz(i))


        listaresultadoResta=np.subtract(matricesfotosResta[0], matricesfotosResta[1])#resta los arreglos y los guarda

        archivo = open("matrizRestaUnit8.txt","w+")                             #crea un archivo
        for i in range(len(listaresultadoResta)):										#recorremos la imagen pixel a pixel por posición
            for j in range(len(listaresultadoResta[i])):
                archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadoResta[i][j])+"")	#guardamos el pixel en el archivo nuevo
            archivo.write("\n")

        img = Image.fromarray(listaresultadoResta, 'L')                         #convierte el arreglo a imagen
        img.save('resta.png')                                                   #crea la imagen
        img.show()                                                              #mueestra la imagen
        
        print("\nTu archivo fue creado buscalo en la carpeta donde esta este ejecutable\n")	#imprime en pantalla
        input("Precione Enter para continuar")                                                 #al precionar enter vuelve al menu

    elif opcionMenu == "4":                                                     #si el numero es 4 entra en esta seccion

        listaresultadoSuma = []                                                 #CREA 2 arreglos vacios
        matricesfotossuma= []
        cantidadimagenes = int(input("inserte la cantidad de imagenes :"))      #guarda la cantidad de imagenes

        for i in range (128):                                                   #crea el arreglo de 128x128 pixeles
            listaresultadoSuma.append( [0] * 128)

        print("\nnota:no debes poner la extension solo coloca el nombre de la imagen\n") #imprime una nota
        for i in range(cantidadimagenes):                                       #crea las matrices de la imagenes y las guarda
            matricesfotossuma.append(creaMatriz(i))


        listaresultadoSuma =matricesfotossuma[0]                                #guarda la primer matris
        cantidadimagenes-=1                                                     #resta la matris para el siguiente arreglo
        for z in range(cantidadimagenes):                                       #suma todas las matrices restantes
            listaresultadoSuma=np.add(listaresultadoSuma,matricesfotossuma[z+1])



        img = Image.fromarray(listaresultadoSuma, 'L')                          #vuelve al arreglo una imagen
        img.save('suma.png')                                                    #lo guarda
        img.show()                                                              #lo muestra

        archivo = open("matrizSumaUnit8.txt","w+")

        for i in range(len(listaresultadoSuma)):										#recorremos la imagen pixel a pixel por posición
            for j in range(len(listaresultadoSuma[i])):
                archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadoSuma[i][j])+"")	#guardamos el pixel en el archivo nuevo
            archivo.write("\n")
        
        print("\nTu archivo fue creado buscalo en la carpeta donde esta este ejecutable\n")	#imprime en pantalla
        input("Precione Enter para continuar")



    elif opcionMenu =="5":                                                      #si el numero es 5 entra en esta seccion
        listaresultadomul = []                                                  #crea 2 arreglo vacios
        matricesfotosmul=[]
        cantidadimagenesmul = int(input("inserte la cantidad de imagenes :"))   #guarda el numero de imagenes
        for i in range (128):                                                   #vuele un arreglo de 128x128 pixeles
            listaresultadomul.append( [0] * 128)

        print("\nnota:no debes poner la extension solo coloca el nombre de la imagen\n")#imprime una nota
        for i in range(cantidadimagenesmul):                                    #crea y guarda las matrices
            matricesfotosmul.append(creaMatriz(i))


        listaresultadomul = matricesfotosmul[0]                                 #utiliza la primera matris y la guarda
        cantidadimagenesmul-=1                                                  #resta la matris usada arriba el numero
        for z in range(cantidadimagenesmul):                                    #va sacando el producto cartesiano de las matrices
            listaresultadomul =np.dot(listaresultadomul, matricesfotosmul[z+1])


        img = Image.fromarray(listaresultadomul, 'L')                           #vuelve la matriz en imagenNombre
        img.save('mul.png')                                                     #guarda la imagen
        img.show()                                                              #muesta la imagen

        archivo = open("matrizmultiUnit8.txt","w+")                             #crea el archivo

        for i in range(len(listaresultadomul)):										#recorremos la imagen pixel a pixel por posición
            for j in range(len(listaresultadomul[i])):
                archivo.write("["+str(i)+"]"+"["+str(j)+"]"+"="+str(listaresultadomul[i][j])+"")	#guardamos el pixel en el archivo nuevo
            archivo.write("\n")

        print("\nTu archivo fue creado buscalo en la carpeta donde esta este ejecutable\n")	#imprime en pantalla    
        input("Presione enter para regresar al menu")                           #regresa al menu principal





    elif opcionMenu == "9":                                                     #enta si el numero precionado es 9
        break                                                                   #termina el proceso
    else:                                                                       #si preciona cualquier otro  entra aqui
        input("La opcion no existe\n Presione Enter para continuar")            #te pide dijitar algo permitido y regresa al manu
