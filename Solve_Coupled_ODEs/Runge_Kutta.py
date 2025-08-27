"""
Script implementing second order Runge-Kutta method for 
numerical integration Implemented for pendulum 
"""

import math 
import matplotlib.pyplot as plt


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


#constants for part 7
k=0.0                                                                           #damping constant
phi=0.6667                                                                      #initial phase
A=0.0                                                                           #Amplitude
g=1                                                                             #gravity
L=1                                                                             #Length of the pendulum

if __name__=="__main__":
    theta=3.0                                                                       #value of theta
    omega=0.0                                                                       #angular velocity
    t=0.0                                                                           #time
    dt=0.01                                                                         #increments with which time will increase


    #initializing lists for storing values of theta, omega and time so they could be easily plotted on the graph
    theta_list=[theta]                                                              #list for theta
    omega_list=[omega]                                                              #list for omega
    t_list=[t]                                                                      #list for time 


    #loop for finding the area of the trapezoid using Range-kutta method
    for i in range(1,1000):                                                         #the end value of 1000 was instructed to be used in the lab manual 
        #to avoid confusion k1a, k1b, k2a, k2b, k3a, k3b, k4a and k4b are used calculate parts of equation (21) and (22)
        k1a = dt * omega
        k1b = dt * eqn_pendulum(theta, omega, t, sin_approx=False)
        k2a = dt * (omega + k1b/2)  
        k2b = dt * eqn_pendulum(theta + k1a/2, omega + k1b/2, t + dt/2, sin_approx=False)
        k3a = dt * (omega + k2b/2)
        k3b = dt * eqn_pendulum(theta + k2a/2, omega + k2b/2, t + dt/2, sin_approx=False)
        k4a = dt * (omega + k3b)
        k4b = dt * eqn_pendulum(theta + k3a, omega + k3b, t + dt, sin_approx=False)

        theta=theta + (k1a + 2 * k2a + 2 * k3a + k4a)/6                             #calculating the value for equation (21) and updating the value of theta
        omega=omega + (k1b + 2 * k2b + 2 * k3b + k4b)/6                             #caluclating the value for equation (22) and updating the value of omega
        t=t+dt                                                                      #incrementing the value of t(time)

        theta_list.append(theta)                                                    #appending the updated value of theta
        omega_list.append(omega)                                                    #appending the updated value of omega
        t_list.append(t)                                                            #appending the updated value of t(time)

    plt.plot(t_list, omega_list, "blue", label=r"Angular Velocity, $\omega$")
    plt.plot(t_list, theta_list, "red", label=r"Theta $\theta$")
    plt.title("Solving Non-Linear Pendulumn Equation with initial conditions\n"+
              "Runge-Kutta Method\n"
              r"$\theta$ = {:.2f} radians | $\omega$ = {:.2f} rad/s".format(theta_list[0], omega_list[0]),
                wrap=True)
    plt.xlabel("Time (s)")
    plt.legend(loc="upper right")
    plt.ylim(-math.pi, math.pi)
    plt.grid()
    plt.show()
