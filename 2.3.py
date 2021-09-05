''' Chapter 2
    #3: Enhanced Projectile Trajectory Comparison Program
    Your challenge here is to enhance the trajectory comparison program in a few ways. First, your progam should print
    the time of flight maximum horizontal distance, and maximum vertical distance traveled for each of the velocity and
    angle of projection combinations. The other enhancement is to make the program work with any number of initial
    velocity and angle of projection values, supplied by the user.
'''
import math

from matplotlib import pyplot as plt

# Helper functions from the book, slightly modified:
def func_range(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers

# Draw trajectory from the book:
def add_trajectory(u, theta):
    theta = math.radians(theta)
    gravity = 9.82
    t_flight = 2*u*math.sin(theta)/gravity      # Calculating landing spot.
    intervals = func_range(0, t_flight, 0.001)

    x_values = []
    y_values = []

    for t in intervals:
        x_values.append(u*math.cos(theta)*t)
        y_values.append(u*math.sin(theta)*t - 0.5*gravity*t**2)

    plt.plot(x_values, y_values)

if __name__ == '__main__':
    trajectories = 0
    plt.xlabel('Distance (meters)')
    plt.ylabel('Height (meters)')
    plt.title('Projectile motions of multiple balls')

    while(True):
        try:
            trajectories = int(input("How many trajectories? (Enter in a real value greater than zero): "))
            if(trajectories < 0):
                raise Exception
        except:
            continue
        break


    for i in range(trajectories):
        try:
            init_vel = float(input("Enter in the initial velocity for trajectory {0}".format(i+1)))
            start_angle = float(input("Enter in the angle for trajectory {0}, in degrees".format(i + 1)))
        except:
            print("You entered in a bad input!")
        else:
            add_trajectory(init_vel, start_angle)

    plt.show()
