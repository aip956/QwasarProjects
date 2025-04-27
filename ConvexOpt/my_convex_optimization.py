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
    if save_path:
        plt.savefig(save_path) # Save plot
    plt.show()

# TESTING AREA
if __name__ == "__main__":
    f = lambda x: (x - 1)**4 + x**2
    values = np.linspace(-2, 3, 100)
    print_a_function(f, values, save_path = "function_plot.png")