import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
import numpy as np
import sys
import pickle
import os.path
import re
import matplotlib.pyplot as plt
import seaborn as sns
# ~ from Preprocesamiento.lematizador import lematizar
		

df = pd.read_excel("Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx")
Cosrpus_X = df.drop(['Polarity', 'Attraction','Title','Opinion'],axis=1).values
y_title = df['Title'].values
y_opinion = df['Opinion'].values
y_polarity = df['Polarity'].values
y_attraction = df['Attraction'].values	
Corpus_polarity=(y_polarity)
Corpus_attraction=(y_attraction)

df["Union"]=df['Title'].astype(str)+" , "+df['Opinion']
Cosrpus_X=df["Union"]
Cosrpus_X1=[]
for i in Cosrpus_X:
	Cosrpus_X1.append(i)

# ~ print(Cosrpus_X1)
# lematizar y tokenizacion
def lem(n):
	cadena_lematizada = lematizar(n)
	# ~ #print (cadena_lematizada.lower())
	return(cadena_lematizada)

	
aux1=[i for i, v in enumerate(Corpus_polarity) if v == 3]# imprime la pocision 
Corpus_polarity=np.delete(Corpus_polarity,aux1)
Cosrpus_X1=np.delete(Cosrpus_X1,aux1)
Corpus_attraction=np.delete(Corpus_attraction,aux1)


#Lematizacion

# ~ Cosrpus_lem1=[]	
# ~ for i in Cosrpus_X1:
	# ~ Cosrpus_lem1.append(lem(i))


# ~ print(Cosrpus_lem1)


        
## SEL polaridad
LisPro=[]
def load_sel():
	#~ global lexicon_sel
	lexicon_sel = {}
	input_file = open('SEL_full.txt', 'r')
	for line in input_file:
		#Las líneas del lexicon tienen el siguiente formato:
		#abundancia	0	0	50	50	0.83	Alegría
		
		palabras = line.split("\t")
		palabras[6]= re.sub('\n', '', palabras[6])
		pair = (palabras[6], palabras[5])
		if lexicon_sel:
			if palabras[0] not in lexicon_sel:
				lista = [pair]
				lexicon_sel[palabras[0]] = lista
			else:
				lexicon_sel[palabras[0]].append (pair)
		else:
			lista = [pair]
			lexicon_sel[palabras[0]] = lista
	input_file.close()
	del lexicon_sel['Palabra']; #Esta llave se inserta porque es parte del encabezado del diccionario, por lo que se requiere eliminar
	#Estructura resultante
		#'hastiar': [('Enojo\n', '0.629'), ('Repulsi\xf3n\n', '0.596')]
	return lexicon_sel

def getSELFeatures(cadenas, lexicon_sel):
	#'hastiar': [('Enojo\n', '0.629'), ('Repulsi\xf3n\n', '0.596')]
	features = []
	for cadena in cadenas:
		valor_alegria = 0.0
		valor_enojo = 0.0
		valor_miedo = 0.0
		valor_repulsion = 0.0
		valor_sorpresa = 0.0
		valor_tristeza = 0.0
		cadena_palabras = re.split('\s+', cadena)
		dic = {}
		for palabra in cadena_palabras:
			if palabra in lexicon_sel:
				caracteristicas = lexicon_sel[palabra]
				for emocion, valor in caracteristicas:
					if emocion == 'Alegría':
						valor_alegria = valor_alegria + float(valor)
					elif emocion == 'Tristeza':
						valor_tristeza = valor_tristeza + float(valor)
					elif emocion == 'Enojo':
						valor_enojo = valor_enojo + float(valor)
					elif emocion == 'Repulsión':
						valor_repulsion = valor_repulsion + float(valor)
					elif emocion == 'Miedo':
						valor_miedo = valor_miedo + float(valor)
					elif emocion == 'Sorpresa':
						valor_sorpresa = valor_sorpresa + float(valor)
		dic['__alegria__'] = valor_alegria
		dic['__tristeza__'] = valor_tristeza
		dic['__enojo__'] = valor_enojo
		dic['__repulsion__'] = valor_repulsion
		dic['__miedo__'] = valor_miedo
		dic['__sorpresa__'] = valor_sorpresa
		
		#Esto es para los valores acumulados del mapeo a positivo (alegría + sorpresa) y negativo (enojo + miedo + repulsión + tristeza)
		dic['acumuladopositivo'] = dic['__alegria__'] + dic['__sorpresa__']
		dic['acumuladonegative'] = dic['__enojo__'] + dic['__miedo__'] + dic['__repulsion__'] + dic['__tristeza__']
		# ~ LisPro=[]
		if dic['acumuladopositivo'] > dic['acumuladonegative']:
			LisPro.append(1)
		else:
			LisPro.append(2)
		# ~ print(LisPro)
	
	
	return features

if __name__=='__main__':
	
	#Load lexicons
	if (os.path.exists('lexicon_sel.pkl')):
		lexicon_sel_file = open ('lexicon_sel.pkl','rb')
		lexicon_sel = pickle.load(lexicon_sel_file)
	else:
		lexicon_sel = load_sel()
		lexicon_sel_file = open ('lexicon_sel.pkl','wb')
		pickle.dump(lexicon_sel, lexicon_sel_file)
		lexicon_sel_file.close()

	
	df = pd.read_csv("CorpusLematizado1.csv")
	X = df.drop(["TitulOpinion"],axis=1).values
	cadenas = df["TitulOpinion"].values
	cadenas = (cadenas)
	# ~ print(cadenas)
	
	cadenas1=[]
	for i in cadenas:
		if type(i)!= str:
			cadenas1.append(str(i))
		else:
			cadenas1.append(i)

	polaridad = getSELFeatures(cadenas1, lexicon_sel)
	#1=
	# ~ print (polaridad)
	# ~ print(len(LisPro))
aux=0
aux1=0
for i in LisPro:
	if i == 1:
		aux1=aux1+1
	else:
		aux=aux+1

print(aux1)
print(aux)
# lista buena 
LisTrue=[]
for i in Corpus_polarity:
    if i==1:
        LisTrue.append(2)
    elif i==2:
        LisTrue.append(2)
    elif i==4:
        LisTrue.append(1)
    elif i==5:
        LisTrue.append(1)

aux=0
aux1=0
for i in LisTrue:
	if i == 1:
		aux1=aux1+1
	else:
		aux=aux+1

print(aux1)
print(aux)
# ~ print("\n\n\n",len(LisTrue))
        
#print(LisTrue)

# ~ Exactitud Metodo Polaridad 

target_names=["Positivo","Negativo"]
print(classification_report(LisTrue,LisPro, target_names=target_names))

data_={"Valores de Predicion":[24724,3367],
       "Valores de Predicion1":[1277,26814]}
       
df=pd.DataFrame(data_, index =["Valores de reales",
                               "Valores de reales1"])

sns.heatmap(data=df, cmap="Greens", annot=True)
plt.show()

#guardar en excel
# ~ lista={"TitulOpinion":Cosrpus_lem1 }

# ~ df_rrss=pd.DataFrame(lista)
# ~ df_rrss.to_csv("CorpusLematizado1.csv")

