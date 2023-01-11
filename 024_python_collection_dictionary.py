################################# Python dictionary ############################

'''
A dictionary is a python collection data type (1-D or 2-D) that holds key:value pairs.

The characteristic of a dictionary is given as follows:

1- It can be initiated by curly brackets {}.
2- It holds key:value pairs.
3- No duplication is allowed,
4- Items inside a dictionary are ordered and changeable.
5- A dictionary is mutable.

'''

'Lets create a dictionary that holds the capitals of some countries'
Capitals={"France":"Paris","Italy":"Rome","Norway":"Oslo","India":"New Delhi"}

'To print the attributes and methods of a dictionary object'
#print(dir(Capitals))

'To show a description of each attribute and method'
#print(help(Capitals))

'To retrieve a value of a key, we use the method get, we send the key and receive the value'
print(Capitals.get("Italy"))
print(Capitals.get("France"))
print(Capitals.get("USA"))  # If you send a country that is not listed in the dictionary, then you will receive None
print('-'*50)

'We can use if condition to show if a capital of a country exists or not'
if Capitals.get("Italy"):
    print(f"I love {Capitals.get('Italy')}")
else:
    print("Capital is not included")

if Capitals.get("Egypt"):
    print(f"I love {Capitals.get('Egypt')}")
else:
    print("Capital is not included")
print('-'*50)

'We can update the dictionary using the .update method'
Capitals.update({"USA":"Washington D.C."})
print(Capitals)

'We can update the existing key:value pairs using the .update method, suppose the capital of Italy becomes Milano'
Capitals.update({"Italy":"Milan"})
print(Capitals)
print('-'*50)

'.pop method is used to remove the key:value pair item be sending just the key'
Capitals.pop("USA")
print(Capitals)

'As in list, .popitem method is used to remove the key:value pair. Remember: in the set, the pop method removes the first element'
Capitals.popitem()
print(Capitals)
print('-'*50)

'To erase dictionary items, we use .clear method'
Capitals.clear()
print(Capitals)
print('-'*50)

'What if we want to retrieve only keys from a dictionary'
Capitals={"France":"Paris","Italy":"Rome","Norway":"Oslo","India":"New Delhi"}
Keys=Capitals.keys()  # It will retrieve an object resembling a list of keys inside a tuple
print(Keys)
print('-'*50)

'We can also iterate over keys object'
for key in Keys:
    print(key,end=' ')
print('')
print('-'*50)

'Similarly to the keys, we can also retrieve the values  of a dictionary object'
Values=Capitals.values()
print(Values)   # It will retrieve an object resembling a list of keys inside a tuple
print('-'*50)

'We can also iterate over values object'
for value in Values:
    print(value,end=' ')
print('')
print('-'*50)

'Similarly to the keys and values, we can also retrieve items of pair key:value'
Items=Capitals.items()
print(Items)      # It will retrieve an object resemble a 2d list of tuples
print('-'*50)

'We can iterate over Key:Value items'
for key,value in Items:
    print(key,':',end=' ')
    print(value,end=' ')
    print('')
print('-'*50)
'The same results can be obtained with less print method'
for key,value in Items:
    print(f'{key} : {value}')

print('-'*50)

'A dictionary can store string, numerical values, or heterogeneous data types'
CV={"Name":"Mohanad","Age":35,"Gender":"Male","Mobile":'{0:014}'.format(972589900000)}
print(CV)

'We can make a dictionary using dict method with tuple'
CV2=dict(Name="Moahand",Age=35,Gender="Male",Mobile='{0:013}'.format(97258990000)) # No need to use double qutation marks for keys
print(CV2)
print("-"*50)

'Besides .get method, we can retrieve the value based on a key using square brackets'
print(CV["Name"])
print(CV2["Name"])
print(CV["Age"])
print('-'*50)

'If we pass a key that does not exist, an exception will be raised. Remember: .get method does not raise an error but it gives "None"'
#print(CV["City"])

'Besides .update method, we can update/ add new key:value pairs a dictionary using square brackets []'
CV["City"]="Gaza"
CV2["City"]="Gaza"
print(CV)
print(CV2)
print('-'*50)

'Let us update the mobile number at the first dictionary'
CV["Mobile"]='{0:012}'.format(9725998446)
print(CV)

'Besides the .pop method, we can use the del method to delete  an item from a dictionary'
del CV["City"]
print(CV)
print('-'*50)

'We can use if condition to retrieve the value of a key, besides what we introduced in the above'
if "Name" in  CV:
    print(CV["Name"])

'Another method to retrieve a value of a given key by using try: Except statement'
try:
    print(CV["Name"], CV["Age"])
    print(CV.get("Name"),CV.get("Age"))  # Another way
except:
    print("Not found error")
'What if we passed a key that does not locate in the dictionary'
try:
    print(CV["Job"])
    print(CV.get("Job"))
except:
    print("Error key does not found")
print('-'*50)

'Let us recap looping in a dictionary'
'Looping through keys'
for key in  CV:
    print(key,end=' ')
print('')
'The similar results will be obtained  using CV.keys()'
for  key in CV.keys():
    print(key,end=' ')
print('')
print('-'*50)

'Another way to retrieve the keys through casting the dictionary into a tuple  or a list'
CV3=tuple(dict(Name="ALi",Age=20,Gender="Male",Mobile='{0:013}'.format(97258992200)))
print(CV3)
CV4=list(dict(Name="ALi",Age=20,Gender="Male",Mobile='{0:013}'.format(97258992200)))
print(CV4)


'Similarly, we can loop through the values'
for value in CV:
    print(value,end=' ')
print('')
'We can achieve the same results using CV.values()'
for value in CV.values():
    print(value, end=' ')
print()
'Again we can print key:value pairs'
for key, value in CV.items():
    print(key,':',value,',',end=' ')
print('')
print('-'*50)

'We can copy a dictionary using normal assignment'
CV_new=CV
print(CV)
print(CV_new)
'Remember if you modify the original dictionary, then the copied one will be changed or vice versa'
CV.update({"Job":"Developer"})
CV_new.update({"Status":"Married"})
print(CV)
print(CV_new)
'Normal assignment is not recommended to copy, both original and copied one will give the same object ID'
print(f'Original object:  {id(CV)}')
print(f'The copied object: {id(CV_new)}')
print('-'*50)

'We can do .copy() method to perform an actual copy'
CV_new=CV.copy()
print(CV)
print(CV_new)
print('-'*50)

'Or we can pass  the original dictionary as an argument inside the dict method'
CV_new=dict(CV)
print(CV)
print(CV_new)
print('-'*50)


'We can merge two dictionaries into one, using the update method where the first dictionary will be updated  by the other'
CV2=dict(Name="Moahand",Age=35,Gender="Male",Mobile='{0:013}'.format(97258990000))
CV3=dict(Name="ALi",Age=20,Gender="Male",Mobile='{0:013}'.format(97258992200))
CV2.update(CV3)
print(CV2)
print('-'*50)

'Number as a key'
num_dict={1:30,2:40,3:50,4:60}
print(num_dict)
print('-'*50)

'Important: here we must pass the actual key value, not the index'
#print(num_dict[0])  It will return an error since we do not deal with indices but with values
print(num_dict[1])
print('-'*50)

'Tuple as keys'
tuple_keys=((10,20),(30,40))
tuple_dict={tuple_keys[0]:30,tuple_keys[1]:70}
print(tuple_dict)
print('-'*50)
'''List as keys will return an error because list is mutable and its unique integer identifier can be changed
during its life item, i.e., an un-hashable object. 

Also, a dictionary as a key of a dictionary will retrieve the same error
'''
list_key=[[10,20],[30,40]]
#list_dict={list_key[0]:30,list_key[1]:70}  It will return an error with "unhashable type: 'list'"
'How can we fix it? we can change list to a tuple'
list_dict={tuple(list_key[0]):30,tuple(list_key[1]):70}
print(list_dict)

'Similarly, the dictionary can be a key of another dictionary'
dict_key={70:80,90:100}
dict_dict={(10,20):30,(30,40):70,tuple(dict_key):340}
print(dict_dict)
print('-'*50)

'As in the lists and tuples, we can build a dictionary comprehension if we have homogeneous data samples and we repeat a similar transformation among samples'
names=["Mohanad","Diago","Massimo","Angela"]
names_dict={name:len(name) for name in names}
print(names_dict)
print('-'*50)

'Generating unique key identifiers using uuid module and dictionary, it can generate billions of unique IDs'
from uuid import uuid4  # You can import uuid1,2,3,4,5 but we use uuid4 since it generates random IDs without considering local network privacy
User_dict_identifiers={"Mohaand":uuid4()}
print(User_dict_identifiers)

User_dict_identifiers={"Mohanad":uuid4(),"Ali":uuid4(),"Maria":uuid4()}
print(User_dict_identifiers)
cc=User_dict_identifiers["Mohanad"]
