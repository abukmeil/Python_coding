########################################## Math in Python exercises ###################################

# 1- Calculate the circumference of a circle.
'C=2*pi*radius'

import math
radius=float(input("Enter a radius of a circle: "))
circumference=2*math.pi*radius
print(f"The circumference is :{round(circumference,2)} cm")

# 2- Calculate the area of a circle
'Area=math.pi*(radius**2)'

import math
radius=float(input("Enter a radius of a circle: "))
area=math.pi * (radius**2)
print(f"The area of the circle is : {round(area,2)} cm\u00b2")

# Calculate the hypotenuse of a triangle
'C=math.sqrt(pow(a,2)+pow(b,2))'

import math
a=float(input("Enter the length of side a: "))
b=float(input("Enter the length of side b: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypotenuse of a triangle is: {round(c,2)}")







