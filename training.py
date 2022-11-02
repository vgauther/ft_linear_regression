#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022

@author: vgauther
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from src import Prediction

# fonction lineaire
def estimation(x, theta):
    return theta[0] + x * theta[1]

def cost_function(theta0, theta1,X,Y):
    global_cost  = 0
    for i in range(len(X)):
        cost_i = ((theta0 + (theta1 * X[i])) - Y[i]) * ((theta0 + (theta1 * X[i])) - Y[i])
        global_cost+= cost_i
    return (1 / (2 * len(X))) * global_cost

def main():

    # ouverture du dataset
    data = pandas.read_csv("./data.csv")

    # creation de tableau pour chaque colone
    mileage = np.array(data['km'])
    price = np.array(data['price'])

    # on normalise la data pour faire la regression lineaire
    mileage_norm = (mileage - np.mean(mileage)) / np.std(mileage)

    # learning rate & nombre cas
    lr = 0.2
    m = len(price)
    nb_train=100
    Cost = []

    pr = Prediction(0,0)

    for i in range (nb_train):
        pr.training(lr, m, mileage_norm, price)

        # tetha finaux
        theta = [pr.theta0, pr.theta1]
        Cost.append(cost_function(theta[0], theta[1], mileage_norm, price))

    pr.scale(mileage_norm, mileage)
    pr.save_model()
    Yn = pr.theta1 * mileage + pr.theta0

    plt.xlabel('Nombre d\'iterations')
    plt.ylabel('Cout d\'erreur global')

    plt.plot(Cost,'ro')
    plt.show()

    plt.plot(mileage, Yn, markersize=4)
    plt.plot(mileage, price,'ro')
    plt.show()

if __name__ == "__main__":
    main()
