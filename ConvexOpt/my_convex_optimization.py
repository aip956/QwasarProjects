import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# 1.Plot a function
def print_a_function(f, values, save_path = None, minimum_x = None):
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
    plt.close()

# 2. Write and Test Bisection Method
# Method findes where function crosses 0 between 2 points
# Where f′(x) = 0, where the slope is flat, is the min
def find_root_bisection (f, a, b, tol = 0.001):
    # Find a root of f between a and b using bisection method
    iterations = 0
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0 or (b - a) < tol:
            print(f"Bisection iterations: ", iterations)
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
    print(f"Bisection iterations: ", iterations)
    return (a + b) / 2

# 3. Find root with Newton - Raphson
def find_root_newton_raphson(f_prime, f_double_prime, x0, tol = 0.001, max_iter = 100):
    # Find root of f' using Newton-Raphson method starting from x0
    x = x0
    iterations = 0
    for _ in range(max_iter):
        fx = f_prime(x)
        if abs(fx) < tol:
            print(f"N-R iterations: ", iterations)
            return x
        fpx = f_double_prime(x)
        if fpx == 0:
            raise ValueError("Zero derivative encountered; no solution found.")
        x = x - fx / fpx
        iterations += 1
    raise ValueError("Max iterations reached without convergence.")

# 4. Gradient Descent
def gradient_decent(f, f_prime, start, learning_rate = 0.1, tol = 0.001, max_iter = 10000):
    # Find the min of f using Grad Desc starting from 'start'
    x = start
    iterations = 0
    for _ in range(max_iter):
        grad = f_prime(x)
        if abs(grad) < tol:
            print ("Gradient Descent iterations: ", iterations)
            return x
        x = x - learning_rate * grad
        iterations += 1
    print("Gradient Descent reached max iterations: ", iterations)
    return x
    
# 5. Linear Programming with Simplex
def solve_linear_problem(A, b, c):
    # Solve a linear protramming problem of the form maximize c^T x subject to Ax <= b.
    # scipy minimizes, so t maximize we pass -c
    res = linprog(c, A_ub = A, b_ub = b, method = 'simplex')
    if res.success:
        return res.fun, res.x
    else:
        raise ValueError("Simplex optimization failed")
    





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
    # print_a_function(f, values, save_path = "2function_plot.png", minimum_x = root)

    # Newton-Raphson method
    f_double_prime = lambda x: 12 * (x - 1) ** 2 + 2 # 2nd derrivative of f
    root_newton = find_root_newton_raphson(f_prime, f_double_prime, x0 = -1)
    print("Root found by Newton-Raphson at x = ", root_newton)
    print("Value of f at that x: ", f(root_newton))
    
    # Gradient Descent method
    start = -1 #Starting point
    x_min = gradient_decent(f, f_prime, start, learning_rate=0.01)
    print("Minimum found by Gradient Descent at x = ", x_min)
    print("Value of f at that x: ", f(x_min))
    
    # Solve linear programming program
    A = np.array([
        [2, 1],
        [-4, 5],
        [1, -2]
    ])
    b = np.array([10, 8, 3])
    c = np.array([-1, -2]) #Note negative signs for maximization

    optimal_value, optimal_arg = solve_linear_problem(A, b, c)
    print("Optimal value (max'd z) is: ", -optimal_value) #Flip back to positive
    print("Optimal x and y values: ", optimal_arg)
    