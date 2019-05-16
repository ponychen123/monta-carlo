import numpy as np
import math
import random
from matplotlib import pyplot as plt

def get_rand_number(min_value, max_value):
    return random.uniform(min_value, max_value)

def f_of_x(x):
#    the function we want to integrate
    return (math.e**(-1*x))/(1+(x-1)**2)

def g_of_x(x, A, lamda):
#    weight function
    return A*math.pow(math.e, -1*lamda*x)

def inverse_G_of_r(r, lamda):
# inverse function of the integeration of g
    return (-1*math.log(float(r)))/lamda


def importance_sampling_MC(lamda, num_samples):
    A = lamda

    running_total = 0
    for i in range(num_samples):
        r = get_rand_number(0, 1)
        running_total += f_of_x(inverse_G_of_r(r, lamda=lamda))/g_of_x(inverse_G_of_r(r, lamda=lamda), A, lamda)
        approximation = float(running_total/num_samples)
        return approximation

#run importance MC
num_samples = 10000
optimal_lamda = 1.65
approx = importance_sampling_MC(optimal_lamda, num_samples)
print(f"Importance Sampling Approximation : {approx}")


