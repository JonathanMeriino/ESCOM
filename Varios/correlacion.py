"""
Benitez Merino Leonardo Jonathan
Franco Rodriguez Maria Guadalupe 
"""

#importacion de las bibliotecas
from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np
ecg = electrocardiogram()
fs= 360
time = np.arange(ecg.size) / fs
plt.figure(1)
plt.plot(time,ecg)
plt.xlim(9, 10.2)
plt.ylim(-1, 1.5)
plt.show()
correlacion=np.correlate(ecg,ecg)
#plt.figure()
plt.xcorr(ecg,ecg)
plt.show()