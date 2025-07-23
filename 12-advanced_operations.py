#zip:
fruit_list=["apple","banana","orange"]   
calorie_list=[100,200,300]
daily_list=["monday","tuesday","wednesday"]
do_zip=list(zip(fruit_list,calorie_list,daily_list))
for new in do_zip:
    print(f"Data type: {type(new)},Content:{new}")
    
#Advanced list operations:
list=[]
my_str="nurhayat cengiz"
for vowel in my_str:
    list.append(vowel)
    print(vowel)
    
new_list=[number*5 for number in list(range(0,10))]
print(new_list)
          
    