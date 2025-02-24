# %%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn import metrics 



# %% [markdown]
# Load Data in a Data Frame

# %%
# Load CSV file
dataset = pd.read_csv('boston.csv')
# print(dataset.head())
# print(dataset.info())
# print(dataset.describe())

# %% [markdown]
# Print First Rows

# %%
def print_summarize_dataset(dataset):
   print("Dataset dimension:", dataset.shape)

   print("\nFirst 10 rows of dataset:")
   print(dataset.head(10))
   print("\nStatistical summary:")
   print(dataset.describe())

print_summarize_dataset(dataset)

# %% [markdown]
# Clean the dataset

# %%
def clean_dataset(dataset):
    return dataset.dropna()

dataset = clean_dataset(dataset)

# %% [markdown]
# Generate histograms

# %%
def print_histograms(dataset):
    dataset.hist(figsize=(12, 10), bins=20)
    plt.tight_layout()
    plt.show()

print_histograms(dataset)

# %% [markdown]
# Correlation Matrix

# %%
def compute_correlations_matrix(dataset):
    """
    Computes the Pearson correlation matrix for the dataset 
    and returns it as a dictionary
    """
    correlation_matrix = dataset.corr() # Compute corr matrix
    return correlation_matrix.to_dict() # Convert to dictionary

correlations = compute_correlations_matrix(dataset)

# Access correlations for "MDEV"
if 'MDEV' in correlations:
    print("Correlations with MDEV:", correlations['MDEV'])
else:
    print("Column 'MDEV' not found in dataset.")

# %% [markdown]
# Scatter Matrix

# %%
def print_scatter_matrix(dataset):
    pd.plotting.scatter_matrix(dataset, figsize=(15, 15), diagonal='hist')
    plt.show()

print_scatter_matrix(dataset)

# %%
def plot_scatter(dataset, x_col, y_col):
    """
    Plots a scatter plot for 2 given columns
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(dataset[x_col], dataset[y_col], alpha=0.6)
    plt.title(f"{y_col} vs. {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid()
    plt.show()

    plot_scatter(dataset, 'RM', 'MDEV')
    plot_scatter(dataset, 'AGE', 'MDEV')
    plot_scatter(dataset, 'LSAT', 'MDEV')
    plot_scatter(dataset, 'CRIM', 'MDEV')


# %% [markdown]
# Model Training

# %%
def boston_fit_model(dataset):
    model_dataset = dataset[["RM", "MDEV"]]
    x = model_dataset.iloc[:, :-1].values
    y = model_dataset.iloc[:, 1].values
    regressor = LinearRegression()
    regressor.fit(x, y)
    return regressor

model = boston_fit_model(dataset)

# %% [markdown]
# 

# %% [markdown]
# Prediction

# %%
def boston_predict(estimator, array_to_predict):
    return estimator.predict([array_to_predict])

prediction = boston_predict(model, [6])
print("Prediction:", prediction)

# %% [markdown]
# Model Evaluation

# %%
def print_model_prediction_evaluator(base_test, prediction):
    print("Mean Absolute Error:", metrics.mean_absolute_error(base_test, prediction))
    print("Mean Squared Error:", metrics.mean_squared_error(base_test, prediction))
    print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(base_test, prediction)))

# Example usage with dummy data
base_test = [24, 21, 28]
predictions = [23.5, 21.2, 28.1]
print_model_prediction_evaluator(base_test, predictions)



