################################# User input ############################


'To accept any user input we use the "input(HERE WE CAN TYPE OUR PROMPT)" function'

input("Enter your name: ")
' let us  assigning it, i.e, input to a variable'
name=input("Enter your name: ")
'We can print our name within a message as follows'
print(f"Hello {name}")
print()

'let us create a variable age'
age=input("Enter your age please: ")
print(f"Your age is {age} years old ")

'Let us increase the age variable by one'
#age=age+1
#print(f"Your age is {age} years old ")
' Note the above line will return an error because we need to  cast age as int'
age=int(age)
age=age+1
print(f"Your age is {age} years old ")

# Casting at input time
'If you want to string the default input function return string'
'If you want to accept numeric values, you can cast input directly as follows'
age=int(input("Enter your age please: "))
weight=float(input("Enter your weight please: "))



