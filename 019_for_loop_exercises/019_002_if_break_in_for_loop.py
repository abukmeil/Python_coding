################################# If break inside for loop ############################
'''Suppose you forgot your mobile at your company, given a list of the recent
locations you left in the meeting room. Write a python code that searches among different locations
and if it finds a meeting room then it will break and print your mobile inside this room

'''
import time
Mobile_location="Meeting room"
Recently_visited=["G.M office","Meeting room","Toilet","Administration","Lab"]

for i in Recently_visited:
    print(f"Searching progress ...")
    print('')
    time.sleep(0.3)
    if i=="Meeting room":
        break
print(f"Your mobile inside {i}")
