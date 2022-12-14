################################# Compound Interest exercise ############################

'''Compound of interest: is the amount of the monetary charge for the privilege of borrowing money
in case you deposit the money, the interest will be reduced.

The formula to calculate the compound interest is given as follows:

A=P(1+(r/n))^t

A   =   final amount,
P   =   initial principal balance
r   =   interest rate
n   =   number of times interest applied per time period (will use it =100)
t =  is the number of time periods (usually in years) elapsed

'''
Principal_amount    =   0
rate                =   0
time                =   0

'Prompting the user to propose a principal amount, considering the amount cannot be <=0'
while Principal_amount <=0:
    Principal_amount=float(input("Enter your principal amount please: "))
    if Principal_amount <=0:
        print("Principal amount cannot be less than or equal to 0")

'Prompting the user to propose a rate, considering the rate cannot be <=0'
while rate <=0:
    rate=float(input("Enter the rate of interest please: "))
    if rate <=0:
        print("The rate can not be less than or equal 0")


'Prompting the user to propose the time, considering that the time cannot be <=0'
while time<=0:
    time=int(input("Enter the  time in years: "))
    if time <=0:
        print("The time period can not be lower than or =0")

A= Principal_amount*pow((1+rate/100),time)
print(A)

