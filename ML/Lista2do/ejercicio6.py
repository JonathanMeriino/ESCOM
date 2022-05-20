#Library
import numpy as np
from sklearn.impute import SimpleImputer

#creanis el arreglo
arreglo = np.array([[5., np.nan, 8.],
                    [9., 3., 5.],
                   [8., 6., 4.],
                   [np.nan, 5., 2.],
                   [2.,3.,9.],
                   [np.nan, 8., 7.],
                   [1., np.nan,5.]])
print("Array")
print(arreglo)

#transformacion del imputer oara completar valores faltantes por metodo "mean:media"
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')

#ajuste del imputer
imp_mean.fit(arreglo)
print("Array SimpleImputer")
# imprime la nueva matriz con los valores faltates
print(imp_mean.transform(arreglo))