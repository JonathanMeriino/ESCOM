from numpy import size
import re

#Funcion principal usada para identificar el tipo de gramatica
def main():
  producciones = [[],[]]
  op = "0"

  #Se agregan reglas de producccion segun la respuesta del usuario
  while(op == "0"):
    producciones[0].append(input("Ingrese el lado izquierdo de la regla de producción:"))
    producciones[1].append(input("Ingrese el lado derecho de la regla de producción:"))
    op = input("Desea ingresar otra regla de procucción? (0-Si, 1-No): ")

  #Se imprimen las reglas ingresadas
  print("Reglas de producción")
  for i in range(size(producciones[0])):
    print(f"{producciones[0][i]} --> {producciones[1][i]}")

  #Se llama a las funciones de evaluacion
  if(evaluarTipo0(producciones[0])):
    if(evaluarTipo1(producciones[0],producciones[1])):
      if(evaluarTipo2(producciones[0],producciones[1])):
        if(evaluarTipo3(producciones[0],producciones[1])):
          return print("Es una gramatica tipo 3 Regular")
        return print("Es una gramatica tipo 2 Independiente de contexto")
      return print("Es una gramatica tipo 1 Sensible al contexto")
    return print("Es una gramatica tipo 0 sin restricciones")
  return print("Es una gramatica no identificable")
        
#Solo se necesita la parte izquierda de la regla, debe contener almenos un SNT
def evaluarTipo0(izq):
  for i in range(size(izq)):
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

#Funcion para evaluar las reglas de una gramatica tipo 1
#Parte anterior y posterior de un simbolo terminal de la parte izquierda
#se conservan en la parte derecha,(Dichas partes pueden ser cualquier combinacion
# de terminales o no terminales)
def evaluarTipo1(izq, der):
  for i in range(size(izq)):
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

#Debe cumplir que la izquierda solo un SNT y en la derecha cualquier secuencia de
#terminales o no terminales
def evaluarTipo2(izq, der):
  for i in range(size(izq)):
    tipo2i = re.compile(r"[A-Z]")
    tipo2d = re.compile(r"\D*")

    x = tipo2i.search(izq[i])
    y = tipo2d.search(der[i])

    if(x and y and len(izq[i]) == 1):
      continue
    else:
      return 0

  return 1

#Debe cumplir que la izquierda solo un SNT y en la derecha una de las sig combinaciones
#(SNT SNT), (ST ST), (ST SNT), (ST), (SNT), (cadena vacia)
#terminales o no terminales
def evaluarTipo3(izq, der):
  for i in range(size(izq)):
    tipo2i = re.compile(r"[A-Z]")
    tipo2d = re.compile(r"([a-z][A-Z]|[a-z]*$|[A-Z]*$)")

    x = tipo2i.search(izq[i])
    y = tipo2d.match(der[i])

    if(x and y and len(izq[i]) == 1 and len(der[i]) <= 2):
      continue
    else:
      return 0

  return 1


#llamada a funcion principal
main()