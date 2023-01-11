################################# Shopping cart exercise  ############################

'''
By using python collection, write a shopping cart program for supermarket.

The user must enter the food, and if he presses q or Q  the program will quit.
The user/ or operator is also able to set the price of the entered food.
At the end of the program, print the list of items and the total price.

Because we want to print the items and we need the order of the items, we will use a list.
we can not use a tuple because we could not append in the tuple, and we can not a set because it will not order the items
'''

foods=[]
prices=[]
total=0

while True:
    usr_input=input("Enter the food please (q to quit): ").lower()
    if usr_input=='q':
        break
    else:
        foods.append(usr_input)
        price=float(input("Enter the price of the selected food: "))
        prices.append(price)


'Let us decorate the output'
print('')
print('#'*50)
print('-'*17,'shopping cart','-'*17)

print(f'The shopping cart contains: ', end='') # this will be print also the following food at the same line
for food in foods:
    print(food,end=' ')
print('')

for price in prices:
    total+=price
print(f'The total price is: {total}')
print('#'*50)





