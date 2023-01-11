################################# Format specifiers  ############################

'''Format specifiers are used within print statement as print(f" {}")
format specifiers = {:flags} allows us to format a value based on what flag is inserted
i.e., format specifier={value:flag}

Flags are listed as follows:
.(number)f  = round to how many decimal places
:(number)   = allocate that many places
:           = insert a space before the positive number
:03         = zero padding by 3  before printing the number
:<          = left justify
:>          = right justify
:^          = center align
:+          = indicates a positive value it shows positive and negative signs
:=          = place the sign in the leftmost position
:, Comma separated

'''
weight1  =  3.1446
weight2  =  20.5145
weight3  =  12.54512
print(f"The  first weight is {weight1} Kg")
print(f"The second weight is {weight2} Kg")
print(f"The third weight is {weight3}  Kg")
print(' ')
"Let's try format specifiers"

'Floating digits specifier'
print(f"The  first weight is {weight1:.2f} Kg")
print(f"The second weight is {weight2:.2f} Kg")
print(f"The third weight is {weight3:.2f} Kg")
print('')

'If you prefer less precision we can use only 1 floating point'
print(f"The  first weight is {weight1:.1f} Kg")
print(f"The second weight is {weight2:.1f} Kg")
print(f"The third weight is {weight3:.1f} Kg")
print('')

'If you use out or range floating point, then it will pad to zeros'
print(f"The  first weight is {weight1:.8f} Kg")
print(f"The second weight is {weight2:.8f} Kg")
print(f"The third weight is {weight3:.8f} Kg")
print("")

'If you want to allocate spaces before each value, add a number after the double colon'
print(f"The  first weight is {weight1:10} Kg")
print(f"The second weight is {weight2:10} Kg")
print(f"The third weight is {weight3:10} Kg")
print("")

'If you want to add zeros (add zeros) before printing use :0 number '
' Note we use :006 to pad one zero and so on for some python versions'
num=2
print(f"{num:03}")
print(f"The  first weight is {weight1:08} Kg")
print(f"The second weight is {weight2:08} Kg")
'Consider if your number is long you must increase the padding number to have the right result'
print(f"The third weight is {weight3:010} Kg")
print("")

'If you want to left justifying the number we use {:< number } i.e., it adds the space after'
print(f"The  first weight is {weight1:<10} Kg")
print(f"The second weight is {weight2:<10} Kg")
print(f"The third weight is {weight3:<10} Kg")
print("")

'If you want to right justify the number we use {:> number } i.e., it adds the space after'
' '
print(f"The  first weight is {weight1:>10} Kg")
print(f"The second weight is {weight2:>10} Kg")
print(f"The third weight is {weight3:>10} Kg")
print("")

'If you want to center justifying the number we use {:^ number } i.e., it adds the space after'
' Note: that is the default setting in Python'
print(f"The  first weight is {weight1:^} Kg")
print(f"The second weight is {weight2:^} Kg")
print(f"The third weight is {weight3:^} Kg")
print("")

Temp1   =   123.254
Temp2   =   -5.3
Temp3   =   20

'If you want to print values with their sign you can add +'
print(f"The  first temp is {Temp1:+} C")
print(f"The second temp is {Temp2:+} C")
print(f"The third temp is {Temp3:+} C")
print("")

'Comma separated thousands'
'Note: we can use _ as a separator for input numbers'
price1  =   123_45.587_56
price2  =   123.1248
price3  =   578_444_2.455
print(f"The  first price is {price1:,} C")
print(f"The second price is {price2:,} C")
print(f"The third price is {price3:,} C")
print("")

'We can use combined flags to together'
val1  =   123_45.587_56
val2  =   - 123.1248
val3  =   578_444_2.455
print(f"The  first value is {val1:+,.2f} C")
print(f"The second value is {val2:+,.2f} C")
print(f"The third value is {val3:+,.2f} C")
print("")

'%s is used for as string specifier'
name = "Mohanad"
print("Hello, %s!"  %name)

'%d is used with integer variables'
name = "Mohanad"
age=35
print("Your name is %s and your age is %d"%(name,age))
