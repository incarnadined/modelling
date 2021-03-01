import numpy as np
from itertools import combinations
import pygame

def calc_force(body1, body2, G=100, softening=1.25):
    return (G*body1.mass*body2.mass) / ((abs(body1.location-body2.location))**2 + softening)

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clear(self):
        self.x = 0
        self.y = 0

    def __sub__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x - other.x, self.y - other.y)
        return Vec2(self.x - other, self.y - other)

    def __mul__(self, other):
        return Vec2(self.x*other, self.y*other)

    def __truediv__(self, other):
        return Vec2(self.x/other, self.y/other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

        return self

    def __abs__(self):
        return np.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"<Vec2 object at ({self.x}, {self.y})>"

class Body:
    def __init__(self, mass=None, velocity=None, location=None):
        self.mass = mass if mass is not None else np.random.rand()
        self.location = location if location is not None else Vec2(np.random.uniform(0, 1920), np.random.uniform(0, 1080))
        self.velocity = Vec2(0, 0) if velocity is None else velocity

        self.acceleration = Vec2(0, 0)
        self.forces = Vec2(0, 0)

        self.colour = np.random.rand(3) * 255

    def update(self, dt):
        self.location += self.velocity * dt
        self.velocity += self.acceleration * dt

        self.acceleration += self.forces / self.mass
        self.forces.clear()

        if self.location.x > 1920:
            self.location.x = 0
        if self.location.x < 0:
            self.location.x = 1920
        if self.location.y > 1080:
            self.location.y = 0
        if self.location.y < 0:
            self.location.y = 1080

    def add_interaction(self, other):
        # calculate the force
        force = calc_force(self, other)

        self.forces += self.direction(other) * force
        other.forces += other.direction(self) * force

    def direction(self, other):
        if abs(other.location - self.location) == 0:
            return Vec2(0, 0)
        return (other.location - self.location) / abs(other.location - self.location)

    def __repr__(self):
        return f"<nody with mass: {self.mass}, velocity: {self.velocity} at location {self.location}>"

def main():
    N = 10

    # pygame stuff
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    oldtime = pygame.time.get_ticks()
    running = True
    active = False

    ra = 100
    bodies = [Body(1000, Vec2(np.random.uniform(-ra, ra), np.random.uniform(-ra, ra))) for i in range(N)]
    #bodies = [Body(100000, Vec2(500, 100), Vec2(480, 590)), Body(100000, Vec2(-500, -100), Vec2(1440, 590))]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    active = True if active == False else False
                    print(f'Active: {active}')
        screen.fill((0, 0, 0))

        # draw the bodies
        for body in bodies:
            pygame.draw.circle(screen, body.colour, (body.location.x, body.location.y), 5)

        if active:
            # calculate new forces for all different body interactions
            for comb in combinations(bodies, 2):
                comb[0].add_interaction(comb[1])
                #active = False

            # update positions/velocities/acclerations
            for body in bodies:
                body.update((pygame.time.get_ticks() - oldtime)/1000)

        oldtime = pygame.time.get_ticks()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()