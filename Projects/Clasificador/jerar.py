import numpy as np
import pandas as pd
import nltk
import re
import os as os
import codecs
import mpld3
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer  # term frequency-inverse document frequency
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram

datos= pd.read_csv('grimms.csv') # lectura del dataframe

#print(datos)

# explorando la informacion

print(datos.info())

# pre-procesamiento de datos

archivos = datos['Text'].values.astype("U")

#print(archivos)
vectorizacion = TfidfVectorizer(stop_words='english')  #Frecuencia de palabras

caracteristicas = vectorizacion.fit_transform(archivos)  #transformando todas las caracteristicas usando la media y la varianza


terms = vectorizacion.get_feature_names_out() #obtencion de la salida de los nombres por caracteristicas para la transformacion


dist = cosine_similarity(caracteristicas)

print(dist)
#print(cosine_similarity(caracteristicas[0:62],caracteristicas))
matriz_enlace = ward(dist) #definimos la matriz de enlace utilizando la distancia euclidiana como metrica
print(matriz_enlace)
#visualizacion del dendograma
fig, ax = plt.subplots(figsize=(15, 20)) # tamaño del set
ax = dendrogram(matriz_enlace, orientation="top");
#Definimos las propiedades
plt.tick_params(
    axis= 'x',          # aplicamos los cambios al eje x
    which='both',      
    bottom='off',      
    top='off',         
    labelbottom='off')

plt.tight_layout() #mostrar plot con un diseño ajustado

#guardar figura
plt.savefig('ward_clusters.png', dpi=200) #guardado de figura