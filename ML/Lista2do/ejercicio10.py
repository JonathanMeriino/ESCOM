from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#dataset wine Ejercicio 7
dataWine = datasets.load_wine()
print("Dataset Wine")
xw = dataWine.data
yw = dataWine.target

x_train , x_test, y_train, y_test = train_test_split(xw,yw, train_size=0.20, shuffle=True)

model_RT= tree.DecisionTreeRegressor()
model_RT.fit(x_train,y_train)
y_pred = model_RT.predict(x_test)

print(f"Acurracy_score Train: {accuracy_score(y_test,y_pred)}")

model_RT.fit(x_test,y_test)
y_pred = model_RT.predict(x_train)
print(f"Acurracy_score Test: {accuracy_score(y_train,y_pred)}")


#dataset diabetes Ejercicio 8
dataDiabetes = datasets.load_diabetes()
print("Dataset Diabetes")
xd = dataWine.data
yd = dataWine.target

x_train , x_test, y_train, y_test = train_test_split(xd,yd, train_size=0.20, shuffle=True)

model_RT.fit(x_train,y_train)
y_pred = model_RT.predict(x_test)

print(f"Acurracy_score Train: {accuracy_score(y_test,y_pred)}")

model_RT.fit(x_test,y_test)
y_pred = model_RT.predict(x_train)
print(f"Acurracy_score Test: {accuracy_score(y_train,y_pred)}")