################################# Calculator program  ############################

'''Write a python program that mimics a simple temperature converter (Celsius to Fahrenheit)  using the following:

Fahrenheit =  (Celsius * (9/5) )+32
Celsius = (Fahrenheit-32)*(5/9)
'''

unit=input("Enter the temperature in Celsius or Fahrenheit (C/ F ): ")
temperature= float(input("Enter the  temperature degree: "))

if unit == "F" or unit == "F".lower():
    temperature=round((temperature-32)*5/9,2)

    print(f"The temperature in Fahrenheit is {temperature} C")
elif unit =="C" or  unit =="C".lower():
    temperature=round((9*temperature)/5+32,2)
    print(f"The temperature in Celsius is {temperature} F")
else:
    print(f"The {unit} is invalid")


