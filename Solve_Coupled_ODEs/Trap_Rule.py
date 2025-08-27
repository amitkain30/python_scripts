"""
Script to implement Trapezoidal method and using it to solve 
Linear and Non-Linear pendulum 
"""

import matplotlib.pyplot as plt
import math


def eqn_pendulum(theta:float, omega:float, time:float, sin_approx:bool=True)->float:
    """
    Function to return solved equation of moition for a pendulum

    Args:
        theta: Value of Theta (angle string makes with the normal)
        omega: value for angular velocity (d_theta/time_step)
        time: value for time
        sin_approx: bool to indicate whether to use sin theta approximation or not

    Return:
        motion: Value for equation of motion at current time 
    """

    damping_term = -(k*omega)
    driving_force = A*math.cos(phi*time)

    if sin_approx==True:
        motion = ((-g/L)*theta) + damping_term + driving_force

    else:
        motion = ((-g/L)*math.sin(theta)) + damping_term + driving_force

    return motion



def pen_lin_eqn(theta:float, omega:float, 
                total_time:int=1000, time_step:float=0.01):
    """
    Evolving the pendulum equation in a linear case

    Args:
        theta: initial value of theta
        omega: intial angular velocity 
        total_time: total number of steps to be used
        time_step: value for incrementing time value
    """

    t = 0.0
    theta_lst = [theta]
    omega_lst = [omega]
    time_lst = [t]

    #implement Trapezoidal Rule
    for i in range(1, total_time):
        k1a=time_step*omega                                                                
        k1b=time_step*eqn_pendulum(theta, omega, t)
        k2a=time_step*(omega+k1b)
        k2b=time_step*eqn_pendulum(theta+k1a, omega+k1b, t+time_step)                                                     #calculating the value for equation (21) and updating the value of theta
        
        theta=theta+(k1a+k2a)/2                                                     #calculating the value for equation (21) and updating the value of theta
        omega=omega+(k1b+k2b)/2                                                     #caluclating the value for equation (22) and updating the value of omega
        t=t+time_step                                                               #incrementing the value of t(time)                                      

        theta_lst.append(theta)                                                    #appending the updated value of theta
        omega_lst.append(omega)                                                    #appending the updated value of omega
        time_lst.append(t)                                                         #appending the updated value of t(time)

    plt.plot(time_lst, omega_lst, "blue", label=r"Angular Velocity, $\omega$")
    plt.plot(time_lst, theta_lst, "red", label=r"Theta $\theta$")
    plt.title(r"Solving Linear Pendulumn Equation with initial conditions $\theta$ = {:.2f} radians | $\omega$ = {:.2f} rad/s".format(theta_lst[0], omega_lst[0]),
                wrap=True)
    plt.xlabel("Time (s)")
    plt.legend(loc="upper right")
    plt.ylim(-math.pi, math.pi)
    plt.grid()
    plt.show()


def pen_non_lin_eqn(theta:float, omega:float, 
                total_time:int=1000, time_step:float=0.01):
    """
    Evolving the pendulum equation in a non-linear case

    Args:
        theta: initial value of theta
        omega: intial angular velocity 
        total_time: total number of steps to be used
        time_step: value for incrementing time value
    """

    t = 0.0
    theta_lst = [theta]
    omega_lst = [omega]
    time_lst = [t]

    #implement Trapezoidal Rule
    for i in range(1, total_time):
        k1a=time_step*omega                                                                
        k1b=time_step*eqn_pendulum(theta, omega, t, sin_approx=False)
        k2a=time_step*(omega+k1b)
        k2b=time_step*eqn_pendulum(theta+k1a, omega+k1b, t+time_step, sin_approx=False)                                                     #calculating the value for equation (21) and updating the value of theta
        
        theta=theta+(k1a+k2a)/2                                                     #calculating the value for equation (21) and updating the value of theta
        omega=omega+(k1b+k2b)/2                                                     #caluclating the value for equation (22) and updating the value of omega
        t=t+time_step                                                               #incrementing the value of t(time)                                      

        theta_lst.append(theta)                                                    #appending the updated value of theta
        omega_lst.append(omega)                                                    #appending the updated value of omega
        time_lst.append(t)                                                         #appending the updated value of t(time)

    plt.plot(time_lst, omega_lst, "blue", label=r"Angular Velocity, $\omega$")
    plt.plot(time_lst, theta_lst, "red", label=r"Theta $\theta$")
    plt.title(r"Solving Non-Linear Pendulumn Equation with initial conditions $\theta$ = {:.2f} radians | $\omega$ = {:.2f} rad/s".format(theta_lst[0], omega_lst[0]),
                wrap=True)
    plt.xlabel("Time (s)")
    plt.legend(loc="upper right")
    plt.ylim(-math.pi, math.pi)
    plt.grid()
    plt.show()


# Constants part 4 and 5
k=0.0                                               #damping constant
phi=0.66667                                         #initial phase
A=0.0                                               #Amplitude
g=1                                                 #gravity
L=1                                                 #Length of the pendulum


if __name__=="__main__":
    pen_lin_eqn(theta=3.1, omega=0.0)
    pen_non_lin_eqn(theta = 3.1, omega=0.0)

    

                                          

    

