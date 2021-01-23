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
    the average value of pi so far (green)
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
    ynpavg = []
    xlatin = []
    ylatin = []
    ylatinavg = []
    yavg = []

    # a variable to keep track of the closest approximation of pi
    closest_guess = 0

    # Approximate pi wihth numpy random sampling
    for i in range(low, high, step):
        pi = 4*(gen_points_nprandom(i)/i)

        if abs(np.pi - pi) < abs(np.pi - closest_guess):
            closest_guess = pi

        xnp.append(i)
        ynp.append(pi)
        ynpavg.append(sum(ynp)/len(ynp))

    # Approximate pi with latin hypercube sampling
    for i in range(low, high, step):
        pi = 4*(gen_points_latinrandom(i)/i)

        if abs(np.pi - pi) < abs(np.pi - closest_guess):
            closest_guess = pi

        xlatin.append(i)
        ylatin.append(pi)
        ylatinavg.append(sum(ylatin)/len(ylatin))

    yavg = [(ylatinavg[x]+ynpavg[x])/2 for x in range(0, len(ylatinavg))]

    plt.figure()

    numpypi, = plt.plot(xnp, ynp, '-r', label='π according to numpy random sampling')
    mypi, = plt.plot(xlatin, ylatin, '-c', label='π according to latin hypercubes sampling')
    avg, = plt.plot(xlatin, yavg, '-g', label='π average')
    actualpi, = plt.plot(xnp, np.full(len(xnp), np.pi), '-b', label='π according to numpy')

    plt.title(f'The closest guess was {closest_guess}')

    # plot the legend for the different lines
    plt.legend(handles=[numpypi, mypi, actualpi])

    plt.xlabel('Number of points')
    plt.ylabel('π approximation')

    plt.show()
    return

if __name__=='__main__':
    main()