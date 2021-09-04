''' Chapter 1
    #1: Even-Odd Vending Machine
    Try writing an "Even-Odd Vending Machine" which will take a number as input and do two things:

    1. Print whether the number is even or odd.
    2. Display the number followed by the next 9 even or odd numbers.

    Example: If the number is 2 the output should be: even: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
             If the number is 1: odd: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
'''

if __name__ == '__main__':
    n = int(input())
    is_even = (n%2 == 0)
    s = ""

    if(is_even):
        s += "even:"
    else:
        s += "odd:"

    for i in range(0,9):
        s += " " + str(i*2 + n)

    print(s.strip())
