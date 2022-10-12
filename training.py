#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np


<<<<<<< HEAD
def estimation(x, theta):
    
    return theta[0] + x * theta[1]
=======
def estimation(x, t0, t1):
    return t0 + (x * t1)
>>>>>>> cc797f96b8339ea50ddaa7227a35e0cccc2cb2ad

theta = [0.0,0.0]
data = pandas.read_csv("./data.csv")

<<<<<<< HEAD
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

=======

mileage = data.km
price = data.price
print(price[0])
lr = 0.15
m = len(price)
std = mileage[0:].std()
mean = mileage[0:].mean()
kmtrage = (mileage[0:] - mean) / std
# for d in range(m):
    # mileage[d] = (mileage[d] - mean) / std

for z in range(19):
    tmp = [0,0]
    for i in range(m):
        tmpp = estimation(kmtrage[i], theta[0], theta[1]) - price[i]
        tmp[0] += tmpp
        tmp[1] += tmpp * kmtrage[i]
    theta[0] -= lr/m * tmp[0]
    theta[1] -= lr/m * tmp[1]
print(lr)
print(m)

print(theta[0])
print(theta[1])

i = 0

# for i in range(m):
    # price[i] = theta[0] + theta[1] * mileage[i]

# plt.plot(mileage, data['price'], markersize=4)
# plt.show()


print(estimation((42000-mean)/std, theta[0], theta[1]))
>>>>>>> cc797f96b8339ea50ddaa7227a35e0cccc2cb2ad
