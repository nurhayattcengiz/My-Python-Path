#Try & Expect:
def addition( x,y):
        return x+y
x=int(input("Please write the first number: "))
y=int(input("Please write the second number: "))
result=addition(x,y)
print(f"new result: {result}")

#try & except & else & finally:
while True:
    try:
        my_int=int(input("please write the num:"))
    except:
     print("please write real num") 
     continue
    else:
     print("Thanks")
     break
    finally:
        print("finally block has been executed")
        
 
        
    
    


