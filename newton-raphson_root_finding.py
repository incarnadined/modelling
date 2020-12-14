import numpy as np
import matplotlib.pyplot as plt
import random

'''
This program uses the Newton-Raphson method for finding the roots of a real-valued function through gradient descent.

It works to find the principal root to any (real-valued) cubic or quadratic with the following formula.

x = x[-1] - (f(x[-1])/finv(x[-1]))

Because the method is iterative, the final graph shows the number of iterations on the x-axis against the proposed value on the y-axis.
The smaller the gradient of the line, the more accurate the solution. If the line has a gradient of 0 at the end, 
the answer should be accurate to as many decimal places as the computer can handle (shown in the title).
'''

class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.type = 'square'

    def f(self, x: int):
        '''
        Function that performs the quadratic defined in this class' initilisation on x
        '''
        return self.a*x**2 + self.b*x + self.c
        
    def finv(self, x: int):
        '''
        Function that performs the inverse of the quadratic defined in this class' initilisation on x
        '''
        return 2*self.a*x + self.b

class cubic:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.type = 'cube'

    def f(self, x: int):
        '''
        Function that performs the quadratic defined in this class' initilisation on x
        '''
        return self.a*x**3 + self.b*x**2 + self.c*x + self.d
        
    def finv(self, x: int):
        '''
        Function that performs the inverse of the quadratic defined in this class' initilisation on x
        '''
        return 3*self.a*x**2 + 2*self.b*x + self.c

def main():
    # c is the value that we want to find the principal root of
    c = 7643
    # the seed is the initial value for iteration. the closer to the actual answer the faster it works
    seed = 24

    x = [0]
    y = [seed]

    f = cubic(1, 0, 0, -c)

    for iteration in range(1, 100):
        x.append(iteration)
        y.append(y[-1] - (f.f(y[-1])/f.finv(y[-1])))

    plt.figure()
    plt.plot(x, y, '-r')

    plt.xlabel('Number of iterations')
    plt.ylabel('Result')

    plt.title(f'The principal {f.type} root of {c} is {y[-1]}')

    plt.show()
    return

if __name__=='__main__':
    main()