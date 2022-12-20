################################# While loop  ############################

''' Uisng while loop allows us to execute some
codes, while some conditions remain, are True'''


job=input("Enter your job please: ") # Remeber this is called prompt

if job =="":
    print("Enter your job to proceed")
else:
    print(f"Your job is {job}")

'''The above code executes once even if you typed/don't type your name
What if we want to continue to prompt the  user to enter his job, we need to replace
if statement with While 
'''
'''
while job=="":
    print("Enter your job to proceed: ")
else:
    print(f"Your job is {job}")
'''
''''The above code will go to an infinite loop, thus we want to terminate and limit
the while loop, that is by doing something directly when the condition does not achieve'''

'''
while job =="":
    print("Enter your job to proceed: ")
    job=input("Enter your job: ")
else:
    print(f"Your job is {job}")
'''
# Age example
age=int(input("Enter your age: "))

while age <0:
    print(f"Your age can  not be negative: ")
    age=int(input("Enter your age again: "))
else:
    print(f"Your age is {age}")


# Sport example

'Introducing some logical operator '
sport=input("Enter your preferred sport (Press q to quit): ")

while not sport =="q":
    print(f"You prefer {sport}")
    sport=input("Enter another sport preference: (q to quit): ")
else:
    print("Ciao")


'Using Or log  operator'
'Example: Ask the user to type  a number between 0:10'

number=int(input("Enter number between 1 to 10: "))

while number <1 or number >10:
    print(f"The {number} is not valid")
    number=int(input("Enter number between 1 to 10: "))
else:
    print(f"Your number is {number} and it is a valid number")