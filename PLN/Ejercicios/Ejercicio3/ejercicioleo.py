import csv
import pandas as pd 

df = pd.read_csv("SavedCorpus.csv")

#for dato in rdatos:
 #   print(dato)
 


#Polaridad de opinion

from polaridad_con_lexicon import *

load_sel()
cadenas = df['titleOpinion'].values


polaridad = getSELFeatures(cadenas,lexicon_sel)