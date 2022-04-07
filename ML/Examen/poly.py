import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
X = np.random.rand(10,1)
y = 5*((X)**(2)) + np.random.rand(10,1)


#funcion de perdida

def Perdida(y,y_hat):
    # y -> valor verdadero/objetivo
    # y_hat - > hipotesis

    #calculo de perdida
    loss = np.mean((y_hat-y)**2)

    return loss

#calculo del gradiente

def Gradientes(X, y, y_hat):
    """
    x - > entrada
    y -> valor verdadero/objetivo
    y_hat - > hipotesis
    w -> pesos
    b -> sesgo
    """
    m = X.shape[0] # numero de ejemplos de entrenamiento

    # Gradiente de pérdida respecto a los pesos. 
    dw = (1/m)*np.dot(X, (y_hat - y))
    
     # Gradiente de pérdida con sesgo. 
    db = (1/m)*np.sum((y_hat - y)) 
    
    return dw, db

#funcion para agregar caracteristicas a los datos de entrada

def x_transform(X, grados):


    # grados --> Una lista, agregamos la característica X^(valor) a la entrada 
    # donde el valor es uno de los valores en la lista. 
    
    # haciendo una copia de X. 
    t = X.copy()
    
     # Agregando columnas de grados más altos a X. 
    for i in grados: 
        X = np.append(X, t**i, axis=1) 
            
    return X

def train(X,y,bs, grados,etapa,lr):

    # bs --> Tamaño del lote. 
    # etapa --> Número de iteraciones. 
    # grados --> Una lista, agregamos la característica X^(valor) a la entrada 
    # donde el valor es uno de los valores en la lista. 
    # lr --> Tasa de aprendizaje. 
    
    # Adición de características a la entrada X. 
    x = x_transform(X, grados)
    
     # m-> número de ejemplos de entrenamiento 
    # n-> número de características 
    m, n = x.shape
    
     # Inicialización de pesos y sesgo a ceros. 
    w = np.zeros((n,1)) 
    b = 0
    
     # Reformando y. 
    y = y.reshape(m,1)
    
     # Lista vacía para almacenar pérdidas. 
    loss = []
    
    # Bucle de entrenamiento. 
    for epoch in range(etapa): 
        for i in range((m-1)//bs + 1):
            
             # Definición de lotes. 
            start_i = i*bs 
            end_i = start_i + bs 
            xb = x[start_i:end_i] 
            yb = y[start_i:end_i]
            
             # Cálculo de la hipótesis 
            y_hat = np.dot(xb, w) + b
            
             # Obtener los gradientes de los parámetros wrt de pérdida. 
            dw, db = Gradientes(xb, yb, y_hat)
            
             # Actualización de los parámetros. 
            w -= lr*dw 
            b -= lr*db
        
         # Calculando la pérdida y agregándola a la lista. 
        l = loss(y, np.dot(x, w) + b) 
        loss.append(l)
        
     # devolviendo ponderaciones, sesgos y loss(Lista).
    return w, b, loss
# Función de predicción.
def predecir(X, w, b, grados):
    
    # X --> Entrada. 
    # w --> pesos (parámetro). 
    # b --> sesgo (parámetro). 
    #grados --> Una lista, agregamos la característica X^(valor) a la entrada 
    # donde el valor es uno de los valores en la lista. 
    
    # Agregar grados a la entrada X. 
    x1 = x_transform(X, grados)
    
     # Devolver predicciones. 
    return np.dot(x1, w) + b
