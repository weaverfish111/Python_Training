## Random Walk
## Richard Weaver
## 15/03/2022

import math
import numpy as np
import matplotlib.pyplot as plt
import random

x, y = 0, 0
x_coordinates = []
y_coordinates = []
Radius = 0

for steps in (0, 200, 1):
    Radius += 1
    angle = random.randint(1, 360)

    x = angle +1
    y = angle +1
    x_coordinates = x_coordinates.append(x)
    y_coordinates = y_coordinates.append(y)


    
    ## Plotting Graph
    plt.plot(x, y, 'bo', markersize = 10)  # blue point
    plt.plot(x_coordinates, y_coordinates, 'r-')
    plt.plot
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # update graph
    plt.draw()
    plt.pause(0.001)

    # clear graph
plt.clf()
