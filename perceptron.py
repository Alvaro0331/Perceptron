
import numpy as np

w = np.array([-1.5, 1, 1])
x= np.array([[0,0],[0,1],[1,0],[1,1]])

def perceptron(w, x):
    x_prima= np.hstack((np.ones((x.shape[0], 1)), x))
    v=np.dot(w, x_prima.T)
    y= v >= 0
    
    
    return y

print(perceptron(w, x))