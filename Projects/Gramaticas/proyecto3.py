import re

def eval(producciones):
  #Se llama a las funciones de evaluacion
  if(evaluarTipo0(producciones[0])):
    if(evaluarTipo1(producciones[0],producciones[1])):
      if(evaluarTipo2(producciones[0],producciones[1])):
        if(evaluarTipo3(producciones[0],producciones[1])):
          mensaje = "Es una gramatica tipo 3 Regular"
          return mensaje
        mensaje = "Es una gramatica tipo 2 Independiente de contexto"
        return mensaje
      mensaje = "Es una gramatica tipo 1 Sensible al contexto"
      return mensaje
    mensaje = "Es una gramatica tipo 0 sin restricciones"
    return mensaje
  mensaje = "Es una gramatica no identificable"
  return mensaje


"""#Tipo 0
### Reglas de Produccion:
*   ***Lado izquierdo -> Debe tener por lo menos un simbolo no terminal***
*   ***Lado derecho -> No tiene restricciones*** 

"""
def evaluarTipo0(izq):
  
  for i in range(len(izq)):
    tipo0 = re.compile(r"[A-Z]+")
    x = tipo0.search(izq[i])

    #Si no cumple la evaluacion regresa 0
    if(not x):
      return 0
      
  return 1

#Funcion para comparar las partes a la izquierda y derecha de un SNT con la parte derecha de 
#la regla de produccion
def comparar(anterior, posterior, der):
  
  ant = re.compile(anterior)

  #Si la parte posterior no es final de cadena realiza la busqueda
  if(posterior != ""):
    pos = re.compile(posterior)
    b = pos.search(der)
  else:
    b = 1

  #Si las expresiones coinciden regresa 1
  if(ant.search(der) and b):    
    return 1
  else:
    return 0


"""#Tipo 1
### Reglas de Produccion:
*   ***Lado izquierdo -> Solo tiene un simbolo No Terminal, se reemplaza por otro simbolo, mientras el resto sigue igual***
*   ***Lado derecho -> No tiene restriccion***
*   Longitud del lado izquierdo siempre debe ser menor o igual que la longitud del lado derecho
"""
def evaluarTipo1(izq, der):
  aux = "".join(der)
  der = aux.split('|')
  for i in range(len(izq)):
    resultado = 0
    cadena = izq[i]
    tipo1 = re.compile(r"[A-Z]")
    for m in tipo1.finditer(cadena):
      #print(m.start(), m.end(), m.group())
      #Si la parte izquierda es solo el SNT se cumple la regla
      if(m.start() == 0 and m.end() == 1 and len(cadena) == 1):
        resultado = 1
        continue
      #Si hay mas que solo el SNT se compara con la parte derecha de la regla de producccion
      else:
        if(comparar(cadena[:m.start()],cadena[m.end():],der[i])):
          resultado = 1
          break
        else:
          continue
    if(resultado == 0):
      return resultado
  return resultado

"""#Tipo 2
### Reglas de Produccion:


*   ***Lado izquierdo -> Un simbolo No terminal***
*   ***Lado derecho -> Cualquier secuencia de terminales o No terminales***
"""
def evaluarTipo2(izq, der):
  aux = "".join(der)
  der = aux.split('|')
  
  for i in range(len(izq)):
    tipo2i = re.compile(r"[A-Z]")
    tipo2d = re.compile(r"\D*")

    x = tipo2i.search(izq[i])
    y = tipo2d.search(der[i])

    if(x and y and len(izq[i]) == 1):
      continue
    else:
      return 0

  return 1

"""#Tipo 3
### Reglas de Produccion:


*   ***Lado izquierdo -> Un simbolo no terminal***
*  *** Lado derecho -> maximo dos simbolos terminales o no terminales, 1 terminal seguido de un SNT, 1 terminal, cadena vacia***

"""
def evaluarTipo3(izq, der):
  aux = "".join(der)

  der = aux.split('|')
  for i in range(len(izq)):
    tipo2i = re.compile(r"[A-Z]")
    tipo2d = re.compile(r"([a-z][A-Z]|[a-z]*$|[A-Z]*$)")

    x = tipo2i.search(izq[i])
    y = tipo2d.match(der[i])

    if(x and y and len(izq[i]) == 1 and len(der[i]) <= 2):
      continue
    else:
      return 0

  return 1
