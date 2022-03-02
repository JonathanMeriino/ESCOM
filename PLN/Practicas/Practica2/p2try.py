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

normalizar = ""
nuevoStr =[]
#for token in range (0,doc,3):
#    print(token.text, token.pos_, token.dep_)
 #   normalizar = normalizar + token.lemma_+ " "

for i in range(2,len(dataset),3):
    doc = nlp(dataset[i])
    for token in doc:
        #token.text
        #token.pos_
        #token.dep_
        #token.lemma_
        token.text, token.pos_, token.dep_, token.lemma_
        normalizar = normalizar + token.lemma_+ " "
    #print(normalizar)
    corpusLema = open('corpusLema.txt','w')
    corpusLema.write(normalizar)



#stop_words
with open ('corpusLema.txt') as corpusLema:
	datasetLema = corpusLema.read()
print(len(datasetLema))


STOP_WORDS.add('a')  # añadir stopword
print(STOP_WORDS)
print(len(STOP_WORDS))

print("a" in STOP_WORDS)

for line in datasetLema:
    if line.is_stop== True:
        corpusFinal = open('corpusFinal.txt','w')
        corpusFinal.write(line)
        