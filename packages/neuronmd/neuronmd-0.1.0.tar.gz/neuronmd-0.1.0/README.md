# NeuronMd

Package for simulating different spiking neuron models.

## Installation
Install using `pip`:
```bash
pip install neuronmd
```
Clone the repository:
```bash
git clone https://github.com/sowmyamanojna/neuronmd
```
Then, `cd` into the directory and run:
```bash
pip install .
```

## Neuron Models
### Hodgkin-Huxley Neuron Model
The HH neuron model can be simulated by creating an instance of the `HHNeuron` class.  

The code is as follows:
```python
import numpy as np
from neuronmd import HHNeuron

# Initialize a HH Neuron Class
hhneuron = HHNeuron()

# tmax - Max time (ms) to simulate the neuron
# dt - time step of simulation
# I - Current for simulating the neuron

tmax = 100
dt = 0.01
I = 0.1
t = np.arange(0, tmax, dt)

# Simulate the neuron for a single current instance
hhneuron.simulate(t, I)
# Plot the results
hhneuron.plot()

# View the variation in the state of the dynamical 
# system, as the input current is varied.
current_list = np.arange(0.01, 0.5, 0.01)
hhneuron.animate(t, ylim=[-85,40], current_list=current_list)
hhneuron.animate(t, current_list=current_list, name="no_ylim")
```

The results obtained from the above code:
![](images/hh_1.gif)

The default parameters used in the model are:
```python
v = -65 # mV
vna = 50 # mV
vk = -77 # mV
vl = -54.387 # mV

gnamax = 1.20 # m.mho/cm**2
gkmax = 0.36 # m.mho/cm**2
gl = 0.003 # m.mho/cm**2
cm = 0.01 # mF/cm**2

m = 0.0530 
h = 0.5960 
n = 0.3177 
```

The parameters can be changed using the `change_params` function. A dict of params as keys and their corresponding values should be passed as the parameter.

### Izhikevich Neuron Model
The Izhikevich neuron model can be simulated by creating an instance of the `IzhNeuron` class.  

The code is as follows:
```python
izhneuron = IzhNeuron()

tmax = 1000
dt = 0.01
t = np.arange(0, tmax, dt)
I = 5
izhneuron.simulate(t, I)
izhneuron.plot()

current_list = np.arange(0.01, 10, 0.5)
izhneuron.animate(t, ylim=[-80,35], current_list=current_list)
izhneuron.animate(t, current_list=current_list, name="no_ylim")
```

The results obtained from the above code:
![](images/izh_1.gif)

The default parameters used in the model are:
```python
a = 0.02
b = 0.2
c = -65
d = 8

v = -65
u = b * v 
```
The above values correspond to Regular Spiking.

The parameters can be changed using the `change_params` function. A dict of params as keys and their corresponding values should be passed as the parameter.