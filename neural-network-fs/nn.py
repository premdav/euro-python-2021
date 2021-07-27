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

if __name__ == '__main__':
  l = Layer(3, 7)
  print(l.forward_pass(np.array([1,2,3]).reshape(3,1)))
