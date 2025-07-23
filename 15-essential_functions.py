#Essential Functions:
def divide_numbers(number):
    return number/2
divide_numbers(20)

my_list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for num in my_list:
    new_list.append(divide_numbers(num))
new_list

#map:
def to_square(x):
    return x*x
numbers=[1,2,3,4,5]
result=map(to_square,numbers)
print(list(result))

def control_function (name):
    return "o" in name
name=["aynur","levent","ayşe","oğuz","orkun"]
#list(map(control_function,name))  

result_list=list(map(control_function,name)) 
result_list.count(False)

#filter:
def ctrl_function(word) :
    return "a" in word
word=["mehmet","ayşe","fatma"]
list(filter(ctrl_function,word))
 
#lambda:
# Using lambda to create an anonymous function
# Define inline logic for small operations using lambda
def square(num):
    return num*num
square(5)

#with lambda:
square=lambda number: number*number
print(square(7))