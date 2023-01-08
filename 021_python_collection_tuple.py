#################################  Tuple  ############################

'''
A collection is a single variable that is used to store multiple variables

A tuple is a 1-D collection that is surrounded by round parentheses.

The characteristic of a tuple is listed as follows:

1- It can be initiated by using double round brackets ()
2- I can hold much different data types such as str, int, etc.
3- Elements inside a list are ordered elements and accessed by index
3- It allows duplicating elements.
4- Tuples are immutable and iterateable
5-  Tuples are faster than lists
5-  Tuples are faster than lists
'''

Fruits=('cherry','banana','apple','watermelon', 'pineapple', 'coconut','banana')
print(Fruits)
print('-'*50)

'To print the attributes and methods for a tuple object'
#print(dir(Fruits))  There are not many methods  for tuples (only count and index methods)

'To show a description of each attribute and method'
#print(help(Fruits)

'Checking if an element is included in a tuple or not'
print('cherry' in Fruits)
print('-'*50)


'Retrieving  how many elements are included in a tuple'
print(len(Fruits))
print('-'*50)

'Printing the index of an element inside a tuple'
print(Fruits.index('apple'))
print('-'*50)

'Printing how many times an element is repeated in a list'
print(Fruits.count('banana'))
print('-'*50)

'As is a list, we can iterate over a tuple'
for fruit in Fruits:
    print(fruit,end=' ')
print()
print('-'*50)

'Tuple can hold heterogeneous values'
mt=("Mohanad","Gaza",13,True)
print(mt)
print('-'*50)

'Remember: The parenthesis are optional and we can leave them away'
mt="Mohanad","Gaza",13,True
print(type(mt))
print('-'*50)

'Considering one element inside the parenthesis, then you should insert "," at the end otherwise it will recognize it as a str or int'
mt=("Mohanad") # invalid tuple syntax
print(type(mt))
mt=(10)
print(type(mt))
mt=("mohanad",) # valid tuple syntax
print(type(mt))
print('-'*50)

'Printing an element based  on its index'
mt="Mohanad","Gaza",13,True
print(mt[1])
print('-'*50)

'Reverse a tuple'
print(mt[::-1])
print('-'*50)

'Remember: a tuple immutable, i.e., we can not do an assignment as follows '
#mt[0]='ID'
#print(mt)  # will return error

'Convert a tuple into a list'
mt_list=list(mt)
print(mt_list)
print('-'*50)

'Convert a list into a tuple back'
nmt=tuple(mt_list)
print(mt)
print('-'*50)

'Slicing in tuple'
t_num=10,20,30,40,50,60,70,80,90,100,120
print(f'Elements from the index # 2 to the index #5 are: {t_num[2:5]}')
print('-'*50)

'Printing every two steps'
print(t_num[::2])
print('-'*50)

'Unpacking tuples'
name, cite, age,is_marrid="Mohanad","Gaza",35,True
print(f'name is {name}, age is {age}, is_marries is {is_marrid}')
print('-'*50)

'Unpacking elements using *  '
mt="Mohanad","Gaza",35,True
print(*mt)
print('-'*50)

t_num=10,20,30,40,50,60,70,80,90,100,120
n1,*n2,n3=t_num
print(n1)
print(n2) #  list of the number between  n1,n2
print(n3)
print('-'*50)

'List vs Tuple in terms of memory location'
import sys
m_list=["Mohanad","Gaza",35,True]*2
m_tuple=("Mohanad","Gaza",35,True)*2

print(f'The total number of bytes: {sys.getsizeof(m_list)}')
print(f'The total number of bytes: {sys.getsizeof(m_tuple)}')
print('-'*50)

'Creating  a list vs tuple 100000 times'
import timeit
print(timeit.timeit(stmt="[10,20,30,40,50]",number=100000))
print(timeit.timeit(stmt="(10,20,30,40,50)",number=100000))



