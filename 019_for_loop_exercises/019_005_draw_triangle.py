################################# If break inside for loop ############################
''' Write a python code that draws the following shape:

*
**
***
****
*****
******
*******
********

'''
symbol=""
for _ in range(8):
    symbol+="*"
    print(symbol)

# Another solution using two for loops


for _ in range(8):
    symbol=""
    for j in range(_+1):
        symbol+='*'
    print(symbol)