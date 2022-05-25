"""
Benitez Merino Leonardo Jonathan - 5BM1
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import  ensemble
from sklearn.metrics import mean_squared_error
from sklearn import tree

data0 = pd.read_csv("Data0.csv")
x0 = data0.iloc[:,2:5].values
y0 = data0["close"].values
print(data0)

#split de los datos en entrenamiento y prueba
x_train , x_test, y_train, y_test = train_test_split(x0,y0, train_size=0.30)

#crecion del modelo
tree = tree.DecisionTreeRegressor()
#entrenamiento del modelo
tree.fit(x_train,y_train)

#prediccion y evaluacion del modelo
y_pred = tree.predict(x_test)
print(f"El error Arbol de decision: {mean_squared_error(y_test,y_pred)}")

"""Random Forest"""
#creacion del modelo
rand_forest = ensemble.RandomForestRegressor(n_estimators = 10,
            criterion    = 'mse',
            max_depth    = None,
            max_features = 'auto',
            oob_score    = False,
            n_jobs       = -1,
            random_state = 123) 

#entrenamiento del modelo
rand_forest.fit(x_train, y_train)

#prediccion y evaluacion del modelo
y_pred = rand_forest.predict(x_test)
print(f"El error Random Forest: {mean_squared_error(y_test,y_pred)}")