#Numpy:
    
import numpy as np
#Numpy Array:
    
my_list=[20,30,40]   
np.array (my_list)

matrix_list=[[10,20,30],[20,30,40],[30,40,50]]
np.array(matrix_list)

#Numpy Methods:
#ARANGE:
list(range(0,10))  
#for np:
np.arange(0,10) #output:Converts a Python list into a NumPy array
np.arange(0,10,2)#Creates an array of values from 0 to 10 with step size of 2

#ZEROS:
np.zeros(5) 
np.zeros((2,2)) #Initializes a 2x2 array filled with zeros

#ONES:
np.ones((5,5))#Generates a 3x3 array filled with ones

#LİNSPACE:
# np.linspace(start, stop, num) → Returns 'num' evenly spaced samples from start to stop
#Returns a NumPy array with evenly spaced values, including the end value. Commonly used in plotting and simulations.
np.linspace(0,20,6)  

#EYE:
np.eye(5) # Creates an identity matrix of size n x n (diagonal elements are 1, others are 0)

  



    
    


