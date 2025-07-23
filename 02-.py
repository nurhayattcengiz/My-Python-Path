#Lists:
lists=[10,20,30,"a"]
print(type(lists))
print(lists[3])
lists[2]=100
print(lists)
#Metods:
lists.append(50)
print(lists)
lists.pop()#Delete the last item
print(lists)
lists.remove(20)#Removes the specified value
print(lists)
#If you try to remove something that doesn't exist, you'll get an error."
lists=[10,10,30,78,43]
print(lists.count(10))

benimStringListem=["ayşe","banu","merve"]
benimDigerListem=["ali","fatih","can"]
toplamListem=benimStringListem + benimDigerListem
print(toplamListem)
benimStringListem.reverse()#sıralamayı sondan başa yapar
print(benimStringListem)

#nestedList:
new=[1,5,"ali",4,[6,"e"]]
print(new[2])
print(new[4])
new_value=new[4][1]
print(new_value)