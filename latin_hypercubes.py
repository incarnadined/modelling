import numpy as np

def latin_hypercubes(low, high, size):
    '''
    https://en.wikipedia.org/wiki/Latin_hypercube_sampling
    '''
    x = np.linspace(low, high, size)

    np.random.shuffle(x)

    return x