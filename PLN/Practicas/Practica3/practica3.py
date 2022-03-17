"""
	Benitez Merino Leonardo Jonathan
	Olver Aguilar Pedro Eduardo
	Sanchez Mederos Yael Alexandr
	5BM1
"""
#importacion de bibliotecas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#lectura del corpus
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

# ~ #Proceso para vector vec_binarizado
vectorizador_binario = CountVectorizer(binary=True)
vec_binarizado = vectorizador_binario.fit_transform(dataset)

lista_parejas = []
lista_simil=[]
for i in range(1,635):
	for j in range (i+1,635):
		dis_coseno=cosine_similarity(vec_binarizado[i],vec_binarizado[j]).flatten()
		lista_parejas.append(f'Noticia{i}-Noticia{j}')
		lista_simil.append(float(dis_coseno))


df = pd.DataFrame()

df['Parejas'] = lista_parejas
df['Valores'] = lista_simil
df_ordenado = df.sort_values('Valores', ascending=False)

print('Comparacion 10 noticias con mayor similitud vector binarizado')
print(df_ordenado[0:15])
#binomial 
# initialize data of lists.
data_ = {'Noticia_332':[1, 0.970, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_585':[0.970, 1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_189':[0, 0, 1,0.859,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_352':[0, 0, 0.859,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_38':[0, 0, 0,0,1,0.825,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_236':[0, 0,0, 0,0.825,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_374':[0, 0, 0,0,0,0,1,0.809,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_428':[0, 0, 0,0,0,0,0.809,1,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_246':[0, 0, 0,0,0,0,0,0,1,0.791,0,0,0,0,0,0,0,0,0,0],
        'Noticia_277':[0, 0, 0,0,0,0,0,0,0.791,1,0,0,0,0,0,0,0,0,0,0],
        'Noticia_218':[0, 0, 0,0,0,0,0,0,0,0,1,0.782,0,0,0,0,0,0,0,0],
        'Noticia_395':[0, 0, 0,0,0,0,0,0,0,0,0.782,1,0,0,0,0,0,0,0,0],
        'Noticia_255':[0, 0, 0,0,0,0,0,0,0,0,0,0,1,0.685,0,0,0,0,0,0],
        'Noticia_272':[0, 0, 0,0,0,0,0,0,0,0,0,0,0.685,1,0,0,0,0,0,0],
        'Noticia_217':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,1,0.661,0,0,0,0],
        'Noticia_397':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0.661,1,0,0,0,0],
        'Noticia_37 ':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.627,0,0],
        'Noticia_62 ':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.627,1,0,0],
        'Noticia_104':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.605],
        'Noticia_453':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.605,1]}
 
# Creates pandas DataFrame.
df = pd.DataFrame(data_, index =['Noticia_332',
                                'Noticia_585',
                                'Noticia_189',
                                'Noticia_352',
                                'Noticia_38',
                                'Noticia_236',
                                'Noticia_374',
                                'Noticia_428',
                                'Noticia_246',
                                'Noticia_277',
                                'Noticia_218',
                                'Noticia_395',
                                'Noticia_255',
                                'Noticia_272',
                                'Noticia_217',
                                'Noticia_397',
                                'Noticia_37',
                                'Noticia_62',
                                'Noticia_104',
                                'Noticia_453'])

sns.heatmap(data=df, cmap="Blues", annot=True)
plt.show()
# ~ #Proceso para vector por frecuencia
vectorizador_frecuencia = CountVectorizer()
vec_frec = vectorizador_frecuencia.fit_transform(dataset)

lista_parejas = []
lista_simil=[]
for i in range(1,635):
	for j in range (i+1,635):
		dis_coseno=cosine_similarity(vec_frec[i],vec_frec[j]).flatten()
		lista_parejas.append(f'Noticia{i}-Noticia{j}')
		lista_simil.append(float(dis_coseno))


df = pd.DataFrame()

df['Parejas'] = lista_parejas
df['Valores'] = lista_simil
df_ordenado = df.sort_values('Valores', ascending=False)

print('Comparacion 10 noticias con mayor similitud vector de frecuencias')
print(df_ordenado[0:15])


# vector de frecuncia


# initialize data of lists.
data_ = {'Noticia_246':[1, 0.984,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_277':[0.984, 1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_332':[0, 0, 1,0.97,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_585':[0, 0, 0.97,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_38 ':[0, 0, 0,0,1,0.96,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_236':[0, 0,0, 0,0.96,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_374':[0, 0, 0,0,0,0,1,0.96,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_428':[0, 0, 0,0,0,0,0.96,1,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_189':[0, 0, 0,0,0,0,0,0,1,0.96,0,0,0,0,0,0,0,0,0],
        'Noticia_352':[0, 0, 0,0,0,0,0,0,0.96,1,0,0,0,0,0,0,0,0,0],
        'Noticia_101':[0, 0, 0,0,0,0,0,0,0,0,1,0.96,0,0,0,0,0,0,0],
        'Noticia_106':[0, 0, 0,0,0,0,0,0,0,0,0.96,1,0,0,0,0,0,0,0],
        'Noticia_233':[0, 0, 0,0,0,0,0,0,0,0,0,0,1,0.95,0,0,0,0,0.95],
        'Noticia_393':[0, 0, 0,0,0,0,0,0,0,0,0,0,0.95,1,0,0,0,0,0],
        'Noticia_211':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,1,0.95,0,0,0],
        'Noticia_276':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0.95,1,0,0,0],
        'Noticia_539':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.95,0],
        'Noticia_578':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.95,1,0],
        'Noticia_534':[0, 0, 0,0,0,0,0,0,0,0,0,0,0.95,0,0,0,0,0,1]}
 
# Creates pandas DataFrame.
df = pd.DataFrame(data_, index =['Noticia_346',
                                'Noticia_277',
                                'Noticia_332',
                                'Noticia_585',
                                'Noticia_38',
                                'Noticia_236',
                                'Noticia_374',
                                'Noticia_428',
                                'Noticia_189',
                                'Noticia_352',
                                'Noticia_101',
                                'Noticia_106',
                                'Noticia_233',
                                'Noticia_393',
                                'Noticia_211',
                                'Noticia_276',
                                'Noticia_539',
                                'Noticia_578',
                                'Noticia_534'])

sns.heatmap(data=df, cmap="Reds", annot=True)
plt.show()
# ~ #Proceso para vector tfidf

vectorizador_tfidf = TfidfVectorizer()
vec_tfidf = vectorizador_tfidf.fit_transform(dataset)

lista_parejas = []
lista_tfidf=[]
for i in range(1,635):
	for j in range (i+1,635):
		dis_coseno=cosine_similarity(vec_tfidf[i],vec_tfidf[j]).flatten()
		lista_parejas.append(f'Noticia{i}-Noticia{j}')
		lista_tfidf.append(float(dis_coseno))


df = pd.DataFrame()

df['Parejas'] = lista_parejas
df['Valores'] = lista_tfidf
df_ordenado = df.sort_values('Valores', ascending=False)

print('Comparacion 10 noticias con mayor similitud vector tfidf')
print(df_ordenado[0:15])
#vector tif
# initialize data of lists.
data_ = {'Noticia_332':[1, 0.95, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_585':[0.95, 1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_189':[0, 0, 1,0.88,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_352':[0, 0, 0.88,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_38 ':[0, 0, 0,0,1,0.86,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_236':[0, 0,0, 0,0.86,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_374':[0, 0, 0,0,0,0,1,0.87,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_428':[0, 0, 0,0,0,0,0.87,1,0,0,0,0,0,0,0,0,0,0,0,0],
        'Noticia_246':[0, 0, 0,0,0,0,0,0,1,0.92,0,0,0,0,0,0,0,0,0,0],
        'Noticia_277':[0, 0, 0,0,0,0,0,0,0.92,1,0,0,0,0,0,0,0,0,0,0],
        'Noticia_218':[0, 0, 0,0,0,0,0,0,0,0,1,0.84,0,0,0,0,0,0,0,0],
        'Noticia_395':[0, 0, 0,0,0,0,0,0,0,0,0.84,1,0,0,0,0,0,0,0,0],
        'Noticia_255':[0, 0, 0,0,0,0,0,0,0,0,0,0,1,0.78,0,0,0,0,0,0],
        'Noticia_272':[0, 0, 0,0,0,0,0,0,0,0,0,0,0.78,1,0,0,0,0,0,0],
        'Noticia_217':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,1,0.76,0,0,0,0],
        'Noticia_397':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0.76,1,0,0,0,0],
        'Noticia_101':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.77,0,0],
        'Noticia_106':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.77,1,0,0],
        'Noticia_104':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.74],
        'Noticia_453':[0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.74,1]}
 
# Creates pandas DataFrame.
df = pd.DataFrame(data_, index =['Noticia_332',
                                'Noticia_585',
                                'Noticia_189',
                                'Noticia_352',
                                'Noticia_38',
                                'Noticia_236',
                                'Noticia_374',
                                'Noticia_428',
                                'Noticia_246',
                                'Noticia_277',
                                'Noticia_218',
                                'Noticia_395',
                                'Noticia_255',
                                'Noticia_272',
                                'Noticia_217',
                                'Noticia_397',
                                'Noticia_101',
                                'Noticia_106',
                                'Noticia_104',
                                'Noticia_453'])

sns.heatmap(data=df, cmap="OrRd", annot=True)
plt.show()
