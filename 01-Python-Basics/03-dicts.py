#Dicts:
#key-value pairing:
fruits=["apple","watermerlon","banana"]
calorie=[100,200,300]
first={"Key":"Value"}
print(type(first))
fruits_calorie={"apple":100,"watermelon":200,"banana":300}
print(fruits_calorie["apple"])
print(fruits_calorie["banana"])
#I can update the value:
fruits_calorie["apple"]=450
print(fruits_calorie["apple"])
fruits_calorie.keys() 
#It returns only the keys.
print(fruits_calorie.keys())
fruits_calorie.values()
#It gives back just the values.
print(fruits_calorie.values())
new_dict={"key1":100,"key2":[10,20,30,40,4.5,"ali"],"key3":{"key9":4}}
print(new_dict["key2"][5])
print(new_dict["key3"]["key9"])
 