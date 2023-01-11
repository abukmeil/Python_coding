################################# 2d_collection ############################

'''
A collection is a single variable that is used to store multiple variables

2-D collection  refers to two-dimensional list (list of lists), tuple (tuple of tuples), list of tuples, and even a list of dictionaries
Note: we will cover "Python dictionary later" them later.

- The following is a description related to a 2-d list, and what is applied to the 2-d list is applicable to the others.
'''

'2-d list is a list of lists'
list_2d=[[],[]]
print(type(list_2d))
print('-'*50)

'Let us create two 1-d lists, one for food and the other for beverage'
foods       =      ['pasta','pizza','fish','upside-down']
beverages   =  ['coca-cola','pepsi','sprite','fanta']

'We can print 1-d list'
print(foods)
print('-'*50)

'We can modify the elements by modifying their indices'
foods[-1]='kebab'
print(foods)
print('-'*50)


'To create two lists, we have to open double [], or simply open [] in insert inside i-d list'
restaurant=[foods,beverages]
print(restaurant)
print(restaurant[0][0])
print('-'*50)

'Accessing the 2-D list by an index is different than 1-D list'
print(restaurant[0])  # in 1-D list it prints the first element, but in 2d- lit it prints the list of list
print('-'*50)

'To print a specific element in 2-d list, we need two indices (looks like coordinates) for rows and columns'
print(restaurant[0][1])
print('-'*50)

# Remember it is not necessary to have the same length of lists in a 2-d list

'We can iterate over a 2-d list to print its contained lists'
for list in restaurant:
    print(list)
print('-'*50)

'To iterate over a 2-d list to print elements inside each 1-d list, we use nested loop'
for list in restaurant:
    for element in list:
        print(f'{element}',end=' ')
    print('')

print('')
print('-'*50)

'We can follow the same intuition of we have a list of tuples'
foods       =      ('pasta','pizza','fish','upside-down')
beverages   =      ('coca-cola','pepsi','sprite','fanta')
restaurant=[foods,beverages]
print(restaurant)
print('-'*50)

'To iterate over a 2-d list of tuples to print elements inside each 1-d list, we use nested loop'
for list in restaurant:
    for element in list:
        print(f'{element}',end=' ')
    print('')

print('')
print('-'*50)

'We can follow the same intuition of we have a tuple of tuples'
foods       =      ('pasta','pizza','fish','upside-down')
beverages   =      ('coca-cola','pepsi','sprite','fanta')
restaurant=(foods,beverages)
print(restaurant)
print('-'*50)

'To iterate over a 2-d list of tuples to print elements inside each 1-d list, we use nested loop'
for list in restaurant:
    for element in list:
        print(f'{element}',end=' ')
    print('')

print('')
print('-'*50)


'We can follow the same intuition of we have a list of sets'
foods       =      {'pasta','pizza','fish','upside-down'}
beverages   =      {'coca-cola','pepsi','sprite','fanta'}
restaurant=[foods,beverages]
print(restaurant)
print('-'*50)

'To iterate over a 2-d list of tuples to print elements inside each 1-d list, we use nested loop'
for list in restaurant:
    for element in list:
        print(f'{element}',end=' ')
    print('')

print('')
print('-'*50)
