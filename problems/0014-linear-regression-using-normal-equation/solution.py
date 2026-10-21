import numpy as np

def linear_regression_normal_equation(X, y):
    X = np.array(X)
    y = np.array(y)

    w = np.linalg.solve(X.T @ X, X.T @ y)

    return [round(float(coef), 4) for coef in w]
