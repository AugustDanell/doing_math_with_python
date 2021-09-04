''' Chapter 1
    #4 Fraction Calculator: Write a calculator that perform the basic mathematical operations on two fractions. It should
    ask the user for two fractions and the operation the user wants to carry out.
'''

from fractions import Fraction

# Using placeholders in format, like in C# syntax.
def add(a, b):
    print("Result of addition is: {0}".format(a+b))

def sub(a, b):
    print("Result of subtraction is: {0}".format(a-b))

def mult(a, b):
    print("Result of multiplication is: {0}".format(a*b))

def div(a, b):
    print("Result of division is: {0}".format(a/b))

if __name__ == '__main__':
    a = Fraction(input("Type in your first fraction please."))
    b = Fraction(input("Type in your second fraction please."))
    op = input("Type in any of the operations: Add, Subtract, Multiply, Divide")
    op = op.lower()

    if(op == "add"):
        add(a,b)
    elif(op == "subtract"):
        sub(a,b)
    elif(op == "multiply"):
        mult(a,b)
    elif(op == "divide"):
        div(a,b)
    else:
        print("You entered in a strange operation, no calculation was made, restart the program if you want to try again.")
