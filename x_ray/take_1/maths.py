import numpy as np

class Vector2D:
    def __init__(self, x, y):
        self.x = [x, ]
        self.y = [y, ]

        self.angle = self.calculate_angle()

    def magnitude(self):
        return np.sqrt(self.x[-1]**2+self.y[-1]**2)
    
    def calculate_angle(self):
        try:
            return np.arctan(self.y[-1]/self.x[-1])
        except ZeroDivisionError:
            return np.pi/2

    def update(self, x, y):
        self.x.append(x)
        self.y.append(y)

        self.angle = self.calculate_angle()

    def update_angle(self, angle):
        magnitude = self.magnitude()

        self.x.append(magnitude*np.cos(self.angle+angle))
        self.y.append(self.magnitude()*np.sin(self.angle.angle))

    def __add__(self, other):
        if type(other) == Vector2D:
            return Vector2D(self.x[-1]+other.x[-1], self.y[-1]+other.y[-1])
        if type(other) == int:
            # the use of both magnitude and self.magnitude() is intentional to prevent the magnitude from updating before the end of this line
            magnitude = self.magnitude()
            return Vector2D((other+magnitude)*np.cos(self.angle), (other+self.magnitude())*np.sin(self.angle))

    def __imul__(self, other):
        # other should be scalar
        self.x.append(self.x[-1]*other)
        self.y.append(self.y[-1]*other)
        return self