import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.feature_extraction.text import TfidfVectorizer


datos= pd.read_csv('grimms.csv')    # lectura de archivo csv
#print(datos)

cuentos = datos['Text']


print(cuentos)
#print(cuentos)

#de texto a datos numericos

#Tfidf (Term frecuency-inverse document frequency)

tfidf = TfidfVectorizer(stop_words='english')

cuentosVector =tfidf.fit_transform(cuentos) #encontrar los parametros ideales para la informacion y aplicarlos

