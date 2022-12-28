#################################  List ############################

'''
A list is 1-D collection that can store or hold different data types. The characteristic of as list:

1- It can be initiated by using double square brackets as follows []
2- I can hold much different data types such as str, int, etc.
3- elements inside a list are ordered  element and accessed by index
3- it allows duplicating elements.
4- lists are mutable and iterateable
'''

'Creating a variable'
Fruits=""
print(Fruits)

'We can turn this variable into a list using square brackets'
Fruits=[]
print(Fruits)

'the above line initiating an empty list and that is similar to the following'
Fruits=list()

'Creating a list of fruits'
Fruits=["apple","banana","pineapple","cherry"]
print(Fruits)
print('-'*50)

'Remember: as a string, we can use the index in a string'
'To access any element inside a list, we use the index operator, in the following, we print the first element'
print(f"The first element: {Fruits[0]}")
print('-'*50)

'Using an index operator we can do slicing by specifying the beginning and ending indices'
print(f"The first two element: {Fruits[0:2]}")
print('-'*50)

'What if we want to print every second element in a list, not the first one is included, i.e. index=0?'
print(f"Every second element: {Fruits[::2]}")
print('-'*50)

'What if we want to reverse our list, i.e., list backward'
print(f"The reveres list: {Fruits[::-1]}")
print('-'*50)

'We can iterate through list collection'
for fruit in Fruits:
    print(fruit, end=' ')
print('-'*50)

'To show what is the method that can be used to perform the operation in a list we use dir (list)'
#print(dir(list))
'If you need more description about each method, you can use the help method'
#print(help(list))

'Let us discover some of these methods as follows'
'To find how many elements in the list collection, we can use the method length'
print(f"The total number of elements: {len(Fruits)}")
print('-'*50)

'We can formalize a pythonic question to check if an element is in a list collection or not'
print(f"Is apple in the list: {'apple' in Fruits}")
print(f"Is mango in the list: {'mango' in Fruits}")
print('-'*50)

'Elements in a list are ordered and changeable'
Fruits=["apple","banana","pineapple","cherry"]
Fruits[0]='mango'
print(Fruits)
print('-'*50)

'We can append a new element to the end of a list'
Fruits.append("coconut")
print(Fruits)
print('-'*50)

'How can we drop the last element from a list?'
Fruits.pop()
print(Fruits)
print('-'*50)

'How can we remove a specific element from a list?'
Fruits.remove('banana')
print(Fruits)
print('-'*50)

'By using the insert method, we can add an element with a specific location'
Fruits.insert(3,'kiwi')
print(Fruits)
print('-'*50)

'We use the sort method to sort elements of a list collection based on alphabetical order'
Fruits.sort()
print(Fruits)
print('-'*50)

'Based on the places where the elements are placed, the reverse method is working'
Fruits=["apple","banana","pineapple","cherry"]
Fruits.reverse()
print(Fruits)
print('-'*50)
'What if we want a reversed alphabetical order, we do sorting then reversing trick'
Fruits=["apple","banana","pineapple","cherry"]
Fruits.sort()
Fruits.reverse()
print(Fruits)
print('-'*50)

'We can also sort numbers'
num_list=[-5,2,3,5,4,-8,0,2]
print(num_list)
num_list.sort()
print(num_list)
print('-'*50)

''''Remember and remember sort method and another method are done inplace of a list
Thus if you want the original list to remain without change then we need to have
another list with original values.'''

'Sometimes we need to keep our original list without sorting'
num_list=[-5,2,3,5,4,-8,0,2]
print(num_list)
num_list_sorted=sorted(num_list) # note: we can not use "num_list_sorted=sort(num_list)", sort is used as "num_list.sort"
print(num_list_sorted)
print(num_list)

'We use the index method to return the index of an element'
Fruits=["apple","banana","pineapple","cherry"]
print(Fruits.index('cherry'))
print('-'*50)

'What if we infer an element that is not in a list, then an error will return'
#print(Fruits.index('orange'))
print('-'*50)

'Since the duplicate are allowed in a list, then we can use the count method'
Fruits=["apple","banana","pineapple","cherry","cherry","cherry"]
print(Fruits.count('cherry'))
print('-'*50)

'We can use a clear method  to clear all elements in a list'
Fruits.clear()
print(Fruits)
print('-'*50)

#
'Remember a list can contain heterogeneous elements'
Hetro_list=["apple",1,True, 'apple',123]
print(Hetro_list)
print('-'*50)

'Check if an item in a list by using the following syntax'
if 1 in Hetro_list:
    print('Yes')
else:
    print('No')
print('-'*50)

'Creating a new list with an element that is repeated many times'
z_list=[0]*10
print(z_list)
print('-'*50)

'Concatenating two lists  list'
zero_list=[0]*10
one_list=[1]*5
zero_one_list= zero_list+one_list
print(zero_one_list)
print('-'*50)

'Extending list by another list'
zero_list=[0]*10
one_list=[1]*5
zero_list.extend(one_list)
print(zero_list)
print('-'*50)


'List slicing, we use the list operator[start:end]. If you do not specify the start then it will consider 0, and the same for end '
num_list=[10,20,30,40,50,60,70,80]
sub_num_list=num_list[2:5]
print(sub_num_list)
print('-'*50)

'In slicing, we can use step index also [::1], by default, it is 1'
num_list=[10,20,30,40,50,60,70,80]
print(num_list[::1])  # We can start at the forth element (third index) [1::1]

'What if we want every second item?'
print(f"Every second element starting from index 0: {num_list[::2]}") # start from  index 0
print(f" Every second element starting from index 1: {num_list[1::2]}") # starts form index 1
print('-'*50)

'Again two methods to reverse a list'
num_list=[10,20,30,40,50,60,70,80]
print(num_list[::-1]) #1
num_list.reverse() #2
print(num_list)
print('-'*50)


'Copying a list: (1) we can copy by assignment'
num_list=[10,20,30,40,50,60,70,80]
copied_num_list=num_list
print(f"Original:  {num_list}")
print(f"Copied:    {copied_num_list}")
print('-'*50)

'''The problem using the assignment approach lies in that if you modified the original
list then the copied also will be affected, let's see:'''
num_list=[10,20,30,40,50,60,70,80]
copied_num_list=num_list
num_list.append(90)
print(f"Original:  {num_list}")
print(f"Copied:    {copied_num_list}")
print('-'*50)

'To make an actual copy of a list, we use .copy()'
num_list=[10,20,30,40,50,60,70,80]
copied_num_list=num_list.copy()
num_list.append(90)
print(f"Original:  {num_list}")
print(f"Copied:    {copied_num_list}")
print('-'*50)

'Another actual copying by using list(num_list)'
num_list=[10,20,30,40,50,60,70,80]
copied_num_list=list(num_list)
num_list.append(90)
print(f"Original:  {num_list}")
print(f"Copied:    {copied_num_list}")
print('-'*50)

'Another actual copying by using a colon in the index operator'
num_list=[10,20,30,40,50,60,70,80]
copied_num_list=num_list[:]
num_list.append(90)
print(f"Original:  {num_list}")
print(f"Copied:    {copied_num_list}")
print('-'*50)

'''To create a new list from an existing list in a faster and more elegant method,
 then we need a list comprehension approach
'''
num_list=[10,20,30,40,50,60,70,80]
squared_num_list=[i*i for i in num_list]
print(f"The original numbers {num_list}")
print(f"The squared numbers {squared_num_list}")



