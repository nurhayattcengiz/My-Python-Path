#Numpy Indexing:
import numpy as np
my_array=np.arange(0,15)
print(my_array)
my_array[5]#output:5

my_array[3:5]#output:([3,4])

my_array[3:8]=-5
my_array

new_array=np.arange(0,24)
new_array

slicing_array=new_array[4:9]
# Slicing from index 4 to 8 (inclusive start, exclusive end)
slicing_array
#output:([4,5,6,7,8])
slicing_array[:]
##output:([4,5,6,7,8])
slicing_array[:]=700
# Assigning value 700 to all elements in the sliced array
slicing_array#output:([700,700,700,700,700])
# Bir dilimin değiştirilmesinin orijinal diziyi nasıl etkilediğini gösterir
print(new_array)
#Output: updated values at index 4 to 8

