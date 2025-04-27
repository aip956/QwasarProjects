import numpy as np
import matplotlib.pyplot as plt

# 1.Plot a function
def print_a_function(f, values, save_path = None):
    y = [f(val) for val in values]
    plt.plot(values, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Function Plot")
    plt.grid()
    
    # If minimum_x is given, plot it:
    if minimum_x is not None:
        plt.scatter(minimum_x, f(minimum_x), color = 'red', marker = 'x', label = 'Minimum')
        plt.legend()

    if save_path:
        plt.savefig(save_path) # Save plot
    plt.show()

# 2. Write and Test Bisection Method
# Method findes where function crosses 0 between 2 points
# Where f′(x) = 0, where the slope is flat, is the min
def find_root_bisection (f, a, b, tol = 0.001):
    # Find a root of f between a and b using bisection method
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0 or (b - a) < tol:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

# TESTING AREA
if __name__ == "__main__":
    f = lambda x: (x - 1)**4 + x**2
    f_prime = lambda x: 4 * (x - 1) ** 3 + 2 * x # Derivative of f

    values = np.linspace(-2, 3, 100)

    # Find the min first and then test bisection
    root = find_root_bisection(f_prime, a = -2, b = 2)
    print("Root found by Bisection Method at x = ", root)
    print("Value of fa at that x: ", f(root))

    # Plot function and mark min
    print_a_function(f, values, save_path = "2function_plot.png", minimum_x = root)

    
    
    