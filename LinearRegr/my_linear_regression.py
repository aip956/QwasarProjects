import numpy as np
import matplotlib.pyplot as plt

# 1. Linear Hypothesis Function
def h(x, theta):
    return x @ theta

# # 2. Mean Squared Error
# def mean_squared_error(y_predicted, y_label):
#     error = y_predicted - y_label
#     return (error ** 2).mean()

# # 3. Add Bias Column
# def bias_column(X):
#     ones = np.ones((X.shape[0], 1))
#     return np.hstack([ones, X])

# # 4. Closed-form Linear Regression
# class LeastSquaresRegression:
#     def __init__(self):
#         self.theta_ = None
    
#     def fit(self, X, y):
#         self.theta_ = np.linalg.inv(X.T @ X) @ X.T @ y
    
#     def predict(self, X):
#         return h(X, self.theta_)
    
# # 5. Gradient Descent Optimizer
# class GradientDescentOptimizer:
#     def __init__(self, f, fprime, start, learning_rate = 0.1):
#         self.f_ = f
#         self.fprime_ = fprime
#         self.current_ = start
#         self.learning_rate_ = learning_rate
#         self.history_ = [start.copy()]

#     def step(self):
#         gradient = self.fprime_(self.current_)
#         self.current_ = self.current_ - self.learning_rate_ * gradient
#         self.history_.append(self.current_.copy())

#     def optimize(self, iterations = 100):
#         for _ in range(iterations);
#             self.step()

#     def getCurrentValues(self):
#         return self.current_
    
#     def print_result(self):
#         print("Best theta found: ", self.current_)
#         print("f(theta) = ", self.f_(self.current_))
#         print("f'(theta) = ", self.fprime_(self.current_))

# # 6. Convex Function and its Gradient
# def f(x):
#     diff = x - np.array([2, 6])
#     return 3 + diff.T @ diff

# def fprime(x):
#     return 2 * (x - np.array([2, 6]))

# # 7. Plotting Helper Functions
# def my_plot(X, y, y_pred):
#     plt.scatter(X, y, label = "Data")
#     plt.plot(X, y_pred, color = 'red', label = "Prediction")
#     plt.legend()
#     plt.title("Linear Fit")
#     plt.show()

# def plot_3d_and_path(history, f):
#     from mpl_toolkits.mplot3d import Axes3D
#     history = np.array(history)
#     x_vals = np.linspace(0, 4, 100)
#     y_vals = np.linspace(4, 8, 100)
#     X_grid, Y_grid = np.meshgrid(x_vals, y_vals)


if __name__ == "__main__":
    print("Test h(x, theta):")
    x_test = np.array([[1, 2], [1, 3], [1, 4]]) # bias + feature
    theta_test = np.array([[1], [2]]) # theata0 = 1, theta1 = 2
    expected = np.array([[5], [7],[9]])
    actual = h(x_test, theta_test)
    print("Expected: ", expected)
    print("Actual: ", actual)
    assert np.allclose(actual, expected), "h(x, theta) failed!"