'''
    Assignment 6.2 - Drawing Sierpinski's triangle
    1. We start with defining different transformations that will generate the triangles (4 transformations).
'''
import random
import matplotlib.pyplot as plt

def extract_x_and_y(p):
    return p[0],p[1]

# 1: Transformations, Transformation_x, for x = 1 to x = 4:
def transformation_1(p):
    x, y = extract_x_and_y(p)
    x1 = 0.5*x
    y1 = 0.5*y

    return x1, y1

def transformation_2(p):
    x, y = extract_x_and_y(p)
    x2 = 0.5*x + 0.5
    y2 = 0.5*y + 0.5

    return x2, y2

def transformation_3(p):
    x, y = extract_x_and_y(p)
    x3 = 0.5*x
    y3 = 0.5*y + 1.0

    return x3, y3

def transform(n, p):
    transforms = [transformation_1, transformation_2, transformation_3]
    x1, y1 = p[0],p[1]
    x = [0]
    y = [0]

    for i in range(n):
        t = random.choice(transforms)
        x1, y1 = t((x1,y1))
        x.append(x1)
        y.append(y1)

    return x, y

if __name__ == '__main__':
    n = int(input('How many points do you want of Sierpienskis triangle?'))
    p = (0,0)
    x_vals, y_vals = transform(n, p)
    print(x_vals)
    print(y_vals)

    plt.plot(x_vals, y_vals, 'o')
    plt.title('Sierpienskis triangle with {0} data points.'.format(n))
    plt.show()
