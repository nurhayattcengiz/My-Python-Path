#random:
import numpy as np
# Imports the NumPy library for numerical operations

np.random.randn(4)
# Generates a 1D array of 4 random numbers from a standard normal distribution
np.random.randn(3,3)
# Generates a 2D array (3x3) of random numbers from a standard normal distribution

np.random.randint(1,10)
# Generates a random integer between 1 (inclusive) and 10 (exclusive); returns one of [1, 2, ..., 9]

np.ramdom.randint(1,10,5)
# Generates an array of 5 random integers between 1 (inclusive) and 10 (exclusive)

my_nparray=np.arange(30)
print(my_nparray)

my_randomarray=np.random.randint(0,100,20)
print(my_randomarray)

