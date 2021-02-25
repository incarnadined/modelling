import numpy as np
import matplotlib.pyplot as plt

from room import Room
from maths import *
from shapes import *

def main():
    # Note: all measurements are in cm
    
    particle_count = 10000
    total_time = 10
    current_time = 0
    timestep = 0.1

    spawn = Vec2(20, 0)
    vel = Vec2.from_magnitude(10, -np.pi/2)
    bin_count = 100
    bin_length = 40
    bin_y = -60
    room = Room(spawn, vel, timestep, bin_count, bin_length, bin_y)

    room+=Rectangle(Vec2(0, 50), 40, 10)
    room+=Circle(Vec2(20, 55), 2)

    # fire all of the particles
    for i in range(particle_count):
        room.fire()

    while current_time < total_time:
        room.simulate()
        current_time+=timestep

    y = []
    for energy in room.bin_energies:
        # normalise the energy for each bin and exp it
        energy = energy/room.particle_dests[room.bin_energies.index(energy)] if room.particle_dests[room.bin_energies.index(energy)] != 0 else 0
        y.append(np.exp(energy))

    plt.figure()
    plt.plot([i*(bin_length/bin_count) for i in range(bin_count)], y, 'r-')

    plt.show()


if __name__=='__main__':
    main()