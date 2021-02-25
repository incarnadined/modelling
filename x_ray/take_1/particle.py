from maths import *

class Particle:
    def __init__(self, start: Vector2D, vel_mag: int):
        self.position = start

        angle = np.random.uniform(0, np.pi/36)
        self.velocity = Vector2D(np.sin(angle)*vel_mag, np.cos(angle)*vel_mag)

    def move(self, timestep):
        if self.velocity.magnitude() <= 0.01:
            pass

        else:
            self.position.update(self.position.x[-1] + self.velocity.x[-1] * timestep, self.position.y[-1] + self.velocity.y[-1] * timestep)
            
            # adjust velocity
            self.velocity*=0.9
            #self.velocity.update_angle(self.scattering_angle)