"""
Benitez Merino Leonardo Jonathan - Perceptron
"""

numX= int(input ('ingrese el número de x: '))

x = []
w = []

for _ in range (numX):
    aux = float(input ('Ingrese el valor de x: '))
    aux2 = float(input ( 'ingrese el valor de w: '))
    x.append(aux)
    w.append(aux2) 


print (f'Valor de X: {x} ')
print(f'Valor de los pesos {w}')

#Valor de h
h = [i*j for i,j in zip (x,w) ]

print(f'h: {h}')
h = sum(h)
print(f"Valor de h:{h} ")
#funcion sigmoide

fx = 1 / (1 + 2.71**-h)
#error
y = 0.2
e = fx - y
print(f'error: {e}')
sse = e**2
print(f'sse: {sse}')