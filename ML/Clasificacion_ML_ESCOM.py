#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 6 7:10:56 2022

@author: usuario
"""
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

data = datasets.load_iris()

X = data.data
y = data.target

print(X[0:5,:])

scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_X = scaler.fit_transform(X)

rescaled_X[0:5,:]

#%%
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

data = datasets.load_iris()
X = data.data
y = data.target
print(X[0:5,:])

scaler = StandardScaler().fit(X)
standardize_X = scaler.transform(X)

print(standardize_X[0:5,:])
#%%
from sklearn import datasets
from sklearn.preprocessing import Normalizer

data = datasets.load_iris()

X = data.data
y = data.target

print(X[0:5,:])

scaler = Normalizer().fit(X)
normalize_X = scaler.transform(X)


print(normalize_X[0:5,:])
#%%%

from sklearn import datasets
from sklearn.preprocessing import Binarizer

data = datasets.load_iris()

X = data.data
y = data.target

print(X[0:5,:])

scaler = Binarizer(threshold = 1.5).fit(X)
binarize_X = scaler.transform(X)

print(binarize_X[0:5,:])

#%%%

from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#from sklearn.datasets import fetch_california_housing

#housing = fetch_california_housing()
#print(housing.DESCR)
#print(housing.data)
#print(housing.target)
data = datasets.load_iris()
descp=data.DESCR
print(descp)
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)

svc_model = SVC(gamma='scale')

svc_model.fit(X_train, y_train)

predictions = svc_model.predict(X_test)

s= X_test.shape

X_test[:,0]=predictions.T

print(X_test)

print("Accuracy: ",  accuracy_score(y_test, predictions))
#%%%

#Importamos los paquetes que utilizaremos

from sklearn.svm import SVR 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

#cargamos nuestro dataset
data= datasets.load_boston()
print(data.DESCR)
#separamos los datos  que utilizaremos
X=data.data
y=data.target

#Separamos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test =train_test_split(X,y, shuffle= True)


#Creamos nuestro modelo

svr_model= SVR(gamma='scale')

#Entremos a nuestro modelo

svr_model.fit(X_train, y_train)

#Creamos las predicciones

predictions= svr_model.predict(X_test)

X_test[:,0]=predictions.T

print("Metrica mean_squared_error: %.2f "% sqrt(mean_squared_error(y_test,predictions)))
 
#%%%
