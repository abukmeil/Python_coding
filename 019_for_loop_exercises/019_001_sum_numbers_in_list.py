################################# Sum numbers in a list ############################
'''Suppose you have a list of expenses for any month,
 write a python code that sum all expenses together using for loop'''

Expenses=[1200,500,20,40,1600,500,700,4,20]

'It is better to initiate our placeholder for the sum with 0'
total=0
for i in Expenses:
    total+=i

print('')
print(f" Your total total sum of expenses in this month: {total}")