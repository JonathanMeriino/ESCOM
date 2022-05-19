#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:07:28 2022

@author: usuario
"""
#Importamos las bibliotecas que utilizaremos
import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib
import numpy as np



# Generamos nuestro dataser utilizando la biblioteca SKLEARN, NO lineal


np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.1)



#Graficamos los datos simulados
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)



# Asignamos la tasa de aprendizaje
learningRate = 0.01


oneVector = np.ones((X.shape[0], 1))
X_train = np.concatenate((oneVector, X), axis=1)


plotData = []

#Asignamos pesos aleatorios
weights = np.random.rand(3, 1)

misClassifications = 1
minMisclassifications = 10000
#Inicializamos el contador del ciclo
iteration = 0

# Codigo del algoritmo principal
while (misClassifications != 0 and (iteration<1000)):
    iteration += 1
    misClassifications = 0

    for i in range(0, len(X_train)):
        currentX = X_train[i].reshape(-1, X_train.shape[1])
        currentY = y[i]
        wTx = np.dot(currentX, weights)[0][0]
        
        if currentY == 1 and wTx < 0:
            misClassifications += 1
            weights = weights + learningRate * np.transpose(currentX)
        elif currentY == 0 and wTx > 0:
            misClassifications += 1
            weights = weights - learningRate * np.transpose(currentX)
    plotData.append(misClassifications)
    
    if misClassifications<minMisclassifications:
        minMisclassifications = misClassifications
   
    

#Graficamos los datos con la linea y=wx+b
def plot_hyperplane(X, Y, weights, bias):
    """
    Plots the dataset and the estimated decision hyperplane
    """
    print(y)
    slope = - weights[1]/weights[2]
    intercept = - bias/weights[1]
    x_hyperplane = np.linspace(-2,3,10)
    y_hyperplane = slope * x_hyperplane + intercept
    plt.figure(figsize=(8,6))
    plt.scatter(X[:,0], X[:,1], c=Y, cmap=plt.cm.Spectral)
    plt.plot(x_hyperplane, y_hyperplane, '-')
    plt.title("Dataset and fitted decision hyperplane")
    plt.xlabel("First feature")
    plt.ylabel("Second feature")
    plt.show()
    
    
plot_hyperplane(X, y, weights,weights[0] ) 