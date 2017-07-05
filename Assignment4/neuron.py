import numpy as np
def neuron(weights,input,activationFn):
    z=dotProduct(weights,input)
    if activationFn == "tanh":
        return np.tanh(z)
    else :
        k = 1/(1 + np.exp(-z))
        return k




def dotProduct(weights,input):
    return np.dot(input,weights)




