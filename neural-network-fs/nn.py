import numpy as np

def generate_weight_matrix(nrows, ncols):
  return np.random.default_rng().normal(
    loc=0,
    scale=1/(nrows * ncols),
    size=(nrows, ncols),
  )

def generate_bias_factor(length):
  return generate_weight_matrix(length, 1)

class Layer:
  '''Class representing connections between two layers of neurons'''

  def __init__(self, inps, outs):
      self._W = generate_weight_matrix(outs, inps)
      self._b = generate_bias_factor(outs)

  def forward_pass(self, x):
    return np.dot(self._W, x) + self._b

class Network:
  '''Class representing sequence of compatible layers'''
  def __init__(self, layers):
      self._layers = layers
    
  def forward_pass(self, x):
    out = x
    for layer in self._layers:
      out = layer.forward_pass(out)
    return out

if __name__ == '__main__':
  layers = [
    Layer(3, 7),
    Layer(7, 6),
    Layer(6, 2),
  ]

  net = Network(layers)
  print(
    net.forward_pass(np.array([1, 2, 3]).reshape((3, 1)))
  )