#While loops:
x=0
while x<10:
    print(x)
    x=x+1
    
my_list=[1,2,3,4,5]
while 3 in my_list:
    print("OK")
    my_list.pop()
    
number=0
while number <5:
    if number==4:
        break
    print(number)
    number=number+1
    
new_num=0
while new_num<15:
#method1:
    #print("nem_value",new_num)
#method2:
    print(f"new_value:{new_num}")
    new_num=new_num+1
#Method 1: Using comma (easier to write)
#Method 2: Using f-string (more flexible)

    

