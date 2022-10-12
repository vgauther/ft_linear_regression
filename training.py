#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt


def estimation(x):
    global theta
    return theta[0] + x * theta[1]

theta = [0,0]
data = pandas.read_csv("./data.csv")

mileage = data.km
price = data.price
lr = 0.1
m = len(price)

tmp = [0,0]

for i in range (m):
    tmp[0] += (estimation(mileage[i])-price[i])
    tmp[1] += (estimation(mileage[i])-price[i]) * mileage[i]
    
theta[0] = (lr/m) * tmp[0]
theta[1] = (lr/m) * tmp[1]


    
plt.plot(data['km'], data['price'], markersize=4)
plt.show()


print(price)