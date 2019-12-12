import numpy as np
import matplotlib.pyplot as plt

def numerical_integration(function, section, sequence_num=1000):
    sequence = np.linspace(section[0], section[1], sequence_num)
    result = 0
    for i in range(len(sequence)-1):
        result += (function(sequence[i])+function(sequence[i+1])) * (sequence[i+1]-sequence[i]) / 2
    return result

def fourier_series_expansion(function, section, expansion_num, x):
    T = section[1] - section[0]
    a0 = (2/T) * numerical_integration(function, section)
    y = a0/2
    for i in range(1, expansion_num+1):
        def a_function(x):
            return function(x)*np.cos(2*np.pi*i*x/T)
        def b_function(x):
            return function(x)*np.sin(2*np.pi*i*x/T)
        a = (2/T)*numerical_integration(a_function, section)
        b = (2/T)*numerical_integration(b_function, section)
        
        y += a*np.cos(2*np.pi*i*x/T) + b*np.sin(2*np.pi*i*x/T)
    return y


save_path = 'image'
def func(x):
    return x*x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
true_y = func(x)
y = fourier_series_expansion(func, [-np.pi, np.pi], 8, x)
plt.plot(x, y)
#plt.plot(x, true_y)
plt.show()