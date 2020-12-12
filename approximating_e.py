import numpy as np
import matplotlib.pyplot as plt
import random
from latin_hypercubes import latin_hypercubes

'''
This program approximates e (Euler's number).

Each trial consists of taking uniformally distributed random numbers between zero and one and adding them together until the sum exceeds one.
At that point, count the number of random numbers you added together. This is the result of each trial (typically 2-3).
As you repeat trials, and average out the result of each, you converge on e.


The graph shows an approximation of e according to pythons built-in random module (red), an approximation according to numpy randomness (cyan), and the numpy recorded value for e (blue)
'''

# Wrapper functions to manage arguements properly
def random_random(low: float, high: float) -> float:
    '''
    Function that takes two bounds and returns a random number between them using the random module's rand function
    '''
    return random.uniform(low, high)

def numpy_random(low: float, high: float) -> float:
    '''
    Function that takes returns a random number using the numpy module's rand function

    The np.rand() function requires no bounds. All return values are in the range 0<=x<=1
    '''
    return np.random.rand()


def count_to_one(random_function):
    '''
    A function that generates random numbers between 0 and 1 until their sum exceeds 1

    Returns the number of numbers required to exceed 1
    '''

    t = 0
    rand = []

    while t < 1:
        rand.append(random_function(0.0, 1.0))
        t += rand[-1]

    return len(rand)

def main():
    # Number of trials to be run. Higher it is, the more accurate e will be
    num_trials = 10000
    x = []
    ynp = []
    yrandom = []
    trials_np = []
    trials_random = []
    
    for trial in range(1, num_trials+1):
        current_value = 0

        numbers_required_random = count_to_one(random_random)
        numbers_required_np = count_to_one(numpy_random)

        e_rolling_avg_np = (sum(trials_np)+numbers_required_np)/(len(trials_np)+1)
        e_rolling_avg_random = (sum(trials_random)+numbers_required_random)/(len(trials_random)+1)

        x.append(trial)
        ynp.append(e_rolling_avg_np)
        yrandom.append(e_rolling_avg_random)
        trials_random.append(numbers_required_random)
        trials_np.append(numbers_required_np)

    plt.figure()

    np_e, = plt.plot(x, ynp, '-c', label='e according to numpy randomness')
    random_e, = plt.plot(x, yrandom, '-r', label='e according to random randomness')
    e, = plt.plot(x, np.full(np.shape(x), np.e), label='numpy value of e')

    # plot the legend for the different lines
    plt.legend(handles=[np_e, random_e, e])

    plt.xlabel('Number of trials')
    plt.ylabel('e approximation')

    plt.show()
    return

if __name__=='__main__':
    main()