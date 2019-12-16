import numpy as np
import matplotlib.pyplot as plt

save_path = 'image'
def mandelbrot_func(z, c):
    return z**2 + c

X,Y = np.meshgrid(np.arange(-2, 2, 0.01),np.arange(-2, 2, 0.01))
value = np.zeros_like(X.flatten())
for i,  (real, imaginary) in enumerate(zip(X.flatten(), Y.flatten())):
    z = 0 + 0j
    for count in range(50):
        c = complex(real, imaginary)
        z = mandelbrot_func(z, c)
        if (abs(z) > 2):
            value[i] = 1
            break

value = value.reshape(X.shape)

plt.contourf(X, Y, value, cmap='Greys')
plt.colorbar()
#plt.show()
plt.savefig(save_path+'/mandelbrot_square.png')