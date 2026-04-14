# input 5 information for annotating 
label = input("Enter the label: ")
x_min = float(input("Enter the x_min: "))
y_min = float(input("Enter the y_min: "))
x_max = float(input("Enter the x_max: "))
y_max = float(input("Enter the y_max: "))

# validating dataset
if x_min < 0 or y_min < 0 or x_max  < 0 or y_max < 0 : 
    print("Invalid: negative")
elif x_min >= x_max or y_min >= y_max :
    print("Invalid: order")
else : print("Valid")