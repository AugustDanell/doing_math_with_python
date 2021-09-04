''' Chapter 2
    #1: How does the temperature vary during the day?
    If you enter a search term like "New York Weather" in Google's search engine you'll see among other things, a graph
    showing the temperature at different times of th present day. Your task is here to re-create such a graph. Use a city
    of your choice and finde the temperature at different points of the day. Use the data to create two lists in your program
    and to create a raph with the time of the day on the x-axis and the corrosponding temperature on the y-axis. The graph
    should tell you how the temperature varies with time of the day, try different cities and see how the lines compare on
    the graph.
'''
from matplotlib import pyplot as plt

if __name__ == '__main__':
    time_data  = ["17.00", "20.00", "23.00", "02.00", "05.00", "08.00", "11.00", "14.00"] # x-axis
    tokyo_data = [22, 21, 21, 19, 19, 19, 21, 23]
    stockholm_data = [9, 13, 14, 13, 8, 6, 4, 4]
    paris_data = [20, 24, 27, 25, 23, 21, 19, 18]

    plt.plot(time_data, tokyo_data, marker = 'o')
    plt.plot(time_data, stockholm_data, marker = 'o')
    plt.plot(time_data, paris_data, marker = 'o')
    plt.xlabel("Time of the day")
    plt.ylabel("Temperature in Celsius")
    plt.legend(['Tokyo','Stockholm','Paris'])
    plt.show()
