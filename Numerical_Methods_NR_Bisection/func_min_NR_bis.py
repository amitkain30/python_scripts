"""
Script to find minima of functions (quadratic) using 
two numerical methods Newton Raphson & Bisection
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_parabola(c_1:int, c_2:int, c_3:int):
    """
    Function to plot equation with the provided coefficients.
    Assuming equation of the form (c_1)x^2 + (c_2)x + c_3

    Args:
        c_1: Coefficient of x^2 
        c_2: Coefficient of x
        c_3: Constant
    """

    x_vals = np.arange(-5.0, 5.0, 0.2)
    y_vals = (c_1*x_vals*x_vals) + (c_2*x_vals) + c_3

    plt.plot(x_vals, y_vals)
    plt.plot(x_vals, 0.0*x_vals)
    plt.show()



def eval_func(c_1:int, c_2:int, c_3:int, x:float) -> float:
    """
    Function to evaluate value of function at a given x.

    Args:
        c_1: Coefficient of x^2
        c_2: Coefficient of x
        c_3: Constant
        x: Value at which to evaluate the function

    Returns:
        Value of the function at x
    """
    return (c_1*x*x) + (c_2*x) + c_3



def bisection_method(c_1:int, c_2:int, c_3:int, x_1:float, x_2:float, tol:float=0.0001) -> float:
    """
    Function to find root of equation using bisection method

    Args:
        c_1: Coefficient of x^2
        c_2: Coefficient of x
        c_3: Constant
        x_1: Lower bound where function is negative
        x_2: Upper bound where function is positive
        tol: Tolerance for convergence

    Returns:
        Root of equation within specified tolerance
    """
    nsteps = 0
    x_mid = (x_1 + x_2) / 2.0
    f_mid = eval_func(c_1, c_2, c_3, x_mid)

    while abs(f_mid) > tol:
        nsteps += 1
        if f_mid > 0:
            x_2 = x_mid
        else:
            x_1 = x_mid
        
        x_mid = (x_1 + x_2) / 2.0
        f_mid = eval_func(c_1, c_2, c_3, x_mid)

    print(f"Root found at x = {x_mid} after {nsteps} iterations")
    return x_mid


def NR_method(c_1:int, c_2:int, c_3:int, x:float=1.0, tol:float=0.0001) -> float:
    """
    Function to find root of equation using Newton-Raphson method

    Args:
        c_1: Coefficient of x^2
        c_2: Coefficient of x
        c_3: Constant
        x: Initial guess for the root
        tol: Tolerance for convergence

    Returns:
        Root of equation within specified tolerance
    """
    nsteps = 0
    f_x = eval_func(c_1, c_2, c_3, x)
    f_prime_x = 2*c_1*x + c_2

    while abs(f_x) > tol:
        nsteps += 1
        x -= f_x / f_prime_x
        f_x = eval_func(c_1, c_2, c_3, x)
        f_prime_x = 2*c_1*x + c_2

    print(f"Root found at x = {x} after {nsteps} iterations")
    return x



if __name__=="__main__":

    c_1 = 1                                 #coefficient 1
    c_2 = -4                                 #coefficient 2
    c_3 = -5                                #coefficient 3

    # plot_parabola(c_1, c_2, c_2)
    print(f"Solving for equation: {c_1:+}x²{c_2:+}x{c_3:+} = 0")

    x_1 = float(input("Enter value of x₁ such that f(x₁)<0: "))
    x_2 = float(input("Enter value of x₂ such that f(x₂)>0: "))

    # do some sanity checks on x_1 and x_2
    while eval_func(c_1, c_2, c_3, x_1) > 0 or eval_func(c_1, c_2, c_3, x_2) < 0:
        if eval_func(c_1, c_2, c_3, x_1) > 0:
            x_1 = float(input("Warning! Enter value of x₁ such that f(x₁)<0: "))
        elif eval_func(c_1, c_2, c_3, x_2) < 0:
            x_2 = float(input("Warning! Enter value of x₂ such that f(x₂)>0: "))

    # call bisection method to find root
    bis_root = bisection_method(c_1, c_2, c_3, x_1, x_2)

    # call newton-raphson method to find root 
    nr_root = NR_method(c_1, c_2, c_3)
