# Derivatives and their role in Optimization

# What are derivatives?
#   - Measures the rate at which a function changes with respect to its input
#   - For a function f(x), the derivative f'(x) indicates the slope of the tangent line at a point x

# Role in optimization
#   - Used to minimize or maximize a function

import sympy as sp

""" x = sp.Symbol('x')
f = x**2
derivative = sp.diff(f, x)
print("Derivative: ", derivative) """

# Partial derivatives
#   - Measures how a function changes with repects to one variable while keeping other variables constant

# Gradient
#   - Vector of all partial derivatives, indicating the direction of the steepest ascent

x, y = sp.symbols('x, y')
f = x**2 + y**2
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Partial Derivatives: ", grad_x, grad_y)

# Gradient Descent
#   - Iterative optimization algorithm used to minimize a function
#   - Updates parameters in the directino of negative gradient to find the minimum
#   - Used in learning models
