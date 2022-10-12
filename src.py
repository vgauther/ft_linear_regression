#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:17:49 2022

@author: anthelme
"""

class Prediction():
    
    def __init__(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1
    
    def predict(self, mileage):
        
        return self.theta0 + mileage * self.theta1