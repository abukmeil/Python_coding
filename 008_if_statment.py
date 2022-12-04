################################# If statement ############################
''' If statement is used to do some code only if a condition/ some condition is True,

else we do something '''

'if----else'
age=int(input("Enter your age: "))
if age >=33:
    print('You are active')
else:
    print("You must be 30+ to be activated")

print('***********************************')

'if----elif----else'
age=int(input("Enter your age: "))

if age <0:
    print("Enter valid age")
elif age>= 100:
    print("You are too old to signin")
elif age >=33:
    print('You are active')
else:
    print("You must be 30+ to be activated")

# Example food

respnse=input("Would you like food? (Y/N): ")

if respnse=="Y":
    print("Have some food!")
else:
    print("No food for you")

# Example name
name=input("Enter your name: ")
if name =="":
    print("You did not entered your  name")
else:
    print(f"Hello {name}")

# Example Boolean with if
for_sale=True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

print('**************************************')
online=False
if online:
    print("You are online")
else:
    print("You are offline")