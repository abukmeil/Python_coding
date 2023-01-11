################################# Logical operator  ############################
'''
Logical  operators are used in a conditional statement
 and    =   when two conditions are True
 or     =   when one condition AT LEAST is TRUE
 not    =   when a condition is False, and vice versa

 '''

'and operator'
Humidity=30

if Humidity  > 30 and Humidity < 50:
    print("The humidity is good ")
else:
    print("The humidity is bad")

if Humidity >= 30 and Humidity <=50:
    print("The humidity is good ")
else:
    print("The humidity is bad")

print("")

'or operator'

Humidity=30

if Humidity  > 30 or Humidity < 50:
    print("The humidity is good ")
else:
    print("The humidity is bad")

if Humidity >= 30  or Humidity <=50:
    print("The humidity is good ")
else:
    print("The humidity is bad")

print('')

'True/ False operator'

temp=15
sunny=True

if temp <=0 or temp >=30:
    print("The temperature is good ")
else:
    print("The temperature is bad")

if sunny:
    print("It is sunny outside")
else:
    print("It is cloudy  outside")



