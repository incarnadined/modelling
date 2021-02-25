import numpy as np
from copy import deepcopy

from particle import Particle
from maths import *

class Room:
    def __init__(self, spawn, vel, timestep, bins, binx, biny):
        '''
        Note: objects with high precedence should be added after objects with low precedence
        '''
        self.spawn = spawn
        self.timestep = timestep
        self.vel = vel

        self.bin_count = bins
        self.bin_length = binx
        self.bin_y = biny

        self.objects = []
        self.particles = []
        self.particle_dests = [0 for i in range(self.bin_count)]
        self.bin_energies = [0 for i in range(self.bin_count)]

    def check_bin(self, particle: Particle):
        if particle.y < self.bin_y:
            if particle.position.x_hst[-2]-particle.x != 0.0:
                m = (particle.position.y_hst[-2]-particle.y)/(particle.position.x_hst[-2]-particle.x)
                eq = lambda y: (y-particle.y+particle.x*m)/m

                if (eq(self.bin_y) < self.bin_length and eq(self.bin_y) > 0):
                    current_bin = np.floor(eq(self.bin_y)/(self.bin_length/self.bin_count))
                    self.particle_dests[int(current_bin)]+=1
                    self.bin_energies[int(current_bin)]+=particle.energy

                # set the particle's velocity to 0, it shouldn't be measured again
                particle.velocity.x_hst.append(0)
                particle.velocity.y_hst.append(0)

    def scattering_medium(self, particle: Particle):
        '''
        Returns the scattering index of the medium the given particle is currently in
        '''
        for item in self.objects[::-1]:
            if item.collides(particle):
                print(item.scatteringIndex)
                return item.scatteringIndex
        
        # if the particle isn't in an object return scattering index for air
        return 0.01

    def fire(self):
        self.particles.append(Particle(Vec2.from_vec2(self.spawn), Vec2.from_vec2(self.vel), self.timestep))
        self.particles[-1].velocity@=np.random.uniform(-np.pi/18, np.pi/18)

    def simulate(self):
        for particle in self.particles:

            # only move the particle if its velocity is above a certain threshold
            if abs(particle.energy) > 0.01:
                particle.move(self.scattering_medium(particle))

                # only check the particle if it just moved, otherwise it should already be accounted for
                self.check_bin(particle)

    def __iadd__(self, other):
        self.objects.append(other)

        return self