import pandas as pd
#from imblearn.under_sampling import RandomUnderSampler
#from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder

datos= pd.read_csv('grimms.csv', low_memory=False)    # lectura de archivo csv
#print(datos)

print(datos)

datos_pre = datos.drop(['Title'], axis=1)
#print(datos_pre)

datosPreOne = OneHotEncoder(datos_pre = [0])
x = datosPreOne.fit_transform(datosPreOne).toArray()
#cuentos = datos['Text']
#print(cuentos)

#print(cuentos)

#de texto a datos numericos

#Tfidf (Term frecuency-inverse document frequency)

#tfidf = TfidfVectorizer(stop_words='english')

#cuentosVector =tfidf.fit_transform(cuentos) #encontrar los parametros ideales para la informacion y aplicarlos



# finalizacion
#data.tocsv("datos_limpios.csv", index =False)