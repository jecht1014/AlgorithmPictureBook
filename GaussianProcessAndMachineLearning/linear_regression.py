import numpy as np

def simple_regression(xn, yn):
    n = xn.shape[0]
    a = (np.sum(np.square(xn)) * np.sum(yn) - np.sum(xn) * np.sum(xn * yn)) / (n * np.sum(np.square(xn)) - np.square(np.sum(xn)))
    b = (n * np.sum(xn * yn) - np.sum(xn) * np.sum(yn)) / (n * np.sum(np.square(xn)) - np.square(np.sum(xn)))

    return a, b

def multiple_regression(X, y):
    w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
    return w