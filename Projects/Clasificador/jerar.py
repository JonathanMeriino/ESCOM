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
from sklearn import  metrics
from sklearn.cluster import AgglomerativeClustering
datos= pd.read_csv('grimms.csv') # lectura del dataframe

#print(datos)

# explorando la informacion

print(datos.info())

# pre-procesamiento de datos

archivos = datos['Text'].values.astype("U")

#print(archivos)
vectorizacion = TfidfVectorizer(max_df=0.8,stop_words='english')  #Frecuencia de palabras

caracteristicas = vectorizacion.fit_transform(archivos)  #transformando todas las caracteristicas usando la media y la varianza

some= caracteristicas.toarray()
terms = vectorizacion.get_feature_names_out() #obtencion de la salida de los nombres por caracteristicas para la transformacion


dist = cosine_similarity(caracteristicas[0:62],caracteristicas)

print("Distancia Coseno: ", dist, sep='\n')
#print(cosine_similarity(caracteristicas[0:62],caracteristicas))
matriz_enlace = ward(dist) #definimos la matriz de enlace utilizando la distancia euclidiana como metrica
print("Mattriz de enlace: ", matriz_enlace, sep='\n')
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


modelo=AgglomerativeClustering(n_clusters=2,affinity='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='ward', distance_threshold=None, compute_distances=False)
modelo.fit(some.distance_threshold)

