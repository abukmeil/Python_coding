################################### Typecasting #########################################
''' - Typecasting is a process in which we convert a value of one data type into another.
    - Data types including string, integer, float, and boolean.
    - Two types of casting including explicit casting and implicit casting.

'''

# Explicit casting: manually converting from one data type to another.
'We use explicit casting keyword such as int, str, float, bool'

my_name="Mohanad"
my_age=35
my_gpa=4.5
student=False

print(type(my_name))
print(type(my_age))
print(type(my_gpa))
print(type(student))
print()

'Casting a value as a float'
my_age=float(my_age)
print(type(my_age))

'Casting a value as an integer'
my_gpa=int(my_gpa)
print(type(my_gpa))

'Casting a value as a string'
student=str(student)
print(type(student))

print()
'Casting as value as a boolean'
my_age=bool(my_age)
print(my_age)
'Note that if you convert any numeric value to a boolean if it is "+" or "-" it will return True, and if it is 0 it returns False.'

my_name=bool(my_name)
print(my_name)
'If the string is empty, it will return False'
my_name=""
my_name=bool(my_name)
print(my_name)
print()

# Implicit casting
'when values or variables are converted into different data types automatically.'

a=2
print(type(a))
b=2.5
print(type(b))
result=a/b
print(result)
print(type(result))

