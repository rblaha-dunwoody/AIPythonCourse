# Integrals
#   - Compute the area under a curve, representing accumulation

# Applications in ML
#   - Probability distributions
#   - Cost functions

import sympy as sp

x = sp.Symbol('x')
f = x**2
definite_integral = sp.integrate(f, (x, 0, 2))
indefinite_integral = sp.integrate(f, x)
print("Definite integral: ", definite_integral)
print("Indefinite integral: ", indefinite_integral)

# Optimization Concepts
#   - Local vs Global minima
#   - Convex Funcions

# Stochastic Gradient Descent
#   - Optimization algorithm that uses random subsets (mini-batches) of data to computer gradients and update paramaters