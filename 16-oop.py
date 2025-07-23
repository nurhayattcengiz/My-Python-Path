#OOP:
my_list=list()
type(my_list)

#Instance & Attribute:
character_name="Superman"
character_age=30
character_job="journalist"

character_name2="Batman"
character_age2=43
character_job2="teacher"

#Class:
class Super_character():
     def __init__(self,name,age,job):
         print("Congratulations")
         self.name=name
         self.age=age
         self.job=job     
Superman=Super_character("Ironman",30,"lawyer")
Superman.name="Clark Kent"
Superman.name
  
#Default:
class dog():
    def __init__(self,age=5):
        self.age=age
my_dog=dog(8)
my_dog.age
#If no value is passed, 5 will be used as the default parameter.

class new_dog():
    years=7
    def __init__(self,age):
        self.age=age
    def human_age(self):
        return self.age*self.years
my_dog=new_dog(4)
#my_dog.age
my_dog.human_age()  
        

        
         
    
    