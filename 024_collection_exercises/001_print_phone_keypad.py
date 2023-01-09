################################# Phone keypad exercise  ############################

'''
Suppose you have to design a phone keypad, then you will end up with many different options:

1- Use a list of lists.
2- Use a list of tuple, or tuple of tuple.
3- Use a list of sets.

- To design the keypad, you want to consider the 2-d collection that orders the elements, i.e., we exclude sets because
it holds un-ordered elements.
- We can use 2-d collection of lists since it orders the elements, but it consume more memory
- The best choice here is to select  a tuple of tuples, less memory, and no duplication

Write a python code that prints the keypad of any phone.
'''

elements_pad=((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))

for tuple in elements_pad:
    print(tuple)
print('-'*50)
'The above for loop prints the elements in an untidy way'


for tuple in elements_pad:
    for element in tuple:
        print(element,end=' ')
    print('')


