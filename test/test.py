#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:40:09 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np 

data = pandas.read_csv("./data.csv")

mileage = data.km
price = data.price
pricenv=price


# On décompose le dataset et on le transforme en matrices pour pouvoir effectuer notre calcul
X = np.matrix([np.ones(data.shape[0]), data['km']]).T
y = np.matrix(data['price']).T

# On effectue le calcul exact du paramètre theta
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print(theta)

plt.xlabel('km')
plt.ylabel('price')


m =len(X)
for i in range(m): 
    X[i,1] = theta[0] + theta[1] * y[i]
    
plt.plot(X[:,1], y, 'ro', markersize=4)
plt.show()
