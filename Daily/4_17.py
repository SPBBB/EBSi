# functio
"""
3
5
5
print('efr')
577757575
# return None == void ? 

def greet(name, message="Hello!") : 
    print(f"{name}, {message}") 
    return None 

greet("Alice")
greet(369,"Hi!")

a = greet(435)
print(a)

def greet1(name, message="Hello!") : 
    print(f"{name}, {message}") 

b = greet1(324)
print(b) # no comment about return equals to setting return None

# default vaules & 명시!!! 
greet(name="Alphs")
greet("Kim",message=1234) # type of default value and arg is not neccessary to be equal.  

def greet2(name, game, message="Hello!") : 
    print(f"{name}, {game}, {message}") 
    return None 

greet2("kim",message="higg",game="retr")
"""
# arg 개수 유동적이게 하기 *args < tuple
def add_numbers(*args) :
    print(args)
    added = 0 
    for i in args : 
        added += i
    return added

x = add_numbers(3)
y = add_numbers(5,6,2)
z = add_numbers(10,3,3,3,3)
print(x,y,z)

# **kwargs < dictinonary
## 용어 : fruitful < a funtinon is fruitful if it has a return that is not None (?)
# modify global variable in function : set the variable with the keyword type 'global' ""
"""function
reusablity
readabiity
maintainablity
abstraction 
. . . 
one func. to one well-defined work .
"""

# lab 1. Function 
