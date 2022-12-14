################################# for loop ############################
'''
for loop: is a programming meachnisim to execute a block of code
for a fixed number of time through iteration approach.

In for loop, you are able to iterate over:
1- list
2- range
3- string
4- sequence
5- enumerate of indices
6- any iterable object
 '''

'Use range function to iterate over, note you can not print range function beacuse it is a python object and you need to unpack it using list(range)'
'range[inclusive, execlusive, step] range[0,4,1] print 0,1,2,3 only '

'Counter using for loop for 20 times'
for x in range(1,21,1):
    print(x)
print("Done!")
print("")

'Reversed counting'
for x in reversed(range(1,21,1)):
    print(x)
print("Reversed done")
print('')

'Another reversed counting'
for x in range(20,0,-1):
    print(x)
print("Another reversed!")
print(' ')

'Counting with a step of 2'
for x in range(1,21,2):
    print(x)
print("Done with a step of 2!")
print("")

'Counting with a step of 2 even'
for x in range(2  ,21,2):
    print(x)
print("Done with a step of 2!")
print("")

# continue: Do the condition and if it  is achived just neglect or skipp over it


for x in range(1,21,1):
    if x==13:
        continue
    else:
        print(x)

# break: if condition is acived just break the loop

for x in range(1,21,1):
    if x==13:
        break
    else:
        print(x)