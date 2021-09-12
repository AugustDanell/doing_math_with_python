from sympy import Symbol, sympify
from sympy import factor

expr = "UNSPECIFIED"
while(1):
    try:
        expr = input('Enter in an expression that you want to factorize.')
        expr = sympify(expr)
    except:
        print("You entered in an illegal value, please enter in an expression to factorize again.")
    else:
        break

print("Your expression can be factorized into: {0}".format(factor(expr)))
