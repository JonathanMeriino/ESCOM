import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.preprocessing import OneHotEncoder

datos= pd.read_csv('grimms.csv', low_memory=False)    # lectura de archivo csv
#print(datos)
print(datos.dtypes)  # tipos de datos
print(datos)

#Preprocesamiento

#visualizar dataframes
#print(datos.head(1))
#print(datos.tail(1))
#print(datos.describe())
#print(datos.info)
datos_pre = datos.drop(['Title','Count'], axis=1)
print(datos_pre)
#print(datos_pre.dtypes)

#beta=pd.get_dummies(datos,columns = ['Title']) -> cambiar de variables categoricas a numericas

# 

#datosPreOne = OneHotEncoder(datos_pre = [0])
#x = datosPreOne.fit_transform(datosPreOne).toArray()
#cuentos = datos['Text']
#print(cuentos)

#print(cuentos)

#de texto a datos numericos

#Tfidf (Term frecuency-inverse document frequency)

#tfidf = TfidfVectorizer(stop_words='english')

#cuentosVector =tfidf.fit_transform(datos_pre) #encontrar los parametros ideales para la informacion y aplicarlos

#print(cuentosVector.dtypes)

# finalizacion
#datos_pre.to_csv("datos_clasificados.csv", index =False)

"""
Comandos para instalar librerias:
    pip install pandas
    pip install scikit-learn
    pip install imblearn

Crear entorno virtual en conda:
    1. conda create --name machlearn python=3.9
    2. conda activate machlearn
    3. conda install pandas
        conda install scikit-learn
        conda install imblearn

"""

"""
-Eliminar datos faltantes

axis= 0 - para elimiar filas 
axis = 1 - para elimiar columnas

df.dropna()

- Remplazar datos faltantes

raplece (data a reemplazar, nuevo dato)

"""
