#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:13:37 2022

@author: anthelme
"""

class Prediction():
    
    def __init__(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1
        self.mileage = input ("mileage ?")
        while self.mileage.isnumeric() == False:
            print("Ce n'est pas un nombre, veuillez recommencer espece de con ")
            self.mileage = (input ("mileage ?"))
        self.mileage = float(self.mileage)
    
    def prediction(self):
        estimatedprice = self.theta0 + self.mileage * self.theta1
        return estimatedprice
        
    
