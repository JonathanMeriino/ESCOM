import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import json
import random
import pickle
#nltk.download('punkt')

with open("Shrek.json", "rb") as archivo:
	datos = json.load(archivo)

palabras=[]
tags=[]
auxX=[]
auxY=[]

for contenido in datos["contenido"]:
	for patrones in contenido["patrones"]:
	    PalabraAux = nltk.word_tokenize(patrones)
	    palabras.extend(PalabraAux)
	    auxX.append(PalabraAux)
	    auxY.append(contenido["tag"])

	    if contenido["tag"] not in tags:
	    	tags.append(contenido["tag"])

palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
palabras = sorted(list(set(palabras)))
tags = sorted (tags)

entrenamiento = []
salida = []
salidaVacia = [0 for _ in range(len(tags))]

for x, documento in enumerate (auxX):
	cubeta = []
	PalabraAux = [stemmer.stem(w.lower()) for w in documento]

	for w in palabras:
		if w in PalabraAux:
			cubeta.append(1)
		else:
			cubeta.append(0)
	filaSalida = salidaVacia[:]
	filaSalida[tags.index(auxY[x])] = 1
	entrenamiento.append(cubeta)
	salida.append(filaSalida)
# ~ print(entrenamiento)
# ~ print(salida)

entrenamiento = numpy.array(entrenamiento)
salida = numpy.array(salida)

tensorflow.compat.v1.reset_default_graph()

red = tflearn.input_data(shape = [None, len(entrenamiento[0])])
red = tflearn.fully_connected(red, 50)
red = tflearn.fully_connected(red, 50)
red = tflearn.fully_connected(red, len(salida[0]), activation = "softmax")
red = tflearn.regression(red)

modelo = tflearn.DNN(red)
modelo.fit(entrenamiento,salida, n_epoch = 100, batch_size= 10, show_metric=True)
modelo.save("modelo.tflearn")

nombre = "sherk"

def respuesta(entrada):
	cubeta = [0 for _ in range(len(palabras))]
	entradaProcesada = nltk.word_tokenize(entrada)
	entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
	for parabraIndividual in entradaProcesada:
		for i, palabra in enumerate(palabras):
			if palabra == parabraIndividual:
				cubeta[i] = 1
	resultados = modelo.predict([numpy.array(cubeta)])
	resultadosIndices = numpy.argmax(resultados)
	tag = tags[resultadosIndices]

	for tagAux in datos ["contenido"]:
		if tagAux["tag"] == tag:
			respuesta = tagAux["respuesta"]

	return random.choice(respuesta)	

