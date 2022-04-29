import pandas as pd
from sklearn.model_selection import train_test_split

#lectura del corpus tokenizado y lematizado
dataset = pd.read_csv('Corpus.csv')
#x = dataset.iloc[:,0:3].values  #localizar elementos por posicion
#x = dataset.iloc[:,:-1].values

#Pre-procesamiento
valores = dataset["TitulOpinion"]
x_train , x_test  =  train_test_split(valores,test_size=0.2,random_state=0,shuffle=True)

valoresNulos=dataset['TitulOpinion'].isnull().sum()



# Para cada palabra en el corpus
