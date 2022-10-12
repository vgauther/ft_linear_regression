#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022
@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt


def estimation(x, t0, t1):
    return t0 + (x * t1)

theta = [0.0,0.0]
data = pandas.read_csv("./data.csv")


mileage = data.km
price = data.price
print(price[0])
lr = 0.15
m = len(price)
std = mileage.std()
mean = mileage.mean()
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