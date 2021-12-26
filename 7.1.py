from sympy import Symbol, Limit, S, Derivative, solve, Integral
''' Assignment 7.1
    We start with reading in three values:
    1. A variable.
    2. A function (using that variable).
    3. A point on that function in which we want to check for continuity.
    
    How do we check for continuity?
    4. We simply check if the limity as we approach from the left matches the limit from the right.
'''


var = input('Enter in a variable:')
x = Symbol(var)

f = input('Enter a function in one variable:')
p = input('Enter a point in which to check the function:')

l1 = Limit(f,x,p, dir = '-')
l2 = Limit(f,x,p, dir = '+')

if(l1.doit() == l2.doit()):
    print('The function {0} is continuous at {1}.'.format(f,p))
else:
    print('The function {0} is NOT continuous at {1}.'.format(f, p))
