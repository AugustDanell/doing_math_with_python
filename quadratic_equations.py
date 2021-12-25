from sympy import solve, Symbol,pprint

''' Solving Quadratic Equations
    1. Using sympy we can import Symbol to make x into a variable.
    2. We can create various expressions of x.
    3. We use pprint (Pretty Print) to output the results.
'''

x = Symbol('x')

# Expression with real roots:
expr = x**2 - 4*x - 15
pprint(solve(expr, dict=True))

# Expression with imaginary roots:
expr = x**2 - 4*x + 15
pprint(solve(expr, dict=True))

