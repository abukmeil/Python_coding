################################# Calculator program  ############################

'''Write a python program that mimics a simple calculator using the following:
+ for summation
- for subtraction
* for multiplication
/ for division
'''

operator=input("Enter the operator (+, -, *, / ): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

'Select the desired operator'

if operator == '+':
    result=num1+num2
    print(f"The result is {round(result,2)}")
elif operator == '-':
    result=num1-num2
    print(f"The subtraction is {round(result,2)} ")
elif operator == '/':
    result= num1/num2
    print(f"The result is {round(result,2)}")
elif operator == '*':
    result=num1*num2
    print(f"The result is {round(result,2)}")
else:
    print(f"The {operator} is not a valid operator")



