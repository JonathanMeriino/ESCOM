import spacy

nlp = spacy.load('es_core_news_sm')

# ~ archivoEntrada = open('archivoEntrada.txt','r')

# ~ for line in archivoEntrada:
	# ~ print(line,end='')

# ~ archivoEntrada.close()


with open ('archivoEntrada.txt') as archivoEntrada:
	dataset = archivoEntrada.read()
	
# ~ print(dataset)

doc = nlp(dataset)

normalizar = " "

for token in doc:
	print(token.text,token.pos_,token.dep_,token.lemma_)
	normalizar = normalizar + token.lemma_+ " "
	
print(normalizar)

archivoSalida = open('archivoSalida.txt','w')
archivoSalida.write(normalizar)
archivoSalida.close()
