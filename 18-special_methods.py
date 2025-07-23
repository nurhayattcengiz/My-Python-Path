#Special methods:
#__init__:
class fruit():
#The __init__ method is a constructor that runs when the object is created.
#It assigns the values provided by the user to the object's attributes.

    def __init__(self,name,calorie):
        self.name=name
        self.calorie=calorie
        
#The __str__ method defines what the object will look like when printed.
# It is used to produce a human-readable output.
         
    def __str__ (self) :
         return f"{self.name} calorie is: {self.calorie}"

# The __len__ method specifies the value returned when len(object) is called.
# Here, it is used to represent the calorie count.

    def __len__(self):
        return self.calorie
 
# The __eq__ method determines whether two objects are equal.
# It returns True if their calorie values are the same.
    
    def __eq__(self, other):
       return self.calorie == other.calorie
   
banana= fruit("Banana",150)  
print(banana)
len(banana)
apple=fruit("Apple",200) 
len(apple)
banana==apple
    
         