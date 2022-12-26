'''
Suppose work a bank and you are asked to write a python program that validate the credit card for
the customers give a protocol.

verification protocol:

1- Remove and ' ', '-'.'_'
2- Add all digits in the odd places from right to left
3- Double every second digit from right to left (If the result is two digits, then add them together to get a single number)
4- Sum the totals of the step 2 , 3
5- If if sum is divided by 10, then the credit card is valid

'''
import copy

credit_card=input("Enter your credit card for verification: ")

punctuation_mark=[' ','-','_']
for i in punctuation_mark:
    credit_card=credit_card.replace(i,'')
print(credit_card)
normalized_credit_card=credit_card[:]
normalized_credit_card=normalized_credit_card[::-1]
# 2


sum_odd_location_right_left=0
for idx,val in enumerate(normalized_credit_card):
    if idx % 2 != 0:
        sum_odd_location_right_left+=int(val)
print(sum_odd_location_right_left)
print('-----------------------------------')
# 3

sum_even_digits=0
for i in normalized_credit_card[1::2]:
    i=int(i)*2
    if i >=10:
        sum_even_digits+=(1+int(i%10))
    else:
        sum_even_digits+=i
print(sum_even_digits)
print('-----------------------------------')

#4
sum_total=sum_odd_location_right_left+sum_even_digits
print(sum_total)

#5
if sum_total %10==0:
    print("Your credit card is valid")
else:
    print("Your credit card is invalid")


