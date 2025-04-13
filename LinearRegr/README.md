# Welcome to My Linear Regression

## Task
The task is to build a simple linear regression model to predict continuous outcomes based on one feature. The challenge is to find the best fitting line using two different techniques:
- The Closed-Form Solution (Normal Equation)
- Gradient Descent Optimization
The goal is to minimize the Mean Squared Error (MSE) between the data and prediction model.


## Description
This project demonstrates both analytical and iterative methods to solve a regression problem from scratch using Python and NumPy

The steps include:
- Define a linear hypothesis function
- Implement a cost function (MSE)
- Solve for optimial weights (theta) using:
  - The Normal Equation (Least Squares)
  - Gradient Descent
- Visualize model predictions and the gradient descent trajectory
- Explore the effect of hyperparameters like learning rate and iterations on convergence.


## Installation
Python3 and NumPy
```
pip install numpy matplotlib
```
Clone this repo and drun the Python scripts directly


## Usage
To train and test the linear regression model using synthetic data:
```
python3 linear_regression.py
```
To run and visualize gradient descent optimization on a convex function:
```
python3 gradient_descent.py
```
Make sure to check the plots for model fit and optimizer progression.

### The Core Team