"""
	Benitez Merino Leonardo Jonathan
	5BM1
"""
#importacion de bibliotecas
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#lectura del corpus
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

# Representación vectorial binarizada
vectorizador_binario = CountVectorizer(binary=True)
vec_binarizado = vectorizador_binario.fit_transform(dataset)
features=vectorizador_binario.get_feature_names_out()
#print(features)
#print(len(features))
#print (vec_binarizado)#sparse matrix
print (type(vec_binarizado.toarray()))#dense ndarray
print ('Representación vectorial binarizada')
#print (vec_binarizado.toarray())#dense ndarray
print("Tamaño matriz: ",vec_binarizado.shape)
df_bin = pd.DataFrame.sparse.from_spmatrix(vec_binarizado,columns=[features])
#print(df_bin)
#df_bin.to_csv('representacion_binarizada.txt',header=True,index=False, sep='\t')

#~ #Representación vectorial por frecuencia
vectorizador_frecuencia = CountVectorizer()
vec_frec = vectorizador_frecuencia.fit_transform(dataset)
print('Representación vectorial por frecuencia')
#print (vec_frec.toarray())
print("Tamaño matriz: ",vec_frec.shape)
df_frec = pd.DataFrame.sparse.from_spmatrix(vec_frec,columns=[features])
#print(df_frec)
#df_frec.to_csv('representacion_frecuencia.txt',header=True,index=False, sep='\t')
#Representación vectorial tf-idf
vectorizador_tfidf = TfidfVectorizer()
vec_tfidf = vectorizador_tfidf.fit_transform(dataset)
print ('Representación vectorial tf-idf')
#print (vec_tfidf.toarray())
print("Tamaño matriz: ",vec_tfidf.shape)
#dataframe
df_tfidf = pd.DataFrame.sparse.from_spmatrix(vec_tfidf,columns=[features])
df_tfidf.to_csv('df_tfidf.txt',header=True,index=False, sep='\t')

