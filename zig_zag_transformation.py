''' Slightly modified example code from page 160 with my own comments.
    1. Transformation is made by two choices, uniformly at random (50% chance for either choice).
    Transformation one is an incrementation for the next point, and Transformation two is a decrement.
    Either choice can be taken, creating a zig zag pattern.
    2.
'''

import matplotlib.pyplot as plt
import random

def transformation_increment(p):
    x = p[0]
    y = p[1]
    return (x+1), (y+1)

def transformation_decrement(p):
    x = p[0]
    y = p[1]
    return (x+1), (y-1)

# 1: Transformation
def transform(p):
    transformations = [transformation_increment, transformation_decrement]
    rand_trans = random.choice(transformations)
    x, y = rand_trans(p)
    return x, y

# 2: Building a trajectory of n transformations:
def build_trajectory(p,n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])

    return x, y

if __name__ == '__main__':
    p = (1,1)
    n = int(input('How many zig zag points do you want to draw up?'))
    x_vector, y_value = build_trajectory(p, n)

    plt.plot(x_vector,y_value)
    plt.xlabel('X-value')
    plt.ylabel('Y-value')
    plt.show()
