import numpy as np
#Matrix:
#matrix[row,column]
my_list=[[10,20,30],[20,30,40],[40,50,60]]
matrix_array=np.array(my_list)
print(matrix_array)

matrix_array[2,1]
#matrix_array[2][1]

matrix_array[0:,2]#output:([30,40,60])

new_list=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
new_matrix=np.array(new_list)
print(new_matrix)
#fancy indexing:
new_matrix[[4,2,0]]


#Operations:
new_array=np.random.randint(1,100,20)  
print(new_array) 

new_array>24 

result_array=new_array>24
result_array

print(new_array)
new_array[result_array]

my_array=np.arange(0,24)
print(my_array)

my_array+my_array
#Adds two arrays element-wise
#Performs addition, subtraction, multiplication, and division

