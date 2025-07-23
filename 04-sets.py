#Sets:   
my_list=[1,2,3,1,2,3] 
print("original list:",my_list)
##Convert list to a set to remove duplicates:
my_list_set=set(my_list)
type(my_list)
print(my_list_set)
##Each value appears only once in a set:
my_set={"a","b","c"}
type(my_set)
##Creating empty collections:
empty_set=set()
type(empty_set)
empty_set.add(10)
print(empty_set)
empty_list=list()
type(empty_list)
empty_list.append(20)
print(empty_list)
empty_dict=dict()
type(empty_dict)
empty_dict["key"]=768
print(empty_dict)