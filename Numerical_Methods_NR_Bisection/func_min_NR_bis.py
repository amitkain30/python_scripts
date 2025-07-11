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

    x_vals = np.arange(-10.0, 10.0, 0.2)

    plt.plot(x_vals, eval_func(c_1, c_2, c_3, x_vals))
    plt.title(r"$f(x) = {:+}x^2{:+}x{:+}$".format(c_1, c_2, c_3))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', lw=0.5, ls='solid')
    plt.axvline(0, color='black', lw=0.5, ls='solid')
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



def bisection_method(c_1:int, c_2:int, c_3:int, init_x_1:float, init_x_2:float) -> float:
    """
    Function to find root of equation using bisection method

    Args:
        c_1: Coefficient of x^2
        c_2: Coefficient of x
        c_3: Constant
        init_x_1: Lower bound where function is negative
        init_x_2: Upper bound where function is positive
        tol: Tolerance for convergence

    Returns:
        Root of equation within specified tolerance
    """

    tol_list = []
    nsteps_list = []
    f_mid_list = []
    x_mid_list = []

    for i in range(0, 20):
        tol = 10**(-i)
        nsteps = 0

        # Make sure x_1 and x_2 are the same as initial values
        x_1 = init_x_1
        x_2 = init_x_2

        x_mid = (x_1 + x_2) / 2.0
        f_mid = eval_func(c_1, c_2, c_3, x_mid)

        while abs(f_mid) > tol:
            nsteps += 1
            if f_mid > 0:
                x_2 = x_mid
            elif f_mid < 0:
                x_1 = x_mid
            
            x_mid = (x_1 + x_2) / 2.0
            f_mid = eval_func(c_1, c_2, c_3, x_mid)
            f_mid_list.append(f_mid)
            x_mid_list.append(x_mid)

        tol_list.append(np.log10(tol))
        nsteps_list.append(nsteps)

    # Plotting the results 
    fig, axs = plt.subplots(2, 1, figsize=(6, 6))
    axs[0].plot(np.arange(-10.0, 10.0, 0.2), eval_func(c_1, c_2, c_3, np.arange(-10.0, 10.0, 0.2)), label='f(x)')
    axs[0].plot(x_mid_list, f_mid_list, 'ro-', label='Bisection Points')
    axs[0].set_title(r"Bisection Method: $f(x) = {:+}x^2{:+}x{:+}$".format(c_1, c_2, c_3))
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("f(x)")
    axs[0].axhline(0, color='black', lw=0.5, ls='solid')
    axs[0].axvline(0, color='black', lw=0.5, ls='solid')
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(tol_list, nsteps_list, '.-')
    axs[1].set_title("Number of Steps for Different Tolerances")
    axs[1].set_xlabel(r"$Log_{10}(Tolerance)$")
    axs[1].set_ylabel("Number of Steps")
    axs[1].axhline(0, color='black', lw=0.5, ls='solid')
    axs[1].axvline(0, color='black', lw=0.5, ls='solid')
    axs[1].grid(True)

    fig.suptitle("Bisection Method Results", fontsize = 16)

    plt.tight_layout()
    plt.show()

    print(f"Root found at x = {x_mid} after {nsteps} iterations")
    return x_mid



def NR_method(c_1:int, c_2:int, c_3:int, init_x:float=-5) -> float:
    """
    Function to find root of equation using Newton-Raphson method

    Args:
        c_1: Coefficient of x^2
        c_2: Coefficient of x
        c_3: Constant
        init_x: Initial guess for the root
        tol: Tolerance for convergence

    Returns:
        Root of equation within specified tolerance
    """
    nsteps = 0
    f_x = eval_func(c_1, c_2, c_3, init_x)
    f_prime_x = 2*c_1*init_x + c_2                                           #derivative of function

    nsteps_list = []
    tol_list = []
    x_list = [init_x]
    fx_list = [f_x]


    for i in range(0, 20):
        tol = 10**(-i)
        x = init_x
        nsteps = 0
        f_x = eval_func(c_1, c_2, c_3, x)
        f_prime_x = 2*c_1*x + c_2

        while abs(f_x) > tol:
            nsteps += 1
            x -= f_x / f_prime_x
            f_x = eval_func(c_1, c_2, c_3, x)
            f_prime_x = 2*c_1*x + c_2

        nsteps_list.append(nsteps)
        tol_list.append(np.log10(tol))
        x_list.append(x)
        fx_list.append(f_x)


    # Plotting the results
    fig, axs = plt.subplots(2, 1, figsize=(6, 6))
    axs[0].plot(np.arange(-10.0, 10.0, 0.2), eval_func(c_1, c_2, c_3, np.arange(-10.0, 10.0, 0.2)), label='f(x)')
    axs[0].plot(x_list, fx_list, 'ro-', label='Newton-Raphson Points')
    axs[0].set_title(r"Newton-Raphson Method: $f(x) = {:+}x^2{:+}x{:+}$".format(c_1, c_2, c_3))
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("f(x)")
    axs[0].axhline(0, color='black', lw=0.5, ls='solid')
    axs[0].axvline(0, color='black', lw=0.5, ls='solid')
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(tol_list, nsteps_list, '.-')
    axs[1].set_title("Number of Steps for Different Tolerances")
    axs[1].set_xlabel(r"$Log_{10}(Tolerance)$")
    axs[1].set_ylabel("Number of Steps")
    axs[1].axhline(0, color='black', lw=0.5, ls='solid')
    axs[1].axvline(0, color='black', lw=0.5, ls='solid')
    axs[1].grid(True)

    fig.suptitle("Newton-Raphson Method Results", fontsize = 16)

    plt.tight_layout()
    plt.show()

    print(f"Root found at x = {x} after {nsteps} iterations")
    return x



if __name__=="__main__":

    c_1 = 1                                 #coefficient 1
    c_2 = -4                                 #coefficient 2
    c_3 = -5                                #coefficient 3

    plot_parabola(c_1, c_2, c_2)
    
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
