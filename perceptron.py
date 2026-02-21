import numpy as np

def perceptron(w, x):
    x_prima= np.hstack((np.ones((x.shape[0], 1)), x))
    v=np.dot(w, x_prima.T)
    y= v >= 0
        
    return y
