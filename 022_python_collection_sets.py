#################################  Sets  ############################

'''
A collection is a single variable that is used to store multiple variables

A set is a 1-D collection that is surrounded by curly brackets.
Sets are helpful when we work with constants, such as a set of colors or any unique measurements.

The characteristic of a set is listed as follows:

1- It can be initiated by using double round brackets {}.
2- I can hold much different data types such as str, int, and only False from logical operators.
3- Elements inside a set are unordered elements, index is not allowed "not sub-scriptable".
3- A set doesn't allow duplicating elements.
4- A set is mutable (only Add/ Remove without changing elements without item assignment) and iterable.
5- Sets are faster than lists.
'''


'A set is created by initiating curly brackets and by separating elements by ","'
Fruits={'cherry','banana','apple','watermelon', 'pineapple', 'coconut','banana'}
'When printing the following list we will find that it removes the duplication and change the order of the elements'
print(Fruits)
print('-'*50)

'To print the attributes and methods for a tuple object'
#print(dir(Fruits))  #There are not many methods  for tuples (only count and index methods)

'To show a description of each attribute and method'
#print(help(Fruits))

'To print the length or number of elements (Not repeated) inside a list we use len function'
print(len(Fruits))
print('-'*50)

'Checking if an element is included in a tuple or not'
print('cherry' in Fruits)
print('-'*50)

'We are not allowed to use the index operator in a set'
#print(Fruits[0])  # Returns error
Fruits.add('orange')
print(Fruits)
print('-'*50)

'We can remove an element from a set'
Fruits.remove('watermelon')
print(Fruits)
print('-'*50)

'We can use the discard method to remove an element from a list, and if the element does not exist then no error message will arise'
Fruits.discard('orange')
print(Fruits)
print('-'*50)

'A set is iterable'
for fruit in Fruits:
    print(fruit, end=' ')
print('')
print('-'*50)


'To remove the first element of a list we use the pop method. Note: it is different from a list, wherein a list pop drops the last element'
Fruits.pop()
print(Fruits)
print('-'*50)

'To clear all elements from a set, we use the clear method'
Fruits.clear()
print(Fruits)
print('-'*50)

' A list can be converted into a set using the set function'
my_list=[10,20,30,4,0,50,60]
print(my_list)
my_set=set(my_list)
print(my_set)
print('-'*50)

'A string also can be converted into a set with unique letters'
my_string='My name is mohanad'
print(my_string)
print(len(my_string))
my_set=set(my_string)
print(my_set)
print(len(my_set))   # Useful to know how many unique elements in a  string
print('-'*50)

'Remember {} alone offer dictionary not a set, you must use set function'
my_set={}
print(type(my_set))
my_set=set()
print(type(my_set))
print('-'*50)

'The union between two collections or sets combines elements from both sets without duplication'
prime_nums ={2, 3, 5, 7, 11, 13, 17, 19, 23 }
even_nums  ={0, 2, 4, 6, 8, 10, 12, 14}
odd_nums   ={1, 3, 5, 7, 9, 11, 13, 15, 17}
union_set=odd_nums.union(even_nums)     # or print(odd_nums | even_nums)
print(union_set)
print('-'*50)

'The intersection gives the elements that are only shared between sets '
intersetion_set_even_prime=even_nums.intersection(prime_nums)     # or print(set_A & set_B)
print(intersetion_set_even_prime)
print('-'*50)

'The difference returns all elements from the first set that are not repeated in the second set'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
difference=set_A.difference(set_B)               # or print(set_A - set_B)
print(difference)
print('-'*50)

'The symmetric difference returns all elements from setA and setB that are not located at both'
sym_difference=set_A.symmetric_difference(set_B)
print(sym_difference)
sym_difference=set_B.symmetric_difference(set_A)
print(sym_difference)
print('-'*50)

'To add elements from one set to another set without duplication, we use update'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_A.update(set_B)
print(set_A) # Note: this is applied inplace
print('-'*50)

'To update a set with only joint elements from another set, we use intersection_update'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_A.intersection_update(set_B)  # Note: this is applied inplace
print(set_A)
print('-'*50)

'The difference update is used to update a set by removing elements found in another set'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_A.difference_update(set_B)
print(set_A)
print('-'*50)


'Update a set with elements from a set A and a set B but not in both'
set_A.symmetric_difference_update(set_A)
print(set_A)
print('-'*50)

'Subset set means all elements from the first set is located in the second set'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_C={1,2,3}
print(set_A.issubset(set_B))             #or print(x<y)
print(set_C.issubset(set_A))
print('-'*50)

'If the first set contains all elements from the second set, then the  first set is called superset'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_C={1,2,3}
print(set_B.issuperset(set_A))
print(set_A.issuperset(set_C))
print('-'*50)

'isdisjoint returns True if both sets contain different elements'
set_A={1,2,3,4,5,6,7,9,10}
set_B={1,2,4,5,7,10,20}
set_C={20,30,40}
print(set_A.isdisjoint(set_B))
print(set_A.isdisjoint(set_C))
print('-'*50)

'Copy a set using simple assignment, consider that any update on set_B will update set_A because we copy the reference only'
set_A={1,2,3,4,5,6,7,9,10}
set_B=set_A
print(set_B)
print(set_A)
set_B.add(11)
print(set_A)
print(set_B)
print('-'*50)

'To make an actual copy, we  use .copy method'
set_A={1,2,3,4,5,6,7,9,10}
set_B=set_A.copy()
print(set_A)
print(set_B)
set_B.add(11)
print(set_A)
print(set_B)
print('-'*50)

'Another actual copy could be done by using the set method of a set'
set_A={1,2,3,4,5,6,7,9,10}
set_B=set(set_A)
print(set_A)
print(set_B)
set_B.add(11)
print(set_A)
print(set_B)
print('-'*50)


'''Often there is a need to keep the set frozen,
for that we use frozenset: you should not be able to change the content of your set'''

set_A=frozenset([10,20,30,40,50,60])
#set_A.add(21) # This will return an error even for an update or remove.
print(set_A)
# Note for frozenset, union, intersection, and difference methods are working.







