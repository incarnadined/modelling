import numpy as np
import matplotlib.pyplot as plt
import random
from latin_hypercubes import latin_hypercubes

'''

'''

def fibonacci(n):
    phi = complex((1+5**0.5)/2)
    return (phi**n-(-phi)**-n)/complex(5**0.5)


def main():
    step = 0.1
    low = -40
    high = 0

    x = np.arange(low, high, step)
    y = np.array([fibonacci(z) for z in x], dtype=complex)

    fig = plt.figure()

    # for plotting the real part against the imaginary part of the nth number in the sequence
    #plt.plot(y.real, y.imag, '-r')
 
    # for plotting the nth term in the sequence on the complex plane against n
    # NOTE: the titles are small to ensure the scale of the graph is visible when the range is too big
    ax = plt.axes(projection='3d') 
    ax.plot3D(x, y.real, y.imag, '-b')

    ax.set_xlabel('n', fontsize=5)
    ax.set_ylabel('Real part of the nth Fibonacci Number', fontsize=5)
    ax.set_zlabel('Imaginary part of the nth Fibonacci Number', fontsize=5)

    plt.show()
    return

if __name__=='__main__':
    main()