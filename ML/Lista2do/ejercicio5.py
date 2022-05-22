"""
Ejercicio 5
Benitez Merino Leonardo Jonathan
"""

import pandas as pd
from sklearn import datasets

#datasetIris = datasets.load_iris()

boston = datasets.load_boston()


dataframe = pd.DataFrame(index= None, columns=['Dataset Name','Observations','Dimensions','Features','Targets'])


dataframe['Dataset Name']=["Boston"]
dataframe['Observations'] =["506"]
dataframe['Dimensions'] =["13"]
dataframe['Features'] = [boston.feature_names]
dataframe['Targets'] =[boston.target]

print(dataframe)

"""
,[datasets.load_diabetes().filename],[datasets.load_iris().filename], [datasets.load_breast_cancer().filename],[datasets.load_wine().filename]
,[datasets.load_diabetes(return_X=True)], [datasets.load_iris(return_X=True)], [datasets.load_breast_cancer(return_X=True)],[datasets.load_wine(return_X=True)]
,[datasets.load_diabetes().shape[1]], [datasets.load_iris().shape[1]], [datasets.load_breast_cancer().shape[1]],[datasets.load_wine().shape[1]]
,[datasets.load_diabetes().feature_names],[datasets.load_iris().feature_names], [datasets.load_breast_cancer().feature_names],[datasets.load_wine().feature_names]
,[datasets.load_diabetes().target_names], [datasets.load_iris().target_names], [datasets.load_breast_cancer().target_names],[datasets.load_wine().target_names]

"""