################################# If continue inside for loop ############################
''' suppose you are given a range of numbers (1,20) and you want to
only need the square of odd numbers. Write a python code that takes a range of number and
print only the square of odd numbers
'''

for i in range(21):
    if i %2==0:
        continue
    else:
        print(f" The square of {i} is {i*i}")

