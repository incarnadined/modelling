import maths
from scene import *
from shapes import *

def main():
    scene = Scene((0, 20))

    scene.addObject(Rectangle((0, -50), (40, -50), (0, -60), (40, -60)))

    scene.addBins(50, (0, 60), 40)

    time = 0
    timestep = 0.1
    while time < 120:
        scene.fire(timestep, 0.2)
        time+=timestep

    print(scene.bins.bins)

if __name__ == '__main__':
    main()