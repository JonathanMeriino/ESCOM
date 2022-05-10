#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.

import operator
import math
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

# Define new functions
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

pset = gp.PrimitiveSet("MAIN", 2)  #Conjunto primitivo 
#Añade las primitivas
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(operator.neg, 1)
pset.addPrimitive(math.cos, 1)
pset.addPrimitive(math.sin, 1)
#Añade una constante efimera al conjunto (nombre , constante efimera)
#pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
#Renombra los argumentos de la funcion con nuevos nombres (**kargs)
pset.renameArguments(ARG0='x')
pset.renameArguments(ARG1='y')
#Creacion de las clases
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # (Nombre de la clase, clase de la que hereda, atributos )
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

#creacion del objeto
toolbox = base.Toolbox()
#(expresion de arbol para convertir en un arbol,metodo: mitad full y mitad grown,conjunto primitivo, altura min y max de los arboles producidos )
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
#(nombre, llama al contenedor de funciones con un unico iterable como unico argumento, argumentos de palabras clave)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
#(nombre, regresa una instancia del contenedor lleno de datos)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# clase para compilar un conjunto que devuelve los resultados al evaluar el arbol
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual, points,p2):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Evaluate the mean squared error between the expression
    # and the real function : x**4 + x**3 + x**2 + x
    sqerrors = ((func(x,y) - x**2 - y**2)**2 for x,y in zip(points,p2))
    return math.fsum(sqerrors) / len(points)
#evaluacion de la funcion
toolbox.register("evaluate", evalSymbReg, points=[x/10. for x in range(-10,10)],points2=[y/10. for y in range(-10,10)])
#seleccion por torneo de tamaño 3
toolbox.register("select", tools.selTournament, tournsize=3)
#operacion de cruza de 1 punto
toolbox.register("mate", gp.cxOnePoint)
# Genera una expresion donde cada hoja tenga la misma profundidad entre min y max
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
# aleatoriamente selecciona un punto en el arbol, reemplaza el subarbol en ese punto como raiz por la expresion generada mediante el metodo expr
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
# se implementa un limite en el arbol, cuando se genera un hijo no valido(por encima del limite) se reemplaza por uno de sus padres

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))#(establece un limite de tamaño, valor maximo permitido para la medicion dada)
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

def main():
    random.seed(318)

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)
    #inicializacion del algoritmo
    pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats,
                                   halloffame=hof, verbose=True)
    # print log

    for i in hof:
        print(i)
        print(evalSymbReg(i,points=[x/10. for x in range(-10,10)],points2=[y/10. for y in range(-10,10)]))

    return pop, log, hof
if __name__ == "__main__":
    main()