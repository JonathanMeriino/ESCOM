import spacy
import re

with open ('archivoEntrada.txt') as archivoEntrada:
	dataset = archivoEntrada.read()
	
nlp = spacy.load('es_core_news_sm')

#print(dataset)

doc = nlp(dataset)

print(doc)
normalizar = ""

for token in doc:
	print(token.text,token.pos_,token.dep_,token.lemma_)
	normalizar = normalizar + token.lemma_+ " "

normalizar = re.sub("\n\s", " ", normalizar)

print(normalizar)

archivoSalida = open('archivoSalida.txt','w')
archivoSalida.write(normalizar)
archivoSalida.close()
