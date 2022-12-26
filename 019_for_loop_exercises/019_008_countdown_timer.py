################################# Head and tail counter of coin ############################
'''
Write a python program that prompts the user to enter a number of seconds,
thereafter based on that number set up a countdown timer
'''
import time

enter_second=int(input("Enter the number of second you want to countdown: "))


'Convert the second to minutes and printing seconds'
#for  i in range(enter_second,-1,-1):
#    seconds=i%60
#    print(f"00:00:{seconds:02}")   # We considered the format specifier for 0 padding i.e., adding 0 before numbers from 0-9
#    time.sleep(0.8)

'Convert the second to minutes and printing minutes'

#for i in range(enter_second,-1,-1):
#    seconds=i%60
#    minutes=int(i/60)%60
#    print(f"00:{minutes}:{seconds:02}")  # We considered the format specifier for 0 padding i.e., adding 0 before numbers from 0-9
#    time.sleep(0.8)

'Convert the second to minutes and printing hours'
for i in range(enter_second,-1,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/(60*60))
    print(f"{hours:02}:{minutes:02}:{seconds:02}")  # We considered the format specifier for 0 padding i.e., adding 0 before numbers from 0-9
    time.sleep(0.8)













