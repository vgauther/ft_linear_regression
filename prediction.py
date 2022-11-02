#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:13:37 2022

@author: vgauther
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from src import Prediction


def visualizer(user_mileage, predicted_price, t0, t1):
    try:
        data = pandas.read_csv('./data.csv')
        mileage = np.array(data['km'])
        price = np.array(data['price'])

    except FileNotFoundError:
        print("No file data.csv, without dataset the visualizer can't work")
        exit()

    # plt.plot(mileage, price, markersize=4)
    plt.title('Price of car based on mileage')
    plt.xlabel('Mileage (in miles)')
    plt.ylabel('Price (in $)')

    plt.plot(user_mileage, predicted_price, 'o', color='r')
    plt.plot(mileage, price, 'o', color='g')
    plt.show()

def main():

    # on essaye de recupèrer les tetha de l'algo de training
    filename = './model.csv'
    try:
        model_file = pandas.read_csv(filename, header=None)
        pr = Prediction(model_file.iloc[0, 0], model_file.iloc[0, 1])

    except FileNotFoundError:
        print("No file model.csv, the result will not be relevant")
        pr = Prediction(0, 0)

    # on demande le kmtrage de la voiture
    mileage = input("What is the mileage of your car ?")
    while mileage.isnumeric() == False:
         print("You have to put a number. exemple : 42000")
         mileage = input ("What is the mileage of your car ?")

    # on lance la prediction (via la fonction lineaire)
    predicted_price = pr.predict(float(mileage))

    # on affiche le résultat
    print("The price of your car is : " + str(predicted_price) + " $")

    visualizer(mileage, predicted_price, pr.theta0, pr.theta1)

if __name__ == "__main__":
    main()
