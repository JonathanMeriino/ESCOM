#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:27:02 2022

@author: jonathan
"""
import numpy as np
from sklearn.impute import SimpleImputer


arreglo = np.array([[5., np.nan, 8.],
                    [9., 3., 5.],
                   [8., 6., 4.],
                   [np.nan, 5., 2.],
                   [2.,3.,9.],
                   [np.nan, 8., 7.],
                   [1., np.nan,5.]])

print(arreglo)

imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')

imp_mean.fit(arreglo)

arrayCLC=imp_mean.transform(arreglo)