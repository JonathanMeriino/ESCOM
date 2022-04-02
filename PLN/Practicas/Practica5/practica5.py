import re
import spacy
import pandas as pd
from rake_nltk import Rake



with open ('corpusStopLimpio.txt',encoding="utf8") as corpusEntrada:
	corpus = corpusEntrada.read()
	

corpus = re.split("\n", corpus)


r = Rake()
		
indices = []
listaRanks = []
for i in corpus:
    r.extract_keywords_from_text(i)
    listaRanks.append(r.get_ranked_phrases_with_scores())
    indices.append(i)
    

dataframe = pd.DataFrame()


dataframe['Noticia'] = indices
dataframe['Palabras Clave'] = listaRanks

dataframe1= dataframe
print(dataframe)

dataframe.to_csv("TablaCompleta.csv")