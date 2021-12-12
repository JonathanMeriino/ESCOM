import pandas as pd
# librerias para pre-procesamiento
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

datos= pd.read_csv('grimms.csv') # lectura del dataframe

#print(datos)

# explorando la informacion

print(datos.info())

# pre-procesamiento de datos

archivos = datos['Text'].values.astype("U")

#print(archivos)
vectorizacion = TfidfVectorizer(stop_words='english')  #Frecuencia de palabras

caracteristicas = vectorizacion.fit_transform(archivos)  #transformando todas las caracteristicas usando la media y la varianza

k = 2
modelo = KMeans(n_clusters=k,init='k-means++',max_iter=100,n_init=1)
modelo.fit(caracteristicas)  #entrenamiento del modelo con los datos

datos['cluster'] = modelo.labels_

print(datos.head())

# resultado al archivo de texto

clusters = datos.groupby('cluster')

#creacion de archivos csv
for cluster in clusters.groups:
    f = open('clusters/cluster'+str(cluster)+'.csv', 'w') # creacion del csv 
    data = clusters.get_group(cluster)[['Title','Text']]     # obtencion de las columnas del titulo y texto
    f.write(data.to_csv(index_label='id'))   # set index to id
    f.close()


print('Centroides: \n')

orden_centroides = modelo.cluster_centers_.argsort()[:,::-1]
terms = vectorizacion.get_feature_names_out()

for i in range (k):
    print("Cluster %d: " %i)
    for j in orden_centroides[i,:10]:
        print('%s' %terms[j])

    print('-----------')