import pandas as pd
from sklearn.model_selection import train_test_split

#lectura del corpus tokenizado y lematizado
dataset = pd.read_csv('Corpus.csv')
#x = dataset.iloc[:,0:3].values  #localizar elementos por posicion
#x = dataset.iloc[:,:-1].values
#x_train , x_test  =  train_test_split(x,test_size=0.2,random_state=0,shuffle=True)

#Pre-procesamiento
valoresNulos=dataset['TitulOpinion'].isnull().sum()
titulOpinion = dataset["TitulOpinion"].dropna()



# Para cada palabra en el corpus

#lexicon
from polaridad_con_lexicon import *

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
	# ~ cadenas = (cadenas)
	# ~ print(cadenas)
	
	cadenas1=[]
	for i in cadenas:
		if type(i)!= str:
			cadenas1.append(str(i))
		else:
			cadenas1.append(i)

	polaridad = getSELFeatures(cadenas1, lexicon_sel)