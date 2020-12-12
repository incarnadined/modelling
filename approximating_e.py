import numpy as np
import matplotlib.pyplot as plt
import random
from latin_hypercubes import latin_hypercubes

'''
This program approximates e (Euler's number)

The graph shows the number of trials against their average (should tend to e)
'''

def count_to_one():
    '''
    A function that generates random numbers between 0 and 1 until their sum exceeds 1

    Returns the number of numbers required to exceed 1
    '''

    t = 0
    rand = []

    while t < 1:
        rand.append(random.uniform(0.0, 1.0))
        t += rand[-1]

    return len(rand)

def main():
    # Number of trials to be run. Higher it is, the more accurate e will be
    trials = 1000
    x = []
    y = []
    
    for trial in range(1, trials+1):
        current_value = 0

        numbers_required = count_to_one()
        e_rolling_avg = (sum(y)+numbers_required)/(len(y)+1)

        x.append(trial)
        y.append(e_rolling_avg)

    plt.figure()

    approx_e, = plt.plot(x, y, '-r', label='approximation of e')
    e, = plt.plot(x, np.full(np.shape(y), np.e), label='numpy value of e')

    # plot the legend for the different lines
    plt.legend(handles=[approx_e, e])

    plt.xlabel('Number of trials')
    plt.ylabel('e approximation')

    plt.show()
    return

if __name__=='__main__':
    main()