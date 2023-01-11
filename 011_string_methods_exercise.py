################################# String methods exercise  ############################
'''
The following exercise is about validating the user input, i.e, user input verification

The rules are as follows:

1. username is no more than 12 characters.
2- username must not contain spaces.
3. username must not contain digits.
'''

Username=input("Enter your name please: ")

if len(Username) >12:
    print(" your username can't be more than 12 character")
    print(Username.find(" ")==1)


elif not Username.find(" ")==-1:
    print("your username can't contain spaces")
    print(not Username.find(" ")==-1)

elif Username.isalpha()==False:
    print("Your username can't contain digits")
else:
    print(f"Welcome {Username} ")





