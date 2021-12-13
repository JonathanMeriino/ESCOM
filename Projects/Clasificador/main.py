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

#print(datos.info())

# pre-procesamiento de datos

archivos = datos['Text'].values.astype("U")

#print(archivos)
vectorizacion = TfidfVectorizer(stop_words='english')  #Frecuencia de palabras

caracteristicas = vectorizacion.fit_transform(archivos)  #transformando todas las caracteristicas usando la media y la varianza

print(caracteristicas)

terms = vectorizacion.get_feature_names_out()


dist = 1 - cosine_similarity(caracteristicas)

print(dist)


linkage_matrix = ward(dist) #definimos la matriz de enlace utilizando la distancia precalculadas de agrupacion de clusteres

fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="right");

plt.tick_params(\
    axis= 'x',          # aplicamos los cambios al eje x
    which='both',      
    bottom='off',      
    top='off',         
    labelbottom='off')

plt.tight_layout() #mostrar plot con un diseño ajustado

#uncomment below to save figure
plt.savefig('ward_clusters.png', dpi=200) #guardado de figura