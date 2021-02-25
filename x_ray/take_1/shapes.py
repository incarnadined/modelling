from maths import Vector2D

class Rectangle:
    def __init__(self, top_left: tuple, top_right:tuple, bottom_left: tuple, bottom_right:tuple):
        self.top_left = Vector2D(top_left[0], top_left[1])
        self.top_right = Vector2D(top_right[0], top_right[1])
        self.bottom_left = Vector2D(bottom_left[0], bottom_left[1])
        self.bottom_right = Vector2D(bottom_right[0], bottom_right[1])

        self.width = abs(top_right[0]-top_left[1])

    def collides(self, other):
        if type(other) == Vector2D:
            if other.x[-1] <= max(self.top_left.x[-1], self.bottom_left.x[-1]) and other.x[-1] >= min(self.top_left.x[-1], self.bottom_left.x[-1]):
                if other.y[-1] <= max(self.top_left.y[-1], self.bottom_right.y[-1]) and other.x[-1] >= min(self.top_left.y[-1], self.bottom_right.y[-1]):
                    return True
        
        return False

class Circle:
    def __init__(self, centre: tuple, radius: int):
        self.centre = Vector2D(centre)
        self.radius = radius

    def collides(self, other):
        if type(other) == Vector2D:
            if (other.x[-1]-self.centre.x[-1])**2+(other.y[-1]-self.centre.y[-1])**2 <= self.radius**2:
                return True
        
        return False