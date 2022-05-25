from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from math import sqrt

#cargar del dataset
dataset = datasets.load_diabetes(as_frame=True)

x= dataset.data
y=dataset.target

x_train , x_test, y_train, y_test = train_test_split(x,y, train_size=0.35)

model_svr = SVR()
model_svr.fit(x_train, y_train)
pred = model_svr.predict(x_test)

print(f"Data Train 35%: {sqrt(mean_squared_error(y_test,pred))}")

#model_svr = SVR()
model_svr.fit(x_test, y_test)
pred = model_svr.predict(x_train)

print(f"Data Test 65%: {sqrt(mean_squared_error(y_train,pred))}")