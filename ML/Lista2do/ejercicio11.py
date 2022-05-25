import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import max_error
from math import sqrt
data0 = pd.read_csv("Data0.csv")
data1 = pd.read_csv("Data1.csv")


x0 = data0.iloc[:,2:-1].values

y0 = data0["volume"]


x_train , x_test, y_train, y_test = train_test_split(x0,y0, train_size=0.35)

model_svr = svm.LinearSVR()

model_svr.fit(x_train, y_train)
y_pred = model_svr.predict(x_test)

print(f"Acurracy_score Test: {max_error(y_test,y_pred)}")