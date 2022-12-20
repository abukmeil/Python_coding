################################# String methods  ############################
'''
A string is a series of characters

The  comprehensive list of string methods can be obtained by "help(str)"

'''
print(help(str))


'Asking the user to enter his full name'
name=input("Please enter your name: ")

'len method returns the length of a string'
result=len(name)
print( f" The length is {result}")
print('')

'find method returns the first occurrence of a given character'
result=name.find(" ") # find where  the first space
print(f"The first occurrence {result}")
print('')
result=name.find("m")
print(f"The first occurrence {result}")
print('')

'rfind method returns the last occurrence of a character'
result=name.rfind("k")
print(f"The last occurrence {result}")
print('')

'capitalize method makes the first letter capital'
result=name.capitalize()
print(f"The first letter capitalization: {result}")
print('')

'upper method  converts the whole string to capital letters'
result=name.upper()
print(f"The capitalized string is: {result}")
print('')

'lower method turns string to small letters'
result=name.lower()
print(f"The small letter version is: {result}")
print('')

'isdigit returns the boolean result of a string containing digits'
result=name.isdigit()
print(f" The string contains digits? {result}")
print('')

'isalpha method returns a boolean result if the string contains only alphabetical characters '
result=name.isalpha()
print(f" The string contains only alphabetical chars: {result}")

print('************************')

mobile_num=input("Enter the mobile number please: ")
result=mobile_num.count("-")
print(f" The mobile number contains {result} of the -")
print('')

'replace method replaces one value by another'
result=mobile_num.replace("-"," ")
print(f"The refind mobile number is: {result}")
print('')

'- can be eliminated from the above example'
result=mobile_num.replace("-","")
print(f"The refind mobile number is: {result}")
print('')





