from maths import *

class Rectangle:
    def __init__(self, top_left: Vec2, width: int, height: int):
        self.tl = top_left
        self.tr = Vec2(top_left.x+width, top_left.y)
        self.bl = Vec2(top_left.x, top_left.y-height)
        self.br = Vec2(top_left.x+width, top_left.y-height)

        self.scatteringIndex = 0.1

    def collides(self, other):
        if other.x < self.tr.x and other.x > self.tl.x:
            if other.y < self.tr.y and other.y > self.br.y:
                return True

        return False

class Circle:
    def __init__(self, centre: Vec2, radius: int):
        self.centre = centre
        self.radius = radius

        self.scatteringIndex = 0.001

    def collides(self, other):
        if (other.x-self.centre.x)**2+(other.y-self.centre.y)**2 <= self.radius**2:
            return True

        return False