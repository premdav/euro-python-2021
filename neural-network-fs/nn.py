import numpy as np
from abc import abstractmethod

def generate_weight_matrix(nrows, ncols):
  return np.random.default_rng().normal(
    loc=0,
    scale=1/(nrows * ncols),
    size=(nrows, ncols),
  )

def generate_bias_factor(length):
  return generate_weight_matrix(length, 1)

class ActivationFunction:
  @abstractmethod
  def f(self, x):
    pass

  @abstractmethod
  def df(self, x):
    pass

class LeakyReLU(ActivationFunction):
  def __init__(self, alpha):
      self._alpha = alpha
      
  def f(self, x):
    return np.maximum(x, self._alpha*x)

  def df(self, x):
    return np.maximum(self._alpha, x > 0)

class LossFunction:
  @abstractmethod
  def loss(self, outs, targets):
    pass

  @abstractmethod
  def dloss(self, outs, targets):
    pass

class MSE(LossFunction):
  def loss(self, outs, targets):
    return np.mean(np.power(outs - targets, 2))

  def dloss(self, outs, targets):
    return 2 * (outs - targets) / outs.size
  

class Layer:
  '''Class representing connections between two layers of neurons'''

  def __init__(self, inps, outs, act_func):
      self._W = generate_weight_matrix(outs, inps)
      self._b = generate_bias_factor(outs)
      self._act_func = act_func

  def forward_pass(self, x):
    return self._act_func.f(np.dot(self._W, x) + self._b)

class Network:
  '''Class representing sequence of compatible layers'''
  def __init__(self, layers, lr, loss_func):
      self._layers = layers
      self._lr = lr
      self._loss_func = loss_func
    
  def forward_pass(self, x):
    out = x
    for layer in self._layers:
      out = layer.forward_pass(out)
    return out

  def loss(self, x, target):
    return self._loss_func.loss(self.forward_pass(x), target)

  def train(self, x, target):
    '''train network on inpux x and target value'''
    # accumulate all intermediate outputs
    # https://mathspp.com/blog/neural-networks-fundamentals-with-python-backpropagation
    xs = [x]
    for layer in self._layers:
      xs.append(layer.forward_pass(xs[-1]))
    
    dx = self._loss_func.dloss(xs.pop(), target)
    for layer, x in zip(self._layers[::-1], xs[::-1]):
      db = dx * layer._act_func.df(np.dot(layer._W, x) + layer._b)
      dx = np.dot(layer._W.T, db)
      dW = np.dot(db, x.T)
      layer._W -= self._lr * dW
      layer._b -= self._lr * db

if __name__ == '__main__':
  layers = [
    Layer(3, 7, LeakyReLU(0.1)),
    Layer(7, 6, LeakyReLU(0.1)),
    Layer(6, 3, LeakyReLU(0.1)),
    Layer(3, 1, LeakyReLU(0.1)),
  ]

  net = Network(layers, 0.001, MSE())

  t = np.array([0])

  inps = [
    generate_bias_factor(3) for _ in range(1_000)
  ]

  loss = 0
  for inp in inps:
    loss += net.loss(inp, t)
  print(loss)
  for _ in range(10_000):
    x = generate_bias_factor(3)
    net.train(x,t)

  loss = 0
  for inp in inps:
    loss += net.loss(inp, t)
  print(loss)
