#Benitez Medina Leonardo Jhonatan 
#Olvera Aguilar Pedro Eduardo
#Sanchez Mederos Yael Alexandr

import spacy
from spacy.lang.es.stop_words import STOP_WORDS  # biblioteca de stop words
import re #biblioteca de expresiones regulares
#extraer corpus de noticias y generacion de nuevo corpus

with open ('corpus_noticias.txt') as corpusEntrada:
	dataset = corpusEntrada.read()
	
nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento
nlp.max_length = 1600000 # longitud del texto
# ~ dataset = re.sub(r'\n',"\n\n" ,dataset)
dataset = re.split("\&{8}", dataset) # separamos por 8 &


listafin=[]
for i in range(2,len(dataset),3): # for que recorre desde la posicion 2 hasta el final de la lista dando saltos de 3 en 3
    normalizar = " "
    doc = nlp(dataset[i]) #procesa las posiciones donde se ubica cada noticia [2,5,8,11,14,...]
    for token in doc:   # for que itera en cada posicion de la noticia
        token.text, token.pos_, token.dep_, token.lemma_   # Proceso de tokenizacon y lematizacion
        normalizar = normalizar + token.lemma_+ " "
    listafin.append(normalizar)
    

with open('corpusLema.txt','w') as corpusLema:
	for i in listafin:
		corpusLema.write("%s\n" %i)       
corpusLema.close()
# ~ corpusLema = open('corpusLema.txt','w')  # creacion del archivo lematizado
# ~ corpusLema.write(normalizar)    #escritura de la normalizacion 
# ~ corpusLema.close()
#stop_words
with open ('corpusLema.txt') as corpusLema:
	datasetLema = corpusLema.read()

datasetLema=re.split("\n",datasetLema)   #conversion a lista a traves de saltos de linea


STOP_WORDS.add('a')  # añadir stopword
print(STOP_WORDS)

filtro=[] # lista vacia 
for palabra in datasetLema: # for que itera palabra por palabra en el txt lematizado
    if palabra not in STOP_WORDS:   # condicional para encontrar las palabras que no estan en STOP_WORDS
        filtro.append(palabra)  # añadir las palabras a la lista vacia definida anteriormente

#datasetFinal = " ".join(filtro)   # conversion de la lista a un string

#print(datasetFinal)

with open('corpusFinal.txt','w') as corpusLema:
	for i in filtro:
		corpusLema.write("%s\n" %i)       
corpusLema.close()
