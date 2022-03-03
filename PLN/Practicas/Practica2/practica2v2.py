import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import re 
#extraer corpus de noticias y generacion de nuevo corpus

with open ('corpus_noticias.txt') as corpusEntrada:
	dataset = corpusEntrada.read()
	
nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento
nlp.max_length = 1600000

#dataset1 = re.sub("\d{18}\&{8}\w+\&{8}","",dataset)


#dataset = re.sub("\d+\,\d+\,\d+\,\d+\,\d+\,\d+", "" ,dataset)
#print(dataset[0:6])

#doc=nlp.make_doc(dataset)
dataset = re.split("\&{8}", dataset)

normalizar = " "
nuevoStr =[]
#for token in range (0,doc,3):
#    print(token.text, token.pos_, token.dep_)
 #   normalizar = normalizar + token.lemma_+ " "
filtro=[]
for i in range(2,len(dataset),3):
    doc = nlp(dataset[i])
    for token in doc:
        token.text, token.pos_, token.dep_, token.lemma_
        normalizar = normalizar + token.lemma_+ " "
        for palabra in token.pos_:
            if palabra not in STOP_WORDS:
                filtro.append(palabra)


datasetFinal = " ".join(filtro)

#print(datasetFinal)

corpusFinal = open('corpusFinal.txt','w')
corpusFinal.write(datasetFinal)

#list(STOP_WORDS)
#print(type(STOP_WORDS))     

