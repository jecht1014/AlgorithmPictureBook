# chapter1
import numpy as np

def simple_regression(xn, yn):
    n = xn.shape[0]
    a = (np.sum(np.square(xn)) * np.sum(yn) - np.sum(xn) * np.sum(xn * yn)) / (n * np.sum(np.square(xn)) - np.square(np.sum(xn)))
    b = (n * np.sum(xn * yn) - np.sum(xn) * np.sum(yn)) / (n * np.sum(np.square(xn)) - np.square(np.sum(xn)))

    return a, b

def multiple_regression(X, y):
    w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
    return w

def linear_regression(phi, y):
    w = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)), phi.T), y)
    return w

def ridge_regression(X, y, alfa = 0.1):
    w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + alfa * np.eye(np.dot(X.T, X).shape[0])), X.T), y)
    return w