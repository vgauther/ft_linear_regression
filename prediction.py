#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:13:37 2022

@author: anthelme
"""

import pandas
import matplotlib.pyplot as plt
from src import Prediction

def main():

    #on recupère les tetha de l'algo de training
    filename = './model.csv'
    model_file = pandas.read_csv(filename, header=None)
    pr = Prediction(model_file.iloc[0, 0], model_file.iloc[0, 1])

    # on demande le kmtrage de la voiture
    mileage = (input ("What is the mileage of your car ?"))
    while mileage.isnumeric() == False:
         print("You have to put a number. exemple : 42000")
         mileage = (input ("What is the mileage of your car ?"))

    #on lance la prediction
    predicted_price = pr.predict(float(mileage))

    #on affiche le résultat
    print("The price of your car is : " + str(predicted_price) + "$")

if __name__ == "__main__":
    main()
