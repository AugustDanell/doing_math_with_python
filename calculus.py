from sympy import Symbol, Limit, S, Derivative, solve, Integral

''' 
    Modified examples from chapter 7, pertaining to calculus in Python:
    
    

'''

print('1. Defining a function of x, f(x) = 1/x^2:')
x = Symbol('x')
inf_lim = Limit(1/x**2, x, S.Infinity)
zero_lim = Limit(1/x**2, x, S.Zero)
print('2. Limit of f(x) as x approaches infinity: {0}'.format(inf_lim.doit()))
print('3. Limit of f(x) as x approaches zero: {0}'.format(zero_lim.doit()))

print()
print('4. Defining a function of x, f(x) = x^2 + 4x - 15:')
f = x**2 + 4*x - 15
df = Derivative(f,x)
print('5. Deriving f(x) into df: {0}'.format(df.doit()))
print()

print('We can also use the Derivative function to find partial derivatives, just by expressing the variable of which to derive with respect to.')
print('6. Defining multivariate function g = x**2 + 4*y - 15')
y = Symbol('y')
g = x**2 + 4*y - 15
dg = Derivative(g, y)
print('7. Deriving the function with respect to y (partial derivative): {0}'.format(dg.doit()))
print()
print('We can also use sympy to find maxima and minima by setting a derivative of the function to zero and solve.')
print("8. Define function M(x) = x^5 - 30x^3 + 50x.")
m = x**5 - 30*x**3 + 50*x
dm = Derivative(m, x).doit()
print("9. Find the derivative of M, M', using sympy: {0}".format(dm))
critical_points = solve(dm)
print("10. Find critical points by solving for when M' = 0: {0}".format(critical_points))
print("11. Testing the critical points by inserting them into m(x): \n")

i = 0
for c in critical_points:
    i += 1
    print("Critical Point {0} yields a function value of m(x) = {1}".format(i, m.subs({x:c}).evalf() ))

print('\nIntegrals:\nWe may also use sympy to calculate integrals of functions.')
print('12. Define function f(x) = x^2.')
f = x**2
print('13. Integrate from zero to three, (we know this should yield 3^3/3 = 3^2 = 9.). Integral(f,(x,0,3)).doit(): {0}'.format(Integral(f,(x,0,3)).doit()))
