################################# String indexing exercise  ############################

'Write a python program that asks the user to insert his/ her email and return the username and the domain'

email=input("Enter your email please: ")

index= email.index("@")

print(f"Your username is {email[:index]} and the hosting domain is {email[index+1:]}")
