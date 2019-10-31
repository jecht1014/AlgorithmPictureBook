import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from gaussian_def.gaussian_process import *

# カーネルを通してできた共分散行列を用いて多変量正規乱数を出力した結果
# kernelsにはリストに入れたカーネルかカーネルを入れる、plot_kはboolでTrueならば共分散行列のplot
def kernel_plot(kernels, params, plot_k):
    x = np.arange(-5, 5, 0.05)
    x2 = np.reshape(x, (x.shape[0], 1))

    if type(kernels) is not list:
        kernels = [kernels]
        params = [params]
    
    for i, kernel in enumerate(kernels):
        if (i == 0):
            k = make_k(x2, params[i], kernel, [0, 1])
        else:
            k *= make_k(x2, params[i], kernel, [0, 1])
    #r = np.reshape(mvnrnd(k), (x.shape[0]))
    for _ in range(3):
        r = np.reshape(np.random.multivariate_normal(np.zeros(k.shape[0]), k), (x.shape[0]))
        if (plot_k):
            plt.subplot(1,2,1)
            plt.plot(x, r.T)
            plt.subplot(1,2,2)
            plt.imshow(k, cmap = 'Greys')
        else:
            plt.plot(x, r.T)
    
    #plt.savefig('image/chapter3/linear_kernel.png')
    plt.show()
    

def gaussian_process_plot():
    xtrain = np.linspace(-5, 5, 11)
    xtrain = xtrain.reshape(xtrain.shape[0], 1)
    noise_var = 0.1
    ytrain = np.sin(xtrain) + np.random.normal(0, noise_var, (xtrain.shape[0], 1))
    ytrain = ytrain - np.mean(ytrain)

    xtest = np.linspace(-6, 6, 500)
    xtest = xtest.reshape(xtest.shape[0], 1)
    ytest = np.sin(xtest)

    params = [np.log(1), np.log(1), np.log(noise_var)]
    mu, var = gaussian_process2(xtrain, xtest, ytrain, ytest, params, rbf)

    plt.plot(xtest.reshape(xtest.shape[0]), mu)
    plt.plot(xtest, ytest)
    #print(xtest, mu-2*np.sqrt(var))
    #print(var)
    plt.fill_between(xtest.reshape(xtest.shape[0]), mu-2*np.sqrt(var), mu+2*np.sqrt(var), color = '#ccccff')
    plt.scatter(xtrain, ytrain, c='green')

    #plt.savefig('image/chapter3/hyper_parameter_estimate.png')
    plt.show()

#kernel_plot([periodic_kernel, exponential_kernel], [[np.log(1), np.log(1), np.log(1)], [np.log(1), np.log(1)]], False)
#kernel_plot(linear_kernel, [np.log(1)], True)
gaussian_process_plot()