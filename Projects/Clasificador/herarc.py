import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
# librerias para pre-procesamiento
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn import preprocessing


datos= pd.read_csv('HollywoodscuemarvelStories.csv') # lectura del dataframe

print(datos)


