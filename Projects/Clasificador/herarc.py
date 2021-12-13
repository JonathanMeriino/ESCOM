import numpy as np
import pandas as pd
import nltk
import re
import os as os
import codecs
from sklearn import feature_extraction
import mpld3
from nltk.stem.snowball import SnowballStemmer

#nltk.download('stopwords')

datos= pd.read_csv('grimms.csv') # lectura del dataframe

#print(datos)

stopwords = nltk.corpus.stopwords.words('spanish')

print(stopwords)

stemmer = SnowballStemmer('english')  # descomponer una palabra en su raiz
