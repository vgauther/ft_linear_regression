#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:12:11 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from src import Prediction

# fonction lineaire
def estimation(x, theta):
    return theta[0] + x * theta[1]

def main():
    # valeur initial de theta0 et theta1
    theta = [0.0,0.0]

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

    pr = Prediction(0, 0)
    pr.training(100, lr, m, mileage_norm, price)
    pr.scale(mileage_norm, mileage)

    # save des tetha
    pr.save_model()

    # on replace les données normalisé sur la nouvelle droite
    Yn = pr.theta1 * mileage + pr.theta0

    # tetha finaux
    thetanew = [pr.theta0, pr.theta1]

    # affichage des points d'or
    plt.plot(mileage, Yn, markersize=4)
    plt.plot(mileage, price,'ro', color='g')
    plt.show()

if __name__ == "__main__":
    main()
