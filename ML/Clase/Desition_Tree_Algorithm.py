#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 07:54:27 2022

@author: usuario
"""

"""
IMPLEMENTACION DE ARBOL DE DESICION PARA CLASIFICACION UTILIZANDO LA 

BIBLIOTECA SKLEARN.
"""

#Importamos los paquetes que utilizaremos

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Cargamos nuestro dataset

data= datasets.load_iris()

# Separamos los vectores de caracteristicas y sus etiquetas
X=data.data
y=data.target

#Dividimos los datos en entrenamiento y prueba
X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=True)

#Creamos nuestro nuevo modelo/objeto 
tree_Clasifier= DecisionTreeClassifier()


#Entrenamos nuestro modelo
tree_Clasifier.fit(X_train,y_train)



#Creamos las predicciones para los datos de prueba

predictions= tree_Clasifier.predict(X_test)

#Evaluamos el desempen~o del modelo en los datos de prueba

print("Exactitud: %.2f "% accuracy_score(y_test,predictions))
#%%%


"""
IMPLEMENTACION DE ARBOL DE DESICION PARA REGRESION UTILIZANDO LA 

BIBLIOTECA SKLEARN.
"""

#Importamos los paquetes que utilizaremos

from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

#cargamos nuestra dataset

data= datasets.load_boston()

# Separamos los datos que utilizaremos, los vectores de caracteristicas
# y las etiquetas

X= data.data
y= data.target

# Dividimos los datos de entrenamiento y prueba

X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=True)

#Creamos el modelo de regresion  
tree_reg= DecisionTreeRegressor()

#Entrenamos nuestro modelo

tree_reg.fit(X_train, y_train)

#Creamo0s las predicciones respecto a los datos de prueba

predictions =tree_reg.predict(X_test)

#Evaluamos el desempen~o del metodo

print("Error cuadratico medio: %.2f"% sqrt(mean_squared_error(y_test,predictions)))




