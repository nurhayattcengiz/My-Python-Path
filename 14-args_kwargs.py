#args & kwargs:
#args:
def new_total(*args):
    return sum(args)
new_total(10,20,80,90)

def my_function(*args):
    print(args)
type(my_function(10,20,30))
#Because I didn't use return, the data type becomes NoneType

def my_functions (*args):
   return args
type(my_functions(20,30,40))
#I use return so the data type is a tuple
 
#kwargs:
def fruit_function(**kwargs):
    return kwargs
fruit_function(banana=100,apple=200,orange=340)

    
def key_control (**kwargs):
    if 70 in kwargs:
        print("True")
    else:
        print("False")
key_control(ahmet=45,mehmet=90,tom=43)
