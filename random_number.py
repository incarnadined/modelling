import numpy as np
import matplotlib.pyplot as plt
import random

def gen_random_numbers(size):
    x = np.random.uniform(0.0, 1.0, size=size)
    avg = np.mean(x)

    return avg

def main():
    x = []
    y = []

    for i in range(1, 100000, 100):
        x.append(i)
        y.append(gen_random_numbers(i))

    plt.figure()
    plt.plot(x, y, '-r')

    plt.xlabel('Length of list of random numbers')
    plt.ylabel('Average of random numbers in the list')

    plt.show()
    return

if __name__=='__main__':
    main()