# Respuesta a impulsos - forma discreta
# Ejemplo Oppenheim Ejemplo 2.3 p83/pdf111
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
# Rango [a,b], simétrico a 0
b = 15 ; a = -b

alfa = 1.5
u = lambda n: np.piecewise(n,n>=0,[1,0])

x = lambda n: u(n)-u(n-5)
h = lambda n: (alfa**n)*(u(n)-u(n-7))


# PROCEDIMIENTO
ni = np.arange(a,b+1,1)
xi = x(ni)
hi = h(ni)

# Suma de Convolucion x[n]*h[n]
muestras = len(xi)
yi = np.zeros(muestras, dtype=float)
for i in range(0,muestras):
    suma = 0
    for k in range(0,muestras):
        suma = suma + x(ni[k])*h(ni[i]-ni[k])
    yi[i] = suma

# yi = np.convolve(xi,hi,'same')

# SALIDA - GRAFICA
plt.figure(1)
plt.suptitle('Suma de Convolución x[n]*h[n]')

plt.subplot(311)
plt.stem(ni,xi, linefmt='b--',
         markerfmt='bo',basefmt='k-')
plt.ylabel('x[n]')

plt.subplot(312)
plt.stem(ni,hi, linefmt='b--',
         markerfmt='ro',basefmt='k-')
plt.ylabel('h[n]')

plt.subplot(313)
plt.stem(ni,yi, linefmt='g-.',
         markerfmt='mo', basefmt='k-')

plt.ylabel('x[n]*h[n]')
plt.xlabel('n')

plt.show()

yi = np.convolve(xi,hi,'same')

http://blog.espol.edu.ec/telg1001/lti-dt-convolucion-de-suma-python/