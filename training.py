#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np


def estimation(x, theta):
    
    return theta[0] + x * theta[1]

theta = [0,0]
data = pandas.read_csv("./data.csv")

Xo = np.array(data['km'])
y = np.array(data['price'])

X = (Xo-np.mean(Xo))/np.std(Xo) 

lr = 0.2
m = len(y)

for i in range (100):
    tmp0 = lr*(1/m)*sum(estimation(X) - y)
    tmp1 =lr*(1/m)*sum((estimation(X) - y)*X)

    theta[0] = (theta[0] - tmp0) 
    theta[1] = (theta[1] - tmp1) 
 

P1 = [Xo[0],Xo[6]]
P2 = [estimation(X, theta)[0],estimation(X, theta)[6]]
codir = (P2[1] - P2[0]) / (P1[1] - P1[0])
ordo = P2[0] - codir * P1[0]

Yn = codir * Xo + ordo

thetanew = [ordo, codir]

plt.plot(Xo, Yn, markersize=4)
plt.plot(Xo,y,'ro', color='g')
plt.show()


print(estimation((42000-np.mean(Xo))/np.std(Xo)))
