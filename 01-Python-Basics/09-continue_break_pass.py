#Continue break pass:
# This script demonstrates break, continue, and pass usage in Python loops.
#BREAK:
my_list=[5,10,15,20,25,30]
for number in my_list:
    if number==15:
        break
    print(number)
#As soon as number equals 15, the loop breaks. The number 15 and all values after it are not printed.
#CONTINUE
for number in my_list:
    if number ==15:
        continue
    print(number)
#When number is 15, continue skips the print() and resumes with the next item in the list
#PASS
for number in my_list:
    pass
#pass is a placeholder that does nothing. It's often used when you need a syntactically valid block but don't want to write any code yet.


