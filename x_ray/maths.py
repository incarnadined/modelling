import numpy as np

class Vec2:
    def __init__(self, x, y):
        self.x_hst = [x, ]
        self.y_hst = [y, ]

    @classmethod
    def from_magnitude(cls, magnitude, angle):
        '''
        Class method to create a vector from a magnitude and angle clockwise from i-hat
        '''

        return Vec2(magnitude*np.cos(angle), magnitude*np.sin(angle))

    @classmethod
    def from_vec2(cls, vec):
        '''
        Class method to create a vector with the same location as another vecotr
        '''

        return Vec2(vec.x, vec.y)

    @property
    def x(self):
        return self.x_hst[-1]

    @property
    def y(self):
        return self.y_hst[-1]

    def __add__(self, other):
        '''
        Overload the + operator to add two vectors
        '''

        return Vec2(self.x+other.x, self.y+other.y)

    def __iadd__(self, other):
        self.x_hst.append(self.x+other.x)
        self.y_hst.append(self.y+other.y)

        return self

    def __mul__(self, other):
        return Vec2(self.x*other, self.y*other)

    def __imul__(self, other):
        self.x_hst.append(self.x*other)
        self.y_hst.append(self.y*other)

        return self

    def __matmul__(self, theta):
        '''
        Overload the @ operator to rotate the vector
        '''
        rot_mat = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

        vec = rot_mat.dot(np.array([self.x, self.y]))

        return Vec2(vec[0], vec[1])

    def __imatmul__(self, theta):
        '''
        Overload the @= operator to rotate the vector
        '''
        rot_mat = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

        vec = rot_mat.dot(np.array([self.x, self.y]))
        self.x_hst.append(vec[0])
        self.y_hst.append(vec[1])

        return self

    def __pow__(self, other):
        return abs(self)**other

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __abs__(self):
        return np.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"<Vec2 object at ({self.x}, {self.y})>"
