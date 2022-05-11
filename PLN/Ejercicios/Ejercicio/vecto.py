from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
import os, pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from  sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import  ConfusionMatrixDisplay
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler 
from imblearn.over_sampling import SMOTE
class data_set_polarity:
	def __init__(self, X_train, y_train, X_test, y_test):
		self.X_train = X_train
		self.y_train = y_train
		self.X_test = X_test
		self.y_test = y_test

class data_set_attraction:
	def __init__(self, X_train, y_train, X_test, y_test):
		self.X_train = X_train
		self.y_train = y_train
		self.X_test = X_test
		self.y_test = y_test

if not (os.path.exists('corpus_attraction.pkl')):
	print ('no se ha generado el corpus lematizado')
else:
	corpus_file = open ('corpus_attraction.pkl','rb')
	corpus_attraction = pickle.load(corpus_file)
	corpus_file.close()

if not (os.path.exists('corpus_polarity.pkl')):
	print ('no se ha generado el corpus lematizado')
else:
	corpus_file = open ('corpus_polarity.pkl','rb')
	corpus_polarity = pickle.load(corpus_file)
	corpus_file.close()

#~ print (corpus_attraction.X_train[0])

# Representación vectorial binarizada
vectorizador_binario = TfidfVectorizer(binary=True)
vectorizador_binario_fit = vectorizador_binario.fit(corpus_attraction.X_train)
X_train = vectorizador_binario_fit.transform(corpus_attraction.X_train)
y_train = corpus_attraction.y_train


"""print (vectorizador_binario.get_feature_names_out())
print (X_train.shape)#sparse matrix"""
X_test = vectorizador_binario_fit.transform(corpus_attraction.X_test)
y_test = corpus_attraction.y_test
"""print (vectorizador_binario_fit.get_feature_names_out())
print (X_test.shape)#sparse matrix"""
#print (type(X_train.toarray()))#dense ndarray
#print ('Representación vectorial binarizada')
#print (X_train.toarray())#dense ndarray


def modeloBal(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(max_iter=10000,C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced")
    clf.fit(X_train, y_train)
    return clf

def modelo(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(max_iter=10000,C=1.0,penalty='l2',random_state=1,solver="newton-cg")
    clf.fit(X_train, y_train)
    return clf
def mostrar (y_test, y_pred):
    #print (y_pred)
    #print(accuracy_score(y_test, y_pred))
    #print(confusion_matrix(y_test, y_pred,labels=[1,2,3,4,5]))
    target_names = ['1','2','3','4','5']
    print(classification_report(y_test, y_pred, target_names=target_names))
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.show()
    
def mostrarAtrc(y_test, y_pred):
    #print(confusion_matrix(y_test, y_pred,labels=['Restaurant','Hotel','Attractive']))
    target_names = ['Restaurant','Hotel','Attractive']
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    
model =  modelo(X_train, X_test, y_train, y_test)
modelW =  modeloBal(X_train, X_test, y_train, y_test)


"""Modelo Original"""
print("Modelo Original")
#Atraccion
y_pred = model.predict(X_test)
mostrarAtrc(y_test, y_pred)

#Polaridad
y_train_polarity = corpus_polarity.y_train
model.fit(X_train, y_train_polarity)
y_test = corpus_polarity.y_test
y_pred = model.predict(X_test)
mostrar(y_test, y_pred)


"""Estrategia: Class Weight"""

#Polaridad
modelW.fit(X_train, y_train_polarity)
y_test = corpus_polarity.y_test
y_pred = modelW.predict(X_test)
print("Estrategia: Class Weight")
mostrar(y_test, y_pred)

"""Estrategia: Subsambling"""
print("Estrategia: Subsambling")

#Polaridad
vectorizador_binario_fit = vectorizador_binario.fit(corpus_polarity.X_train)
X_train = vectorizador_binario_fit.transform(corpus_polarity.X_train)
y_train = corpus_polarity.y_train

us = RandomUnderSampler()
X_train_res, y_train_res = us.fit_resample(X_train,y_train)
model = modelo(X_train_res, X_test, y_train_res, y_test)
y_pred = model.predict(X_test)
mostrar(y_test, y_pred)

"""Estrategia: Oversampling"""
print("Estrategia: Oversampling")

#Polaridad
os =  RandomOverSampler()
X_train_res, y_train_res = os.fit_resample(X_train, y_train)

model = modelo(X_train_res, X_test, y_train_res, y_test)

pred_y = model.predict(X_test)
mostrar(y_test, pred_y)

"""Estrategia: sub-over"""

#Polaridad
"""os_us = SMOTE()
X_train_res, y_train_res = os_us.fit_resample(X_train, y_train)
model = modelo(X_train_res, X_test, y_train_res, y_test)
pred_y = model.predict(X_test)
print("Estrategia: sub-over")
mostrar(y_test, pred_y)
"""

