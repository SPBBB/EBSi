# it's same as 18.py but it can handle the input type error.
try : 
    integer = int(input("Enter a integer value: "))
    remainder = integer % 2
    if remainder == 0 : 
        print("even")
    else : 
        print("odd")

except:
    print("Input is not a integer!")