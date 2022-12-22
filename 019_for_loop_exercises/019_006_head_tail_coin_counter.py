################################# Head and tail counter of coin ############################
'''
Suppose you are playing with a coin to figure out the binary probability of the coin's side (head, tail)

if the outcome is as follows:

result = ["head","tail","tail","head","tail","head","head","tail","tail","tail",tail","head","head","tail"]

Write a python code that counts the total heads and total tail.

'''

Total_head=0
Total_tail=1

result = ["head","tail","tail","head","tail","head","head","tail","tail","tail","tail","head","head","tail"]

for i in range(len(result)):
    if result[i]=="head":
        Total_head+=1
    elif result[i]=="tail":
        Total_tail+=1


print(f"The total number of head {Total_head}")
print(f"The total number of tail {Total_tail}")
