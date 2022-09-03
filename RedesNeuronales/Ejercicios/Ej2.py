#Implementar un vector en R3 en numpy
import numpy as np

#declaracion del array
A = np.array([0.3, 0.6, 0.9])

alpha = 0.1 #valor escalar

#asignacion de la multiplicacion del escalar por el array
res=A*alpha

print(f"Resultado de alpha*A: {res}") #Imprimir en pantalla el resultado

B = A*res

print(f"Resultado de B: {B}")

# Pendiente C

#Parte 2

#Declaracion de los arrays
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
#Multiplicacion de matrix 2x3*3x2
C = np.dot(A,B)
print(f"Valor de C: {C}")#Impresion de C

D = np.transpose(C) #Funcion para calcular la matriz transpuesta de C

print(f"Matriz Transpuesta: {D}") #Impresion D


