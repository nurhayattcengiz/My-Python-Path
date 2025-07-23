#Inheritance:
class animal():
    def __init__(self):
        print("animal class")
    def method1(self):
         print("method1")
    def method2(self):
         print("method2")
my_animal=animal()
my_animal.method1()
my_animal.method2()       

class cat(animal):
    def __init__(self):
        animal. __init__(self)
        print("cat class")      
#override:
    def method1(self):
        print("animal is a cat")
other_animal=cat()    
my_cat=cat()
my_cat.method1()
my_cat.method2()

#polymorphisim:
class apple():
    def __init__(self, name):
        self.name = name

    def information(self):
        return self.name + " 100 calori"

class banana():
    def __init__(self, name):
        self.name = name

    def information(self):
        return self.name + " 150 calori"

new_banana = banana("banana")
print(new_banana.information())
new_apple = apple("apple")
print(new_apple.information())
fruit_list=[new_banana,new_apple]
for fruit in fruit_list:
    print(fruit.information())
    

def new_information(fruit):
    print(fruit.information())
new_information(new_banana)





   
        

        
        
         

