################################# Calculator program  ############################

'''Write a python program that mimics a simple weight converter (Kilogram to Pounds and vice versa)  using the following:

1 Kgs = 2.205 Lbs
'''

weight=float(input("Enter your weight please: "))
unit=input("Kilogram or Pounds (K for Kilogram, P for Pounds): ").lower()

'Check the unit'
if unit =="K":
    weight*=2.205
    unit='Lbs.'
elif unit =="P":
    weight/=2.205
    unit="Kgs."
else:
    print(f"The {unit} is not valid")

print(f"Your weight is {round(weight,2)} {unit}")


