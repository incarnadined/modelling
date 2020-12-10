import numpy as np
from scipy.constants import g
import matplotlib.pyplot as plt


def main():
    dt = 0.1
    v = 100
    a = -g
    theta = np.pi/3
    air_resistance = 0.001

    vx = v * np.cos(theta)
    vz = v * np.sin(theta)
    sx = [0]
    sz = [0]
    while sz[-1] >= 0:
        sx.append(sx[-1] + vx * dt)
        sz.append(sz[-1] + vz * dt)
        vx -= vx * air_resistance
        vz += a*dt - vz*air_resistance

    plt.figure()
    plt.plot(sx, sz, '-r')

    plt.xlabel('Horizontal Displacement (m)')
    plt.ylabel('Vertical Displacement (m)')

    plt.show()
    return

if __name__=='__main__':
    main()