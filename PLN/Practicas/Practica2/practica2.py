from asyncore import write
import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import re 
#extraer corpus de noticias y generacion de nuevo corpus

with open ('corpus_noticias.txt') as corpusEntrada:
	dataset = corpusEntrada.read()
	
nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento
nlp.max_length = 1600000
STOP_WORDS.add('a')  # añadir stopword

print(len(dataset))


# ~ dataset = re.sub(r"\&{8}[\w\s]+\&{8}","",dataset)
# ~ dataset = re.sub(r"\&{8}[\w\d\s]+,"",dataset)

dataset = re.sub(r'[.]',"" ,dataset)
dataset = re.sub(r'\]',"" ,dataset)
dataset = re.sub(r'\[',"" ,dataset)
dataset = re.sub(r'[|]',"" ,dataset)
dataset = re.sub(r'[#]',"" ,dataset)
dataset = re.sub(r"[(]","",dataset)
dataset = re.sub(r"-","",dataset)
dataset = re.sub(r"‘","",dataset)
dataset = re.sub(r"’","",dataset)
dataset = re.sub(r"—","",dataset)
dataset = re.sub(r"_","",dataset)
dataset = re.sub(r"%","",dataset)
dataset = re.sub(r"[$]","",dataset)
dataset = re.sub(r"[¿]","",dataset)
dataset = re.sub(r"[?]","",dataset)
dataset = re.sub(r"¡","",dataset)
dataset = re.sub(r"\'","",dataset)
dataset = re.sub(r"!","",dataset)
dataset = re.sub(r'“',"",dataset)
dataset = re.sub(r'”',"",dataset)
dataset = re.sub(r"[)]","",dataset)
dataset = re.sub(r"[:]","",dataset)
dataset = re.sub(r'["]',"",dataset)
dataset = re.sub(r",","",dataset)
dataset = re.sub(r";","",dataset)
dataset = re.sub(r":","",dataset)
dataset = re.sub(r"\d{18}","",dataset)
dataset = re.sub(r'\w+\&{8}\d+',"" ,dataset)
dataset = re.sub(r'\&{8}\d+',"" ,dataset)
# ~ dataset = re.sub(r'\&\w+',"" ,dataset)
dataset = re.sub(r'[…]',"" ,dataset)
dataset = re.sub(r"\d+\,\d+\,\d+\,\d+\,\d+\,\d+","",dataset)
dataset = re.sub(r"\&{8}[\w\s\d]+\&{8}","",dataset)
dataset = re.sub(r"\&[\w\s\d]+\&{8}","",dataset)
dataset = re.sub(r"\&{8}[\w\s\&\d]+\&{8}","",dataset)
dataset = re.sub(r"\&{8}","",dataset)
# ~ print(dataset)
# ~ archivo_salida = open('corpus_salida.txt', 'w')
# ~ archivo_salida.write(dataset)
# ~ archivo_salida.close()

doc=nlp(dataset)



#print(dataset)
print(len(dataset))
normalizar=" "
for token in doc:
	
	token.text,token.pos_,token.dep_,token.lemma
	normalizar = normalizar + token.lemma_+ " "
	
lematizado = normalizar

lematizado = re.split("\s",lematizado)

filtro=[]
for palabra in lematizado:
    if palabra not in STOP_WORDS:
        filtro.append(palabra)


datasetFinal = " ".join(filtro)

corpusFinal = open('corpusFinal.txt','w')
corpusFinal.write(datasetFinal)


# stopwords
print(STOP_WORDS)
print(len(STOP_WORDS))
print("a" in STOP_WORDS)

noStops=""
#for token in normalizar:
#	if not token.is_stop==True:
#		print(token)


