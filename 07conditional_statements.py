#Conditional Statements:
if 3>1:
 print("True")  
else:
    print("False")
salary=int(input("Please enter your salery:"))
if salary>5000:
    new_salary=(salary*5)/100
    print("New salaray:",new_salary)
elif salary==5000:
    new_salary=(salary-100)
    print("New salary",new_salary)
else:
    print("Thankyou!")
    
brave_hero=input("Who is your hero:").strip().capitalize()
if brave_hero=="Batman":
   print("Congratulations!") 
elif brave_hero=="Superman":
   print("your character is Superman")
elif brave_hero=="Ironman":
    print("your character is Ironman")
else:
     print("who is this?")   
     
    
a=10
b=20
c=30
if a>b and b>c:
    print("a greater than b AND b is also greater than c")
elif a<b and b<c:
    print("a is less than b AND b is also less than c")
else:
    print("The conditions were not met")    
#for booelean  
vivid_character=True
if vivid_character:
    print("your character is live ")
else :
    print("your character isn't live")
     

string="Nurhayat Cengiz"
if string=="Nurhayat Cengiz":
    print("same")
else:
    print("isn't same")
    
if "nurhayat" in string:
    print("True")
else:
    print("False")
    
if "nat"in string:
    print("True")
else:
    print("False")
    
list=[10,30,"w"]
if 10 in list:
    print("yes")
else:
    print("no")
    
dict={"banana":145,"apple":356,"oraange":457}
if "banana" in dict.keys():
    print("True")
else:
    print("False")
    
if 956 in dict.values():
    print("True")
else:
    print("False")
    

