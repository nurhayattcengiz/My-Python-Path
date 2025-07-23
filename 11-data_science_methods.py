#Data science methods:
#range:
list(range(15))
#loop from 0 to 15(15 not include)
for num in list (range(15)):
    print(num*2)

#loop from 0 to 4
for i in range(5):
    print(i)
    
#loop from 2 to 6 (6 not include)
for i in range(2,6):
    print(i)
    
#loop from 0 to 10 with step size of 2
for i in range(0,10,2):
    print(i)

#enumerate:
#loop through the list with index and value
my_list=["apple","banana","cherry"] 
for i,value in enumerate(my_list):
    print(f"index{i}: {value}")
    
#random:
from random import randint
randint(0,100)

my_list=list(range(0,10))
print(my_list)
my_list[randint(0,9)]
#print a random item from the list

from random import shuffle
shuffle(my_list)
print(my_list)

    
    
    
    

