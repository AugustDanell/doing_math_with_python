from sympy import solve, Symbol, pprint

''' Modified example code from chapter 4, page 112 in the book.
    Inputs n expressions of x and y, solving those expressions for y and appending them
    to a table that is outputted at the end:
    
    Step 1: Initiate an empty list of solutions.
    Step 2: Let the user input a number n deciding on how many expressions to be solved.
    Step 3: Let the user define an expression and solve it for y, saving the solution in a list and the expressions.
    Step 4: Output the expressions alongside the solutions.
'''

y = Symbol('y')
solutions = []
expressions = []
n = int(input('How many expressions do you want to solve for?'))


for i in range(n):
    expr = input('Enter in expression %d:' %(i+1))
    expressions.append(expr)
    solutions.append(solve(expr, y))

print()
print('Expressions')
for i in range(n):
    print("Expression %d: %s \t Solution: y = %s" %((i+1), expressions[i], solutions[i][0]))
