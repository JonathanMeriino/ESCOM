"""
    Benitez Merino Leonardo Jonathan
    Practica 1 - Algoritmos bioinspirados
"""

import random

#1. Generar una poblacion inicial
pob_inicial = []
pobInicial_bin = []
for _ in range(5):
    aux=(random.randrange(0,15))
    aux2 = format(aux,'b')
    pob_inicial.append(aux)
    pobInicial_bin.append(aux2)

print("Individuos: ",pob_inicial)
print("Individuos binario: ",pobInicial_bin)




#2. Realizar la seleccion de padres usando el metodo de la ruleta


#3. Realizar la cruza de los padres usando el metodo recombincaion de 1 punto

#4. Reakuzar la mutacion 


#5. Realizar el remplazo del padre mas debil



#6.La condicion de paro