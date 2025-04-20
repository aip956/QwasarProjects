import numpy as np
import matplotlib.pyplot as plt

# 1. Linear Hypothesis Function
def h(x, theta):
    return x @ theta

# 2. Mean Squared Error
def mean_squared_error(y_predicted, y_label):
    