################################# while loop promot try except ############################
'''
Write a python code that uses a while loop to prompt the user to only enter integers.

if the user presses any key in the keyboard other than the integer, then an exception will be done
'''
try:
    while True:
        number=int(input("Please enter a number: "))
except Exception as e:
    print("String is not acceptable")



