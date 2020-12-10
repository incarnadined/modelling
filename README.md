# modelling
A repo for all sorts of modelling stuff

## Particle Simulation
### `basic_particle_simulator.py` 
Unsurprisingly a pretty basic particle simulator that takes an initial velocity (ms^-1) and an intial angle (radians) and plots a graph to simulate the flight of the particle.

### `Lucy.py`
A ~~slightly~~ _significantly_ more complicated particle simulator that works in n dimensions.

## Random Numbers
### `random_number.py`
Some code that plots the length of a list of random numbers on the x-axis against the arithmetic mean of that length list on the y-axis. Unsurprisingly tends to 0.5 (with a range of 0-1).
![Graph](images/random_number_convergance.png?raw=true)

### `calculating_pi.py`
This one has a fun name to say... (although should say approximating)
This code uses the [Monte Carlo method](https://arxiv.org/ftp/arxiv/papers/1909/1909.13212.pdf) to approximate π, by calculating the ratio of points that fall in a circle compared to the number of points in the square that inscribes the circle. The graph plotted shows the real value of π according to numpy, along with an approximation using numpy random numbers as well as latin hypercube random numbers (explained at bottom)
![Graph](images/monte_carlo_pi_approximation.png?raw=true)

## Helper Functions
### `latin_hypercubes.py`
A small module that contains a function (unimaginativley named `latin_hypercubes`) that returns an array of random floats within a specified range, a specified number of values. The function uses [Latin Hypercube Sampling](https://en.wikipedia.org/wiki/Latin_hypercube_sampling) to generate the random array which in essence is just making a nice regular array and then shuffling it up a bit.
