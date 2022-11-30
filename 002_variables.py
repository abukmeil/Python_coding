'''Variable: a container that holds/ stores value/ values. It behaves according to the format of the
contained value, i.e., string. integer, logic, etc.'''

# Numerical variables
age = 35
print()
'Here is a mistake because we print a word "age" not variable'
print("age")

'We use th following format to print the variable age, not "age" must be int'
'"str(int)" is called type casting'
print("You are "+str(age)+" years old")

'Another way to print int with str  by separating variables into two sets arguments using ","'
print("You are",age,"Years old")


'The most common method to print variables with text is called f-string'
'{ } is called place holder in print'
print(f"You are {age} years old")
print()
############################ Basic data typs in python ###################

# INTEGER
quantity = 100
users = 20
age = 35
print(f"The total number of items is {quantity}")
print(f"There are {users} users")
print(f"You are {age}years old")

print()
# FLOAT
distance = 5.6
price = 100.50
temperature = 30.2
print(f" The total distance is {distance}")
print(f"The total is {price}")
print(f"Today is hot, it is {temperature} degrees")
print()
# Strings
'It  is a series of text'
name = "Mohanad"
food = "Pasta"
address = "Gaza"
print(f"My name is {name} and I like {food} and I live in {address}")

print()
# BOOLEAN
'Either "Ture" or "Fales" , i.e. a binary with only two states'

active=True
sale=False
play=True
print(f"Are you active? :{active}")
print(f"Is there any sale today?: {sale}")
print(f"Can you ply cardio?: {play}")

if active:
    print("Active now")
else:
    print("offline")

'Do not put True/ False inside the quotes " ", it will turn to the string'

# Multiple assignment of variables
print()
x=10
y=20
z=30
print(x)
print(y)
print(z)
print()
'Alternatively we use the multiple assignments'
x,y,z=10,20,30
print(x)
print(y)
print(z)

print()
x=y=z=0
print(x)
print(y)
print(z)



