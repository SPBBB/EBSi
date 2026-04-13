# input a class name and make the caracters lower. 
class_name = input("Enter a class name (cat/dog/bird): ")
class_name = class_name.lower()

# assign a label by class name.
if class_name == "cat" :
    label = 0 
elif class_name =="dog" :
    label = 1
elif class_name =="bird" : 
    label = 2
else : label = 3
print(label)