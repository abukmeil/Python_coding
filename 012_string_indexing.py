################################# String indexing and slicing ############################
'''
String indexing allows us to access elements of a sequence such as a string using the indexing operator []
[] is called an indexing operator

[start: end: stop]
'''
credit_card_number="1234-5678-5456-9872"

'The first element is accessed using index 0'
print(credit_card_number[0])
'The second element is accessed using index 1 and so on'
print(credit_card_number[1])


'With indexing operator, up to three fileds can be filled [start : end: stop]'

'Accessing the first three elements'
print(credit_card_number[0:3])  # 4 is exclusive but 0 is inclusive

'Printing with the frequency of 2 indices'
print(credit_card_number[0:4:2])

'Printing from a specific index to the end'
print(credit_card_number[5:])

'Negative index is used for reverse accessing'
print(credit_card_number[-1])

'using step [:,:,step]'
'Printing with the frequency of 2 indices'
print(credit_card_number[0:4:2])

'Printing all elements with a step of three i.e., step=3'
print(credit_card_number[::3])

'Printing the last four digits of the string'
Last_four_digits=credit_card_number[-4:]
print(f"XXXX_XXXX_XXXX_{Last_four_digits}")

'Reversing strings'
reversed_string=credit_card_number[::-1]
print(f"The reversed string is {reversed_string}")

'Reversing a string with a step of 4'
reversed_string_step4=credit_card_number[::-4]
print(f"The reversed string with a step of 4 is {reversed_string_step4} ")


