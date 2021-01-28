import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

class Vector2D:
    def __init__(self, x, y):
        self.x = [x, ]
        self.y = [y, ]
        self.angle = np.arctan(y/x)

    def magnitude(self):
        return np.sqrt(self.x[-1]**2+self.y[-1]**2)

    def update(self, x, y):
        self.x.append(x)
        self.y.append(y)
        self.angle = np.arctan(y/x)

    def update_x(self, x):
        self.x.append(x)
        self.angle = np.arctan(self.y[-1]/x)

    def update_y(self, y):
        self.y.append(y)
        self.angle = np.arctan(y/self.x[-1])

    def update_angle(self, angle):
        '''
        Updates the angle of the vector without changing the magnitude
        '''
        self.angle = angle
        old_mag = self.magnitude()
        self.x.append(np.cos(self.angle)*old_mag)
        self.y.append(np.sin(self.angle)*old_mag)

    def __repr__(self):
        return f"({self.x[-1]}, {self.y[-1]})"

class Particle:
    def __init__(self, size=100, velocity=100, deceleration=0.95):
        '''
        size is half the length of the square they can spawn in, centred on the origin
        velocity is the range of velocity (-velocity to velocity)
        deceleration is the amount of deceleration per timestep, should be < 1
        '''
        self.position = Vector2D(np.random.uniform(-size, size), np.random.uniform(-size, size))

        self.velocity = Vector2D(np.random.uniform(-size, size), np.random.uniform(-size, size))
        self.deceleration = deceleration

        self.mu, self.sigma = 0, np.pi/16

    def update(self, timestep):
        if self.velocity.magnitude() <= 0.01:
            pass

        else:
            self.position.update(self.position.x[-1] + self.velocity.x[-1] * timestep, self.position.y[-1] + self.velocity.y[-1] * timestep)
            
            # adjust velocity
            self.scattering_angle = np.random.normal(self.mu, self.sigma)
            self.velocity.update_angle(self.velocity.angle+self.scattering_angle)
            self.velocity.update(self.velocity.x[-1] * self.deceleration, self.velocity.y[-1] * self.deceleration)


def main():
    n = 300 # number of particles
    timestep = 0.01
    time = 0

    particles = [Particle(500, 500, np.random.uniform(0.8, 0.99)) for x in range(0, n)]

    # number of seconds to simulate
    while time < 120:
        for particle in particles:
            particle.update(timestep)

        time+=timestep

    plt.figure()

    colour=iter(cm.rainbow(np.linspace(0, 1, n)))
    for particle in particles:
        c = next(colour)
        plt.plot(particle.position.x, particle.position.y, c=c)

    plt.show()

if __name__ == '__main__':
    main()