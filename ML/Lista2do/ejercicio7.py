from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
#cargar del dataset
dataset = datasets.load_wine()

x = dataset.data
y= dataset.target
#Datos de entrenamiento del 30%
x_train , x_test, y_train, y_test = train_test_split(x,y, train_size=0.3)

svc_model = SVC()
svc_model.fit(x_train, y_train)
pred = svc_model.predict(x_test)

print(f"Train data de 30%:{accuracy_score(y_test, pred)}")
#SVC con datos de testeo
svc_model.fit(x_test, y_test)
pred = svc_model.predict(x_train)
print(f"Test data de 30%:{accuracy_score(y_train, pred)}")

#Datos de entrenamiento del 70%
x_train , x_test, y_train, y_test = train_test_split(x,y, train_size=0.70)

svc_model = SVC()
svc_model.fit(x_train, y_train)
pred = svc_model.predict(x_test)
print(f"Train test de 70%:{accuracy_score(y_test, pred)}")

svc_model.fit(x_test, y_test)
pred = svc_model.predict(x_train)
print(f"Test data de 70%:{accuracy_score(y_train, pred)}")

"""
No existe overfiting, ya que al implementar las metricas, la brecha entre el
desempeño de los datos de entrenamiento y los datos de prueba no es muy amplia, por
lo que nuestro modelo esta aprendiendo, no memorizando
"""