import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
import numpy as np
import sys
import re
import pickle
from Preprocesamiento.lematizador import lematizar
		

df = pd.read_excel("Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx")
X = df.drop(['Polarity', 'Attraction','Title',"Opinion"],axis=1).values
y_polarity = df['Polarity'].values
# ~ print(y_polarity[5000:5500])
y_attraction = df['Attraction'].values	
y_title = df['Title'].values
y_opinion = df['Opinion'].values
#print(y_opinion[0:1])
Corpus_opinio=(y_opinion[207:208])
Corpus_title=(y_title[207:208])
#print(Corpus_opinio)
# ~ print(Corpus_title)

# ~ def re(i):
	# ~ aux=(i)
	# ~ sin=re.sub("[(]","",aux)
	# ~ sin=re.sub("[)]","",aux)
	# ~ return(sin)


# ~ Cosrpus_lem1=[]	
# ~ for i in Corpus_title:
	# ~ Cosrpus_lem1.append(re(i))
# ~ print(Cosrpus_lem1)

# lematizar y tokenizacion

def lem(n):
	cadena_lematizada = lematizar(n)
	#print (cadena_lematizada.lower())
	return(cadena_lematizada)

aux=[]
for i in range(len(Corpus_title)):
	# ~ print(type(Corpus_title[i]))
	if(str(type(Corpus_title[i]))!="<class 'str'>"):
		aux.append(i)
# ~ print(aux)
Corpus_opinio=np.delete(Corpus_opinio,aux)
Corpus_title=np.delete(Corpus_title,aux)

Cosrpus_lem0=[]	
for i in Corpus_opinio:
	Cosrpus_lem0.append(lem(i))
print(Cosrpus_lem0)

aux1=[]
for i in range(len(Corpus_opinio)):
	#print(i)
	# ~ print(type(Corpus_opinio[i]))
	if(str(type(Corpus_opinio[i]))!="<class 'str'>"):
		aux1.append(i)
# ~ print(aux1)
Corpus_opinio=np.delete(Corpus_opinio,aux1)
Corpus_title=np.delete(Corpus_title,aux1)

Cosrpus_lem1=[]	
for i in Corpus_title:
	Cosrpus_lem1.append(lem(i))
print(Cosrpus_lem1)

# lista buena 
# ~ LisTrue=[]
# ~ for i in y_polarity:
    # ~ if i==1:
        # ~ LisTrue.append(1)
    # ~ elif i==2:
        # ~ LisTrue.append(1)
    # ~ elif i==3:
        # ~ LisTrue.append(3)
    # ~ elif i==4:
        # ~ LisTrue.append(2)
    # ~ elif i==5:
        # ~ LisTrue.append(2)
        
#print(LisTrue)

#Exactitud Metodo Polaridad 

#target_names=["Positivo","Negativo"]
#print(classification_report(LisTrue,ListPred, target_names=target_names))


#gurdar en excel
#lista={"Titulo":Cosrpus_lem1,
#       "Opinion":Cosrpus_lem0}

#df_rrss=pd.DataFrame(lista)
#df_rrss.to_csv("Corpus.csv")



		
