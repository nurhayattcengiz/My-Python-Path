import numpy as np
my_nparray= np.arange(30)
print(my_nparray)

my_randomarray=np.random.randint(0,100,20)   
print(my_randomarray)

#Numpy Array Methods:
my_nparray.reshape(5,6)#The array contains 30 elements, so the shape must match accordingly
my_nparray.max()
my_nparray.min()

my_randomarray.max()
my_randomarray.min()

my_randomarray.argmax()
my_randomarray.argmin()

reshape_array=my_nparray.reshape(5,6)
reshape_array
reshape_array.shape




