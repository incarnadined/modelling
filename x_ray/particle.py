from maths import *
import numpy as np

class Particle:
    def __init__(self, loc: Vec2, vel: Vec2, timestep: int):
        self.position = loc
        self.velocity = vel

        self.timestep = timestep

    def move(self, scatteringIndex):
        self.position += Vec2(self.velocity.x*self.timestep, self.velocity.y*self.timestep)

        self.velocity @= np.random.normal(0, np.pi * scatteringIndex)
        self.velocity *= np.random.uniform(1-scatteringIndex, 1)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def energy(self):
        # calculate the energy where mass is 0.01
        return 1/2*0.01*self.velocity**2

    def __repr__(self):
        return f"<Particle at ({self.x}, {self.y}) with velocity {abs(self.velocity)}>"