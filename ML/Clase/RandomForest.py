#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 07:45:43 2022

@author: usuario
"""
"""

IMPLEMENTACION DEL ALGORITMO DE BOSQUES ALEATORIOS PARA TAREA DE CLASIFICACION

"""
#Importamos los paquetes que utilizaremos

from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#Cargamos el dataset que utilizaremos
data= datasets.load_breast_cancer()

#print(data.DESCR)

#Separamos las caracteristicas en datos y etiquetas

X= data.data

y= data.target

#print(X,y)

#Separamos los datos, en datos de entrenamiento y prueba
#Mezclando los datos y dejandolos sin mezclar

X_train, X_test, y_train, y_test= train_test_split(X,y, shuffle= True)
X1_train, X1_test, y1_train, y1_test= train_test_split(X,y, shuffle= False)

#Creamos nuestros objetos de tipo Bosque clasificador
rf_Classifier= RandomForestClassifier()
rf1_Classifier= RandomForestClassifier()

#Entrenamos nuestros objetos

rf_Classifier.fit(X_train, y_train)
rf1_Classifier.fit(X1_train, y1_train)

#Probamos nuestros clasificadores con los datos de prueba

predicciones= rf_Classifier.predict(X_test)
predicciones1= rf1_Classifier.predict(X1_test)


#Evaluamos el desempeno de nuestros modelos utilizando la metrica accuracy
print("Accuracy : %.2f"% accuracy_score(y_test, predicciones))
print("Accuracy : %.2f"% accuracy_score(y1_test, predicciones1))

#%%%
"""

IMPLEMENTACION DEL ALGORITMO DE BOSQUES ALEATORIOS PARA TAREA DE REGRESION 

"""

from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt


data= datasets.load_diabetes()

print(data.DESCR)

X= data.data

y= data.target
#print(y)
#print(X,y)

#Separamos los datos, en datos de entrenamiento y prueba
#Mezclando los datos y dejandolos sin mezclar

X_train, X_test, y_train, y_test= train_test_split(X,y, shuffle= True)

rf_regressor= RandomForestRegressor()

rf_regressor.fit(X_train, y_train)

print(y_test)
predictions= rf_regressor.predict(X_test)
n= len(y_test)

z=mean_squared_error(y_test,predictions )/n
z= sqrt(z)
print(z)
print(" Raiz del error cuadratico medio: %.2f"% sqrt(mean_squared_error(y_test,predictions )))
