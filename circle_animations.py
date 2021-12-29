'''
    Slightly modified example code from pages 151 and 153
'''

import matplotlib.pyplot as plt
from matplotlib import animation

def create_circle():
    circle = plt.Circle((0,0), radius = 0.05)
    return circle

def update_radius(i, circle, growth_factor = 0.1):
    circle.radius = i*growth_factor
    return circle

def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim = (-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_radius, fargs = (circle,), frames = 30, interval = 200)
    plt.title('Simple Circle Animation')
    plt.show()

def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = create_circle()
    #show_shape(c)
    create_animation()
