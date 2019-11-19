import numpy as np

# 恒等関数
def identity_function(x):
    return x

# ステップ関数
def step_function(x):
    y = x > 0
    return y.astype(np.int)

# シグモイド関数
def sigmoid(x):
    y = 1 / (1+np.exp(-x))
    return y

# ReLu(Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)



# softmax
#def softmax(x):