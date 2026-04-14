# prints “Even” if the variable integer is and even number, and “Odd” otherwise
integer = int(input("Enter a integer value: "))
remainder = integer % 2
if remainder == 0 : 
    print("even")
else : 
    print("odd")