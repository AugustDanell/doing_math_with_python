from collections import Counter

# Func from the book, able to calculate multiple modes:
def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common(1)
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

def residuals(x_data, mean):
    residuals = []
    for x in x_data:
        residuals.append(abs(x-mean))

    return residuals

def calculate_variance(numbers, mean):
    residual_list = residuals(numbers, mean)
    squared_res = [r**2 for r in residual_list]
    sum_squared_res = sum(squared_res)
    variance = sum_squared_res/len(numbers)

    return variance

if __name__ == '__main__':
    number_list = []
    file = open("mydata")
    s = 0

    for line in file:
        number = int(line)
        s += number
        number_list.append(number)

    file.close()

    mean = s / len(number_list)
    mode_list = calculate_mode(number_list)
    variance = calculate_variance(number_list, mean)
    std = variance**0.5
    print("From the file mydata we optained:", number_list)
    print("The mean is:", mean)
    print("Potential Mode/s are: {0}".format(mode_list))
    print("The variance is:", variance)
    print("The standard deviation (STD) is:", std)
