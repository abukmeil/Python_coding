########################################## Math in Python ###################################


# Arithmetic operation
'Addition'
Friends=0
'Increment variable Friends by 1'
Friends=Friends+1
print(Friends)
'Another way using augmented assignment operator'
Friends=0
Friends+=1
print(Friends)

'Subtraction'
Friends=Friends-1
'Another way using augmented assignment operator'
Friends-=1
print(Friends)

'Multiplication'
Friends=1
Friends=Friends*3
print(Friends)
'Another way using augmented assignment operator'
Friends*=3
print(Friends)

'Division'
Friends=Friends/3
print(Friends)
'Another way using augmented assignment operator'
Friends /=3
print(Friends)

'Exponent'
Friends=2
Friends=Friends**2
print(Friends)
'Another way using augmented assignment operator'
Friends **=2

'modulus'
reminder=Friends %3  # divide friends into a group of 3
print(reminder)

print('************************ Next section*********')
# Math function

x=3.14
y=-4
z=5

'Round number'
result=round(x)
print(result)

'Absolute value'
result=abs(y)
print(result)

'Power function'
result=pow(4,3)
print(result)

'maximum value'
result=max(x,y,z)
print(result)

'Minimum value'
result=min(x,y,z)
print(result)

# Math library
print('************************ Next section*********')
import math

'pi constant'
print(math.pi)

'square root'
print(math.sqrt(x))

'Ceil: round number up'
print(math.ceil(10.2))

'floor: round number to down'
print(math.floor(10.2))

