################################# If break inside for loop ############################
''' suppose you have a list of monthly expenses as follows
Expenses=[1200,500,20,40,1600,500,700,4,20]
and corresponding months are
Months = ["January", "February", "March", "April", "May","June","July","August"]

Write a python code that  ask you to insert the expenses from  the list
and it will returns with month this expense is associated with.
'''

Expenses=[1200,500,20,40,1600,500,700,4,30]
Months = ["January", "February", "March", "April", "May","June","July","August","September"]

'Logically remember that the expenses are > 0,  thus we can use the negative values for any index'

Expense_input=int(input("Enter your expense Please: "))

for idx,val in enumerate(Expenses):
    if Expense_input==Expenses[idx]:
        print(f" You spent  {Expense_input} in {Months[idx]}")
        break

#### Another solution using negative value index

holder=-1
for i in range(len(Expenses)):
    if Expense_input==Expenses[i]:
        holder=i
        break
if holder !=-1:
    print(f"You spent {Expense_input} in {Months[holder]}")
else:
    print(f"You did not spend {Expense_input} during the listed months")
