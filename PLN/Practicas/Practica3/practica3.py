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
from sklearn.metrics.pairwise import cosine_similarity

#lectura del corpus
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

#Proceso para vector vec_binarizado
vectorizador_binario = CountVectorizer(binary=True)
vec_binarizado = vectorizador_binario.fit_transform(dataset)
#print("Vectores binarizados")
#print(cosine_similarity(vec_binarizado[3],vec_binarizado).flatten)
print('Comparacion entre noticias vector binarizado')
for i in range(1):
	for j in range (0,635):
		dis_coseno=cosine_similarity(vec_binarizado[i],vec_binarizado[j]).flatten()
		print(f'Noticia{i}-Noticia{j} = {dis_coseno}')

#Proceso para vector por frecuencia
vectorizador_frecuencia = CountVectorizer()
vec_frec = vectorizador_frecuencia.fit_transform(dataset)
#print("Vectores por frecuencia",vec_frec, sep='\n')
#print(cosine_similarity(vec_frec[3],vec_frec).flatten())
print('Comparacion entre noticas vector de frecuencias')
for i in range(1):
	for j in range (0,635):
		dis_coseno=cosine_similarity(vec_frec[i],vec_frec[j]).flatten()
		print(f'Noticia{i}-Noticia{j} = {dis_coseno}')

#Proceso para vector tfidf

vectorizador_tfidf = TfidfVectorizer()
vec_tfidf = vectorizador_tfidf.fit_transform(dataset)
#print("Vectores tfidf",vec_tfidf, sep='\n')
#print(cosine_similarity(vec_tfidf[0],vec_tfidf).flatten())
print('Comparacion entre noticias vector tfidf')
for i in range(1):
	for j in range (0,635):
		dis_coseno=cosine_similarity(vec_tfidf[i],vec_tfidf[j]).flatten()
		print(f'Noticia{i}-Noticia{j} = {dis_coseno}')
