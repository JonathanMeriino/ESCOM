"""
Benitez Merino Leonardo Jonathan - 5BM1
"""
# Importar librerías
from pylab import rand,plot,show,norm

# Clase Perceptron

class Perceptron:
    #inicializacion del perceptron
    def __init__(self):

      
    
      self.w = rand(2)*2-1 # pesos
    
      self.tasaAprendizaje = 0.1 
    #salida del perceptron
    def respuesta(self,x):
    
      y = x[0]*self.w[0]+x[1]*self.w[1] # producto punto entre w y x
    
      if y >= 0:
    
       return 1
    
      else:
    
       return -1
   #actualizacion de los pesos
    def actualizarPesos(self,x,iterError):
        
          self.w[0] += self.tasaAprendizaje*iterError*x[0]
        
          self.w[1] += self.tasaAprendizaje*iterError*x[1]



    def entrenamiento(self,data):
        
          learned = False
        
          iteracion = 0
        
          while not learned:
        
           globalError = 0.0
        
           for x in data: # por cada muestra
        
            r = self.respuesta(x)    
        
            if x[2] != r: # si tenemos un respuesta equivocada
        
             iterError = x[2] - r # respuesta deseada-respuesta actual
        
             self.actualizarPesos(x,iterError)
        
             globalError += abs(iterError)
        
           iteracion += 1
        
           if globalError == 0.0 or iteracion >= 100: # detiene por el criterio
        
            print ('iteraciones {}'.format(iteracion))
        
            learned = True # detiene el aprendizaje

    
#generacion del conjunto de datos de dos dimensiones
def datosGenerados(n):

    xb = (rand(n)*2-1)/2-0.5

    yb = (rand(n)*2-1)/2+0.5

    xr = (rand(n)*2-1)/2+0.5

    yr = (rand(n)*2-1)/2-0.5

    inputs = []

    for i in range(len(xb)):

        inputs.append([xb[i],yb[i],1])

        inputs.append([xr[i],yr[i],-1])

    return inputs



trainset = datosGenerados(30) # generación de datos para entrenar

perceptron = Perceptron()   # Instancia del perceptron

perceptron.entrenamiento(trainset)  # Entrenamiento con el conjunto de datos

testset = datosGenerados(50)  # conjunto de datos para el test.



# Prueba del perceptron

for x in testset:

 r = perceptron.respuesta(x)

 if r != x[2]: # Si la respuesta no es correcta

  print ('error')

 if r == 1:

  plot(x[0],x[1],'ob')  

 else:

  plot(x[0],x[1],'or')



# gráfica de linea de separación

n = norm(perceptron.w)

ww = perceptron.w/n

ww1 = [ww[1],-ww[0]]

ww2 = [-ww[1],ww[0]]

plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'--k')

show()
