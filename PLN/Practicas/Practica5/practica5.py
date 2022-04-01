import spacy
import re
import spacy
import pandas as pd
#from rake_nltk import Rake
from spacy.lang.es.stop_words import STOP_WORDS

nlp = spacy.load('es_core_news_sm') #pipeline para el preprocesamiento
nlp.max_length = 1600000 # longitud del texto

with open ('corpusStopLimpio.txt') as corpusEntrada:
	corpus = corpusEntrada.read()
	

corpus = re.split("\n", corpus)
print(corpus[1])

"""r = Rake()
noticia1 = corpus[0]

print(noticia1)

print(r.extract_keywords_from_text(noticia1))
print(r.get_ranked_phrases())

ranks=[r.get_ranked_phrases_with_scores()]
print(r.get_ranked_phrases_with_scores())
print(type(ranks))"""
#doc = nlp(corpus)

#tokens = [token for token in doc if not token.is_stop]

#tokens = []
#
#for token in doc:
#	if not token.is_stop:
#		tokens.append(token)
#print(tokens)
		
"""with open('corpusStop.txt', 'w') as doc:
	for i in tokens:
		doc.write("%s\n" %i)
tokens.close()"""
"""
indices = []

for i in corpus:
	indices.append(i)

dataframe = pd.DataFrame()


dataframe['Noticia'] = indices[0:1]
dataframe['Palabras Clave'] = ranks

print(dataframe)"""