import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.es.stop_words import STOP_WORDS 

with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset)



# Representación vectorial binarizada
vectorizador_binario = CountVectorizer(binary=True)
vec_binarizado = vectorizador_binario.fit_transform(dataset)
print (vectorizador_binario.get_feature_names_out())
print (vec_binarizado)#sparse matrix
print (type(vec_binarizado.toarray()))#dense ndarray
print ('Representación vectorial binarizada')
print (vec_binarizado.toarray())#dense ndarray


#~ #Representación vectorial por frecuencia
vectorizador_frecuencia = CountVectorizer()
X = vectorizador_frecuencia.fit_transform(dataset)
print('Representación vectorial por frecuencia')
print (X.toarray())

vectorizador_tfidf = TfidfVectorizer()
X = vectorizador_tfidf.fit_transform(dataset)
print ('Representación vectorial tf-idf')
print (X.toarray())

print(X.shape)

#Pandas
df = pd.DataFrame.sparse.from_spmatrix(X, columns=[len(dataset)])
print(df)