# Price process generator

This library provides various generators of stochastic processes modelling real price processes. The generated synthetic
price data can be used in Monte Carlo simulations (or similar statistical experiments) and potentially even to train ML
algorithms. 

Currently the implemented/planned generators are

- [Geometric Wiener motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
- [Geometric Lévy flights](https://en.wikipedia.org/wiki/L%C3%A9vy_process)
- [Ising](https://borab96.github.io/IsingPriceDynamics/ising.html) (TODO)

## Installation

``pip install price_process`` to get the current PyPi version or clone this repo and run ``pip install .`` in the directory 
for most recent version.

## Basic usage

The standard model of stochastic price dynamics is the SDE

<img src="https://latex.codecogs.com/svg.image?\color[rgb]{0.36,&space;0.54,&space;0.66}dP_t&space;=&space;\mu&space;S_t&space;dt&plus;\sigma&space;S_tdW_t" title="dP_t = \mu S_t dt+\sigma S_tdW_t" />

with solution the *geometric Brownian motion*

<img src="https://latex.codecogs.com/svg.image?\color[rgb]{0.36,&space;0.54,&space;0.66}P_t&space;=&space;P_0e^{\mu&space;t&plus;\frac{1}{2}t^2&space;\sigma}" title="\color[rgb]{0.36, 0.54, 0.66}P_t = P_0e^{\mu t+\frac{1}{2}t^2 \sigma}" />

In order to display, say 10 samples of a 1000 point process, one would run

````
from price_process.process import *
price_proc = Gaussian([1000, 10]).to_geometric(0, 0.04)
price_proc.plot()
````
![out1](examples/figures/exp_gaussian_ex.png)

The `np.ndarray` output is accessed through 
``
price_proc.process
``
## Custom process

Custom generators can be implemented by subclassing ``Process``. Here is how one might implement the gamma process
for instance

````
from price_process.process import *
from scipy.stats import gamma
import numpy as np

class Gamma(Process):
    def __init__(self, alpha, beta, size, initial=0, T=1):
        super().__init__(size, initial=initial, T=T)
        self.alpha, self.beta = alpha, beta
        self.rvs = gamma.rvs(alpha, size=self.size, scale=1/self.beta)
        self.process = np.cumsum(self.rvs, axis=0)
````

See [this](https://datalore.jetbrains.com/view/notebook/7ePCXEffpdZr2dA5ySdwr1) for a more advanced use case.
