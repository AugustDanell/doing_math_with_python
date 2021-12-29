'''
    Slightly modified example code from page 165 with my own comments.
    This example code is an implementation of a specific transformation as suggested by British Mathematician
    Michael Barnsley. The transformation is one that draws ferns using 4 transformations with non-uniform
    distribution of probabilities: [0.85, 0.7, 0.7, 0.01].

    1. As with the zig_zag example, define transformations, here we have 4 of them: transformation_x.
       where x is a number from 1 to 4.
    2. Defining an index distributive function that takes in a list L of probabilities and returns the index
    of each element p in L, with the probability p.
    3. Apply transform on the index given in step 2.
    4. Draw n points in accordance with the transformations.

'''
import random

import matplotlib.pyplot as plt


def extract_x_and_y(p):
    return p[0],p[1]

# 1: Transformations, Transformation_x, for x = 1 to x = 4:
def transformation_1(p):
    x, y = extract_x_and_y(p)
    x1 = 0.85*x + 0.04*y
    y1 = -0.04*x + 0.85*y + 1.6

    return x1, y1


def transformation_2(p):
    x, y = extract_x_and_y(p)
    x2 = 0.2 * x - 0.26 * y
    y2 = 0.23 * x + 0.22 * y + 1.6

    return x2, y2


def transformation_3(p):
    x, y = extract_x_and_y(p)
    x3 = -0.15 * x + 0.28 * y
    y3 = 0.26 * x + 0.24 * y + 0.44

    return x3, y3


def transformation_4(p):
    x, y = extract_x_and_y(p)
    x4 = 0
    y4 = 0.16*y

    return x4, y4

# 2: Index distributive function: L -> P
def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

# 3: Applying transform on index where P is:
def transform(p):
    list_of_transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
    probability = [0.85, 0.07, 0.07, 0.01]
    tindex = get_index(probability)
    t = list_of_transformations[tindex]
    x, y = t(p)
    return x, y

def draw_fern(n):

    # Starting position in origo:
    x_values = [0]
    y_values = [0]

    x1, y1 = 0,0
    for i in range(n):
        x1, y1 = transform((x1,y1))
        x_values.append(x1)
        y_values.append(y1)

    return x_values, y_values

if __name__ == '__main__':
    n = int(input('How many points of Fern do you want to draw?'))
    x,y = draw_fern(n)

    plt.plot(x,y,'o')
    plt.title('Fern with {0} points'.format(n))
    plt.show()
