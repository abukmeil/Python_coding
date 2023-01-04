########################################## Math in Python ###################################


# Arithmetic operation
'Addition'
Friends=0
'Increment variable Friends by 1'
Friends=Friends+1
print(Friends)
print('')

'Another way using augmented assignment operator'
Friends=0
Friends+=1
print(Friends)
print('')


'Subtraction'
Friends=Friends-1
'Another way using augmented assignment operator'
Friends-=1
print(Friends)
print('')

'Multiplication'
Friends=1
Friends=Friends*3
print(Friends)
print('')

'Another way using augmented assignment operator'
Friends*=3
print(Friends)
print('')

'Division'
Friends=Friends/3
print(Friends)
print('')

'Another way using augmented assignment operator'
Friends /=3
print(Friends)

'Exponent'
Friends=2
Friends=Friends**2
print(Friends)
print('')

'Another way using augmented assignment operator'
Friends **=2

'modulus'
reminder=Friends %3  # divide friends into a group of 3
print(reminder)
print('')

# Math function

x=3.14
y=-4
z=5

'Round number'
result=round(x)
print(result)
print('')


'Absolute value'
result=abs(y)
print(result)
print('')

'Power function'
result=pow(4,3)
print(result)
print('')

'maximum value'
result=max(x,y,z)
print(result)
print('')

'Minimum value'
result=min(x,y,z)
print(result)
print('')

# Math library
print('************************ Next section*********')
import math

'pi constant'
print(math.pi)
print('')

'square root'
print(math.sqrt(x))
print('')

'Ceil: round number up'
print(math.ceil(10.2))
print('')

'floor: round number to down'
print(math.floor(10.2))
print('')

# numerize lib for making large numbers readble

from numerize import numerize as n
num=123_456_654_213
print(n.numerize(num))

num=123_213
print(n.numerize(num))