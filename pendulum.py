import math as maths
import matplotlib.pyplot as plt

def tdd1(mass1, mass2, theta1, theta2, thetaDot1, thetaDot2, length1, length2, g=9.81):
    a1 = -(g * (2 * mass1 + mass2) * maths.sin(theta1)) - (mass2 * g * maths.sin(theta1 - theta2 - theta2))
    b1 = - 2 * maths.sin(theta1 - theta2) * mass2 * ((thetaDot2 ** 2 * length2) + (thetaDot1 ** 2 * length1 * maths.cos(theta1 - theta2)))
    c1 = length1 * (2 * mass1 + mass2 - mass2 * maths.cos(theta1 + theta1 - theta2 - theta2))

    return (a1+b1)/c1
    
def tdd2(mass1, mass2, theta1, theta2, thetaDot1, thetaDot2, length1, length2, g=9.81):
    a2 = 2 * maths.sin(theta1 - theta2) * ((thetaDot1 ** 2 * length1 * (mass1 + mass2)) + (g * (mass1 + mass2) * maths.cos(theta1)))
    b2 = 2 * maths.sin(theta1 - theta2) * (thetaDot2 ** 2 * length2 * mass2 * maths.cos(theta1 - theta2))
    c2 = length2 * (mass1 + mass1 + mass2 - (mass2 * maths.cos(theta1 + theta1 - theta2 - theta2)))

    return (a2+b2)/c2

def pendulum(initialTheta, initialThetaDot, length, dt, nt, plot=False):
    g = 9.81
    theta1 = [initialTheta[0] * maths.pi/180]  # Convert degrees into radians
    theta2 = [initialTheta[1] * maths.pi/180]  # Convert degrees into radians
    thetaDot1 = initialThetaDot[0]
    thetaDot2 = initialThetaDot[1]
    mass1 = 20
    mass2 = 20
    length1 = length[0]
    length2 = length[1]
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for _ in range(nt - 1):  # Loop through nt
        thetaDoubleDot1 = tdd1(mass1, mass2, theta1[-1], theta2[-1], thetaDot1, thetaDot2, length1, length2)
        thetaDoubleDot2 = tdd2(mass1, mass2, theta1[-1], theta2[-1], thetaDot1, thetaDot2, length1, length2)

        theta1.append(theta1[-1] + dt * thetaDot1)
        theta2.append(theta2[-1] + dt * thetaDot2)

        thetaDot1 += dt * thetaDoubleDot1
        thetaDot2 += dt * thetaDoubleDot2

        x1.append(length1 * maths.cos(theta1[-1]))
        y1.append(length1 * maths.sin(theta1[-1]))
        x2.append(x1[-1] + (length2 * maths.cos(theta2[-1])))
        y2.append(y1[-1] + (length2 * maths.sin(theta2[-1])))
    
    if plot:
        for i in range(nt):
            if i % 5 == 0:   # Plot every 10th time step
                #plt.plot(y[0:i+1], 'k--')
                #plt.plot(i, y[i], 'ko')
                plt.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], 'r-')

                length = length1+length2
                plt.ylim([-length-1, length+1])
                plt.xlim([-length-1, length+1])

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.01)
                plt.clf()

    return theta1, x1, y1

def main():
    dt = 0.001
    nt = 10000
    initTheta = [-40, -50]     # In degrees
    initThetaDot = [10, 5]
    length = [20, 17]


    theta, x, y = pendulum(initTheta, initThetaDot, length, dt, nt, True)


    time = [dt * i for i in range(nt)]

    plt.plot(x, y, 'r')       # Plot theta vs time for all time steps
    plt.show()

if __name__ == '__main__':
    main()

# a1 = -(g * (2 * mass1 + mass2) * maths.sin(theta1)) - (mass2 * g * maths.sin(theta1 - theta2 - theta2))
# b1 = - 2 * maths.sin(theta1 - theta2) * mass2 * ((thetaDot2 ** 2 * length2) +
#                                                 (thetaDot1 ** 2 * length1 * maths.cos(theta1 - theta2)))
# c1 = length1 * (2 * mass1 + mass2 - mass2 * maths.cos(theta1 + theta1 - theta2 - theta2))
#
# a2 = 2 * maths.sin(theta1 - theta2) * ((thetaDot1 ** 2 * length1 * (mass1 + mass2)) + (g * (mass1 + mass2)
#                                                                                       * maths.cos(theta1)))
# b2 = 2 * maths.sin(theta1 - theta2) * (thetaDot2 ** 2 * length2 * mass2 * maths.cos(theta1 - theta2))
# c2 = length2 * (mass1 + mass1 + mass2 - (mass2 * maths.cos(theta1 + theta1 - theta2 - theta2)))
#
# thetaDoubleDot1 = (a1 + b1) / c1
# thetaDoubleDot2 = (a2 + b2) / c2