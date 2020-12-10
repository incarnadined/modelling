import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d

'''
Calculating velocities:

g = -9.81

The components of the overall force can be calculated in terms of the z component (z refers to the dimension in which reaching z = 0 halts movement):
Using equations of motion in terms of z component at point of impact:
0 = ut + 0.5 * g * t^2
0 = t(u + 0.5gt)
t = 0 (at the start) or t = -u*2/g (at the end)

This time can be used to calculate the initial components for the desired position using u = s-0.5at^2/t:
(where u is the initial z component and a is the acceleration in the dimension of interest)
initial x component = (desired x distance - 0.5*a*((-u * 2)/g)^2)/ ((-u * 2)/g)
                    = (desired x distance * g^2 - 2au^2)/ (-u * 2 * g)

NOTE: the x component is just an example, the same equations applies for all other dimensions.

So from here, all we need to do is find a way to calculate the z component. We can do this by using
total velocity = sqrt(xcomponent^2 + ycomponent^2 + .... + zcomponent^2) and the equations we just calculated to get the total velocity in terms of the z component.
(where u is the initial z component, x is the desired x distance, y is the desired y distance, a is the acceleration in x, A is the acceleration in y, and ... implies
it for every instance of x and y the same repeats for all other dimensions apart from z)
total velocity = sqrt(((x * g^2 - 2au^2)/ (-u * 2 * g))^2 + ((x * g^2 - 2Au^2)/ (-u * 2 * g))^2 + ... + u^2)
               = The expansion of this is too large to put here, and will make little sense typed out rather than on paper

From this point we either have to put a limit on the z component or total velocity. We will work with achieving the lowest possible total velocity. We can simplify:
(where A = g^4(x^2 + y^2 + ...)
       B = -4(ag^2x + Ag^2y + ...)
       C = 4(a^2 + 4A^2 +... + 4g^2)
       D = 4g^2
       x = u^2)
total velocity^2 = (A + Bx + Cx^2)*Dx^-1
                 = A/Dx^-1 + B/D + C/Dx

The turning point of y = A/Dx^-1 + B/D + C/Dx occurs at x = sqrt(A/C) which can be calculated by differentiating and setting equal to 0, assuming x cannot be negative
(where x is u^2, or the z component^2, and y is the total velocity^2).

So for the least total velocity, the z component = sqrt(sqrt((g^4(x^2 + y^2 + ...))/(4*(a^2 + 4A^2 +... + 4g^2))))

Once we've calculated this value we can use it again in the equations calculated at the start to find the x and y components
If we want to find the total velocity we can use sqrt(xcomponent^2 + ycomponent^2 + zcomponent^2)
'''

def calculate_velocities():
    '''
    Calculates minimum upwards velocity to reach desired location dest
    Returns list of velocities in order x, y, a, ... z
    '''
    #Summary statistics
    value1 = 0
    value2 = 0

    for dim in dest:
        value1 += float(dim)**2
        
    for dim in acc:
        value2 += float(dim)**2

    acc.append(g)
    
    vz = [math.sqrt(math.sqrt((value1*(g**4))/(4*value2))), ]

    velocities = []

    for dim in dest:
        adim = float(acc[dest.index(dim)])
        dim = float(dim)
        
        v = [((dim*(g**2))-2*adim*(vz[0]**2))/(-2*vz[0]*g), ]
        velocities.append(v)

    velocities.append(vz)
    return velocities
    
def model(velocities):
    '''
    Simulates and plots the flight of a particle given components of initial velocity
    'velocities' parameter should be a list of velocities in order x, y, a, .... z
    Also requires global variables for acceleration and destination in each dimension given
    '''
    t = 0.001

    points = []
    
    for dim in velocities:
        points.append([0, ])
    
    ttaken = 0
    while True:
        #Basic movement with gravity

        for i in range(len(velocities)):
            #Basic movement
            points[i].append(points[i][-1] + velocities[i][-1] * t)
            #Adjust acceleration
            velocities[i].append(velocities[i][-1] + float(acc[i]) * t)

        ttaken += t

        #Displays results once particle hits the ground
        if points[-1][-1] < 0:
            print("Time = ", ttaken)
            for dim in points:
                print(dim[-1])
            break
    
def main():
    global acc, dest, g
    
    dest = "10, 10, 10, 10"
    acc = "10, 10, 10, 10"

    dest = dest.replace(" ","")
    dest = dest.split(",")

    acc = acc.replace(" ","")
    acc = acc.split(",")

    g = -9.81

    velocities = calculate_velocities()
    model(velocities)
    

if __name__ == "__main__":
    main()
