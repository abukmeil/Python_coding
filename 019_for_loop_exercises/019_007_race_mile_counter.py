################################# Head and tail counter of coin ############################
'''
Suppose you are entering a marathon with an intelligent watch, where the total distance is a mile
after each mile, you pass the watch show a message that you ran i mile so far, and the watch asks if you want to continue or not
if you do not want to continue the marathon, then a conclusion message will appear to you and if you
reach 30 miles you will receive a congratulation
'''

for i in range(30):
    if i !=30:
        print("You ran",i+1,"miles.")
        ask_me=input("Do you want to  to stop (y:yes): ")
        if ask_me=="n":
            continue
        elif ask_me=="y":
            break
if i+1 ==30:
    print(f" You are hero, you run {i+1} mile")
else:
    print("You didn't finish marathon but hey congrats anyways! You still ran", i+1,"miles")
