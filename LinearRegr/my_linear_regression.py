import numpy as np
import matplotlib.pyplot as plt

# 1. Linear Hypothesis Function
def h(x, theta):
    return x @ theta

# 2. Mean Squared Error
def mean_squared_error(y_predicted, y_label):
    error = y_predicted - y_label
    return (error ** 2).mean()

# 3. Add Bias Column
def bias_column(X):
    ones = np.ones((X.shape[0], 1))
    return np.hstack([ones, X])

# 4. Closed-form Linear Regression
class LeastSquaresRegression:
    def __init__(self):
        self.theta_ = None
    
    def fit(self, X, y):
        self.theta_ = np.linalg.inv(X.T @ X) @ X.T @ y
    
    def predict(self, X):
        return h(X, self.theta_)
    
# 5. Gradient Descent Optimizer
class GradientDescentOptimizer:
    def __init__(self, f, fprime, start, learning_rate = 0.1):
        self.f_ = f
        self.fprime_ = fprime
        self.current_ = start
        self.learning_rate_ = learning_rate
        self.history_ = [start.copy()]

    def step(self):
        gradient = self.fprime_(self.current_)
        self.current_ = self.current_ - self.learning_rate_ * gradient
        self.history_.append(self.current_.copy())

    def optimize(self, iterations = 100):
        for _ in range(iterations);
            self.step()

    def getCurrentValues(self):
        return self.current_
    
    def print_result(self):
        print("Best theta found: ", self.current_)
        print("f(theta) = ", self.f_(self.current_))
        print("f'(theta) = ", self.fprime_(self.current_))

# 6. Convex Function and its Gradient