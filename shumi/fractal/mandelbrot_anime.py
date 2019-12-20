import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

save_path = 'image'
def mandelbrot_func(z, p, c):
    return z**p + c

fig = plt.figure()
pow_range = np.linspace(0, 6, 600)
X,Y = np.meshgrid(np.arange(-2, 1.5, 0.01),np.arange(-2, 2, 0.01))
def plot(p):
    if p != 0:
        print(p)
        plt.cla()
    value = np.zeros_like(X.flatten())
    for i,  (real, imaginary) in enumerate(zip(X.flatten(), Y.flatten())):
        z = 0 + 0j
        for _ in range(50):
            c = complex(real, imaginary)
            z = mandelbrot_func(z, p, c)
            if (abs(z) > 2):
                value[i] = 1
                break

    value = value.reshape(X.shape)

    plt.title('f(z)=z**{0:.4}+C'.format(p))
    plt.contourf(X, Y, value, cmap='Greys')
    #plt.show()
    #plt.savefig(save_path+'/mandelbrot_square.png')
ani = anm.FuncAnimation(fig, plot, interval=25, frames=pow_range)
ani.save(save_path+'/mandelbrot_power.gif', writer='pillow')