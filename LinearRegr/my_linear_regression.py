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
        for _ in range(iterations):
            self.step()

    # Getter
    def getCurrentValue(self):
        return self.current_
    
    def print_result(self):
        print("Best theta found: ", self.current_)
        print("f(theta) = ", self.f_(self.current_))
        print("f'(theta) = ", self.fprime_(self.current_))

# 6. Convex Function and its Gradient
def f(x):
    diff = x - np.array([2, 6])
    return 3 + diff.T @ diff

def fprime(x):
    return 2 * (x - np.array([2, 6]))

# 7. Plotting Helper Functions
def my_plot(X, y, y_pred):
    plt.scatter(X, y, label = "Data")
    plt.plot(X, y_pred, color = 'red', label = "Prediction")
    plt.legend()
    plt.title("Linear Fit")
    plt.show()

def plot_3d_and_path(history, f):
    from mpl_toolkits.mplot3d import Axes3D
    history = np.array(history)
    x_vals = np.linspace(0, 4, 100)
    y_vals = np.linspace(4, 8, 100)
    X_grid, Y_grid = np.meshgrid(x_vals, y_vals)
    Z = np.array([[f(np.array([x, y])) for x in x_vals] for y in y_vals])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(X_grid, Y_grid, Z, alpha = 0.6)
    ax.plot(history[:, 0], history[:, 1], [f(p) for p in history], color = 'red', marker = 'o')
    ax.set_title("Gradient Descent Path")
    plt.show()

# 8. Main Program Execution
if __name__ == "__main__":
    # print("\nTest h(x, theta):")
    # x_test = np.array([[1, 2], [1, 3], [1, 4]]) # bias + feature
    # theta_test = np.array([[1], [2]]) # theata0 = 1, theta1 = 2
    # expected = np.array([[5], [7],[9]])
    # actual = h(x_test, theta_test)
    # print("Expected:\n", expected)
    # print("Actual:\n", actual)
    # assert np.allclose(actual, expected), "h(x, theta) failed!"

    # print("Test MSE:")
    # y_pred = np.array([[5], [7], [9]])
    # y_true = np.array([[5], [6], [10]])
    # expected_mse = ((0**2 + 1**2 + 1**2) / 3)
    # actual_mse = mean_squared_error(y_pred, y_true)
    # print("Expected: ", expected_mse)
    # print("Predicted: ", actual_mse)
    # assert np.allclose(actual_mse, expected_mse), "MSE function failed!"

    # print("Test Least Squares Regr:")
    # X_known = np.array([[1], [2], [3]])
    # y_known = np.array([[3], [5], [7]]) # true θ0 = 1, θ1 = 2

    # X_known_bias = bias_column(X_known)
    # model = LeastSquaresRegression()
    # model.fit(X_known_bias, y_known)
    # print("Learned Theta:\n", model.theta_)
    # expected_theta = np.array([[1], [2]])
    # assert np.allclose(model.theta_, expected_theta), "Least Squares Regression failed!"

    # y_pred_known = model.predict(X_known_bias)
    # print("Predictions:\n", y_pred_known)
    # assert np.allclose(y_pred_known, y_known), "Prediction mismatch!"

    # Linear Regression Part
    X = 4 * np.random.rand(100, 1)
    y = 10 + 2 * X + np.random.randn(100, 1)

    X_bias = bias_column(X)
    model = LeastSquaresRegression()
    model.fit(X_bias, y)
    y_pred = model.predict(X_bias)

    print("Learned weights:", model.theta_)
    my_plot(X, y, y_pred)

    # Gradient Descent Part
    start = np.random.normal(size = (2,))
    optimizer = GradientDescentOptimizer(f, fprime, start, learning_rate = 0.1)
    optimizer.optimize(10)
    optimizer.print_result()
    plot_3d_and_path(optimizer.history_, f)
