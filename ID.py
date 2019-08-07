import numpy as np
from numpy import random

print(np.shape)
import matplotlib.pyplot as plt


class Neuron:
    def __init__(self):
        random.seed(1)
        ## Gives you random weights
        self.weights = initial_weights = 2 * random.random((1, 1)) - 1
    def tanh_derivative  (self,x):
        return 1- np.tanh(x)**2

    def step(self, x):
        dot_product=np.dot(x, self.weights)
        return np.tanh(dot_product)
    def train(self,iterations, train_input, train_outputs):
        for i in range (iterations):
            output=self.step(train_input)
            error= train_outputs -output
            adjustment=np.dot(train_input.T,(error*self.tanh_derivative(output)))
            self.weights+=adjustment
def fucntion(x):
    return 2*x

x=[i/100 for i in range (300)]
y=[fucntion(i/100) for i in range (300)]
data=[]
for i in range(300):
    data.append(fucntion(i/100)+random.randint(1,100)/50)

plt.plot(data,"b")
plt.show()
