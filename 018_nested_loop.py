################################# Nested  loop ############################

'''
- Is a loop that is found within a code of another loop.
- Tow consecutive loops are formed to execute one task, i.e, in the structure there is an outer loop and an inner loop
-or one loop inside another loop    outer loop:
                                        inner loop:
- The form of nested loop is situational, i,e, your can find for loop inside for loop, or for loop insider wile loop,

or while loop inside while loop
'''


'Suppose we want to print the numbers between 1-15 '
for i in range(1,16,1):
    print(i)
print('')

'To print the number horizontally, we use end statement'
for i in range(1,16,1):
    print(i,end="")
print('')

'If you want to add little bit spaces between numbers'
for i in range(1,16,1):
    print(i,end=' ')

'Suppose we want to repeat a sequence of a number three times, we use another loop'

for i in range(3):
    for i in range(1,16,1):
        print(i,end=' ')
print("")

' at the above code, all were printed at the same line and we need to separate each sequence'
for i in range(3):
    for i in range(1,16,1):
        print(i,end='')
    print('')
print("")
'We can change the counter name of the loop)'
for i in range(3):
    for j in range(1,16,1):
        print(j,end='')
    print('')

#  Example: Printing a rectangle shape based on user input

rows=int(input('Enter the number of rows: '))
column=int(input('Enter the number of columns: '))
symbol=input("Enter the preferred symbol (* ,#,@, etc): ")

for x in range(rows):
    for y in range(column):
        print(symbol,end='')
    print('')