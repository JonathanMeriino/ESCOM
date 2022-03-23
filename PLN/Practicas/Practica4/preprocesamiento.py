import spacy
import re

#Tokenizar corpus de noticas
with open ('corpus_noticias.txt') as corpusEntrada:
	dataset_pretoken = corpusEntrada.read()

#Tokenizacion
#dataset_pretoken = re.split('\&{8}',dataset_pretoken)
#nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento
#nlp.max_length = 1600000 # longitud del texto

#dataset_token=[]

#for i in range(2,len(dataset_pretoken),3): # for que recorre desde la posicion 2 hasta el final de la lista dando saltos de 3 en 3
#   normalizar = " "
#    doc = nlp(dataset_pretoken[i]) #procesa las posiciones donde se ubica cada noticia [2,5,8,11,14,...]
#    for token in doc:   # for que itera en cada posicion de la noticia
#        token.text   # Proceso de tokenizacon
#        normalizar = normalizar + token.text+ " "
#    dataset_token.append(normalizar)

#with open('corpusToken.txt','w') as corpusToken:
#	for i in dataset_token:
#		corpusToken.write("%s\n" %i)       
#corpusToken.close()

#Lectura del corpus tokenizadp
with open ('corpusToken.txt') as corpusEntrada:
	corpusToken = corpusEntrada.read()

corpusToken = re.split('\n',corpusToken)

#print(corpusToken[0:2])

datasetToken=[]
for i in corpusToken:
    aux = re.split("\s", i)
    datasetToken.append(aux)

#print(datasetToken[0])

#lectura del corpus practica 2
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

#print(dataset[0])

nuevoDataset=[]
for i in dataset:
    aux = re.split("\s", i)
    nuevoDataset.append(aux)

#print(nuevoDataset[0])