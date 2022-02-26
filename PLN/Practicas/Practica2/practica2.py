import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import re 
#extraer corpus de noticias y generacion de nuevo corpus

with open ('corpus_noticias.txt') as corpusEntrada:
	dataset = corpusEntrada.read()
	
nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento

STOP_WORDS.add('a')  # añadir stopword

print(len(dataset))
#nuevoDataset2 = nlp.make_doc(dataset[773906:15447809])

dataset = re.sub("&&&&&&&&","",dataset)
dataset = re.sub("\d{18}","",dataset)
dataset = re.sub("\d+\,\d+\,\d+\,\d+\,\d+\,\d+","",dataset)
doc=nlp.make_doc(dataset[0:773905])



#print(dataset)
print(len(dataset))
normalizar=" "
for token in doc:
	
# tokenizacion
	token.text
	token.pos_
	token.dep_
# lematizacion
	token.lemma
	normalizar = normalizar + token.lemma_+ " "
	if not token.is_stop == True:
		print(token)

# stopwords
print(STOP_WORDS)
print(len(STOP_WORDS))

print("a" in STOP_WORDS)

noStops=""
#for token in normalizar:
#	if token.is_stop==True:
#		noStops = token