from matplotlib import pyplot as plt

# Modified function from the books:
def find_corr_x_y(x,y):
    if(len(x) == len(y)):
        n = len(x)
        prods = []
        for xi,yi in zip(x,y):
            prods.append(xi*yi)

        # Defining statistical data:
        prod_sum_x_y = sum(prods)
        sum_x = sum(x)
        sum_y = sum(y)
        squared_sum_x = sum_x**2
        squared_sum_y = sum_y**2

        x_square = []
        y_square = []

        # We use that x and y have to have the same length:
        for i in range(len(x)):
            x_square.append(x[i]**2)
            y_square.append(y[i]**2)

        x_square_sum = sum(x_square)
        y_square_sum = sum(y_square)

        numerator = n*prod_sum_x_y - sum_x*sum_y
        denominator_term1 = n*x_square_sum - squared_sum_x
        denominator_term2 = n*y_square_sum - squared_sum_y
        denominator = (denominator_term1*denominator_term2)**0.5
        correlation = numerator / denominator

        return correlation

    else:
        raise Exception("Lists are of different lengths")

if __name__ == '__main__':
    x_data = [1,2,3,4,5]
    y_data = [3,6,7,5,8]
    correlation = find_corr_x_y(x_data, y_data)

    plt.scatter(x_data, y_data, marker = 'o')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend(['X data / Y data has a correlation coefficient of: {0}'.format(correlation)])
    plt.show()
