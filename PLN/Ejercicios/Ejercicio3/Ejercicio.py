import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np
import sys
import pickle
from Preprocesamiento.lematizador import lematizar
		

df = pd.read_excel("Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx")
X = df.drop(['Polarity', 'Attraction','Title',"Opinion"],axis=1).values
# ~ y_polarity = df['Polarity'].values
# ~ y_attraction = df['Attraction'].values	
# ~ y_title = df['Title'].values
y_opinion = df['Opinion'].values
#print(y_opinion[0:1])
Corpus_opinio=(y_opinion)
#print(Corpus_opinio)


# lematizar y tokenizacion

def lem(n):
	cadena_lematizada = lematizar(n)
	#print (cadena_lematizada.lower())
	return(cadena_lematizada)

Cosrpus_lematizado=[]	
for i in Corpus_opinio:
	Cosrpus_lematizado.append(lem(i))
 
#print(Cosrpus_lematizado)
# ~ Cosrpus_lematizado.to_csv("data.cvs")

with open('data.txt', 'w') as df:
	for i in Cosrpus_lematizado:
		df.write("%s\n" %i)
		
		
