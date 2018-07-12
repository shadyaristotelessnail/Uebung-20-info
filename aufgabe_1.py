# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:04:28 2018

@author: Bongo
"""
import numpy as np
import matplotlib.pyplot as plt

def tropfen(anzahl):
    quad = np.random.uniform(-1, 1, (anzahl,2))
    print(quad)
    print("Quad shape",quad.shape)
    inside = np.sqrt((quad[:,0]**2) + (quad[:,1]**2)) < 1
    inside_number = sum(inside)
    pi_approx = (inside_number*4)/anzahl
    print("pi approximated",pi_approx)
#plot for fun
    plt.plot(quad[:,0], quad[:,1], "o")
    circle1 = plt.Circle((0, 0), 1, color='r')
    plt.gcf().gca().add_artist(circle1)
    plt.show()
    
tropfen(10000000)    