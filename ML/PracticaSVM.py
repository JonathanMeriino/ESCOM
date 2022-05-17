#Benitez Merino Leonardo Jonathan
from math import sqrt
from sklearn.svm import SVR
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

#cargar el dataset
data = datasets.load_wine()
#print(data.DESCR)

x=data.data
y=data.target 
print("Wine Recognition Dataset")
#reescalando los datos
scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_X = scaler.fit_transform(x)

x_train,x_test,y_train, y_test = train_test_split(rescaled_X,y,train_size=.35,shuffle=True)

svr_model = SVR(gamma='scale')
svr_model.fit(x_train,y_train)
predictions = svr_model.predict(x_test)
print("Metrica Datos Reescalados:" , sqrt(mean_squared_error(y_test,predictions)))

# estandarizando los datos
scaler = StandardScaler().fit(x)
standardize_X = scaler.transform(x)

x_train,x_test,y_train, y_test = train_test_split(standardize_X,y,train_size=.35,shuffle=True)
svr_model = SVR(gamma='scale')
svr_model.fit(x_train,y_train)
predictions = svr_model.predict(x_test)

print("Metrica Datos Estandarizados: " , sqrt(mean_squared_error(y_test,predictions)))

print("Fetch California Housing")

data = datasets.fetch_california_housing()

x=data.data
y=data.target 

#Datos de entrenamiento del 90%
x_train,x_test,y_train, y_test = train_test_split(x,y,train_size=.90,shuffle=True)
svr_model = SVR(gamma='scale')
svr_model.fit(x_train,y_train)
predictions = svr_model.predict(x_test)
print("Metrica Datos 90%:" , sqrt(mean_squared_error(y_test,predictions)))

#Datos de entrenamiento del 30%
x_train,x_test,y_train, y_test = train_test_split(x,y,train_size=.30,shuffle=True)
svr_model = SVR(gamma='scale')
svr_model.fit(x_train,y_train)
predictions = svr_model.predict(x_test)
print("Metrica Datos 30%:" , sqrt(mean_squared_error(y_test,predictions)))