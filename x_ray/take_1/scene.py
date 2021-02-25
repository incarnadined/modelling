import numpy as np

from shapes import *
from maths import *
from particle import *

class BinSet:
    def __init__(self, line: Vector2D, n: int):
        self.line = line
        self.bincount = n

        self.bins = [0 for i in range(n)]

    def checkBin(self, other):
        '''
        Only called when a point is definately in one of the bins
        Returns the index of the bin the point/line fell into
        '''
        return np.floor(other.x - self.line.x[-1]) / (self.line.y[-1]/self.bincount)

    def inBinSet(self, other):
        '''
        Checks if a point/line is falls into a bin
        other should be Particle type
        '''
        if other.position.y[-1] <= self.line.y[-1] and other.position.y[-2] >= self.line.y[-2]:
            self.bins[checkBin(other)]+=1


class Scene:
    def __init__(self, gunloc):
        self.objects = []

        self.particles = []

        self.gunloc = Vector2D(gunloc[0], gunloc[1])

    def addObject(self, shape):
        self.objects.append(shape)

    def addBins(self, n: int, start: tuple, length: int):
        '''
        n is the number of bins
        top_left is the tuple for the top_left corner of the bin rectangle
        height is the height (y change) of the bin rectangle
        length is the length (x change) of the bin rectangle
        '''
        line = Vector2D(start[0], start[1])
        line.update(start[0]+length, start[1])
        self.bins = BinSet(line, 50)

    def fire(self, timestep: float, vel: int):
        '''
        Fire some particles from any of the guns individually or all of them.

        guns is a tuple with the indicies of the guns to be fired, empty means all of them
        '''
        self.particles.append(Particle(self.gunloc, vel))

        for particle in self.particles:
            particle.move(timestep)
            self.bins.inBinSet(particle)