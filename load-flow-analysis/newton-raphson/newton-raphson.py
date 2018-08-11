import numpy as np
import math
from numpy.linalg import inv
# from sympy import symbols, diff


# Partial differentiation:

# from sympy import symbols, diff
# x, y, z = symbols('x y z', real=True)
# f = 4*x*y + x*sin(z) + x**3 + z**8*y
# diff(f, x)
# 4*y + sin(z) + 3*x**2

def create_jacobian_matrix():
    jacobian_matrix = [[48.3, 12.94], [12.94, 48.3]]
    return jacobian_matrix


def calc_inverse_jacobian_matrix(jacobian_matrix):
    jacobian_matrix = np.matrix(jacobian_matrix)
    print(jacobian_matrix.I)


calc_inverse_jacobian_matrix(create_jacobian_matrix())
