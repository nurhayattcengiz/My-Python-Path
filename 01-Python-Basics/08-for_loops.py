#For loops:
#pratice with for loops on various data types:
my_list=[10,20,30,40,50]
if 30 in my_list:
    print("yes")
else:
    print("no")

for numbers in my_list:
    print(numbers)
    
for num in my_list:
    new_number=num*3
    print(new_number)
 

new_list=[1,2,3,4,5,6]
for number in new_list:
    if number%2==0:
        print(number)

new_str="NURHAYAT CENGİZ" 
for vowel in new_str:
    print(vowel)
    
my_tuple=(1,2,3,4,5,6)
for number in my_tuple:
    print(number*2)
     
coordinat_list=[(10.2,15.2),(32.4,16.2),(40.2,20.2)]
type(coordinat_list)
type(coordinat_list[2])
print(coordinat_list[2])
for num in coordinat_list:
    print(num[1])
    
for (x,y) in coordinat_list:
#unpack each tuple and print both values
    print(x,y)

for (x,y) in coordinat_list:
    print(y)
#print only the second value
    
my_list=[(1,2,3),(3,4,5),(7,8,9)]
for (a,b,c) in my_list:
    print(a,c)
#print the first and third values from each tuple

my_dict={"banana":123,"apple":245,"orange":567}
my_dict.items()
for (keys,values) in my_dict.items():
    print(keys)
#print only the keys
