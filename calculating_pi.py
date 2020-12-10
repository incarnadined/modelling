import numpy as np
import matplotlib.pyplot as plt
import random
from latin_hypercubes import latin_hypercubes

'''
This program calculates pi using a circle radius one and the square that inscribes the circle

area of square*(number of random points that fall in the circle/total points) = pi

It then plots the number of points on the x axis against the value of pi that those points converge on.
The three lines plotted are:
    the value of pi according to numpy (dark blue)
    the value of pi according to np.random.uniform (red)
    the value of pi according to my latin hypercubes code (cyan)
The most accurate represntation should be the cyan line
'''

def gen_points_latinrandom(size):
    circle_points = 0

    x = latin_hypercubes(-1, 1, size)
    y = latin_hypercubes(-1, 1, size)

    for i in range(size):
        if x[i]**2+y[i]**2 <= 1:
            circle_points+=1

    return circle_points

def gen_points_nprandom(size):
    circle_points = 0

    x = np.random.uniform(-1.0, 1.0, size=size)
    y = np.random.uniform(-1.0, 1.0, size=size)

    for i in range(size):
        if x[i]**2+y[i]**2 <= 1:
            circle_points+=1

    return circle_points

def main():
    step = 10
    low = 500
    high = 10000
    xnp = []
    ynp = []
    xlatin = []
    ylatin = []


    for i in range(low, high, step):
        xnp.append(i)
        ynp.append(4*(gen_points_nprandom(i)/i))

    for i in range(low, high, step):
        xlatin.append(i)
        ylatin.append(4*(gen_points_latinrandom(i)/i))

    plt.figure()
    plt.plot(xnp, ynp, '-r')
    plt.plot(xlatin, ylatin, '-c')
    plt.plot(xnp, np.full(len(xnp), np.pi), '-b')

    plt.xlabel('Number of points')
    plt.ylabel('Pi')

    plt.show()
    return

if __name__=='__main__':
    main()