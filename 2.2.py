''' Chapter 2
    In chapter 1, you learned how to find the roots of a quadratic equation, such as x^2 + 2x + 1 = 0. We can turn this
    equation into a function by writing it as y = x^2 + 2x + 1. For any value of x, the quadratic function produces some
    value for y. For example, when  = 1, y = 4.

'''
from matplotlib import pyplot as plt

if __name__ == '__main__':
    x_values = [x for x in range(-1,10)]
    y = lambda x: (x**2 + 2*x + 1)
    y_values = [y(x) for x in x_values]

    plt.plot(x_values, y_values, 'o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['y = x^2 + 2x +1'])
    plt.show()
