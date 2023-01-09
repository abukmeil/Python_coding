################################# Multiple choice exam exercise  ############################

'''
Write a python code for a multiple-choice exam of 5 questions:
    - For each question, you must print the question and the choices.
    - At each question the user must know whether the answer is correct or not.
    - At the end of the exam, print the correct answers and the input answers by the user.
    - print the result in percent
'''

'We need different collections to write our code'

questions=("1- How many bones are in the human body?",
           "2- Which animal lays the largest eggs?",
           "3- How many elements are in the periodic table?",
           "4- What is the abundant gas in the Earth's atmosphere?",
           "5- Which planet is the hottest in the solar system?")


'For  options, we need a tuple of tuples to store the choices'


options=(("A. 120","B. 220","C. 206","D. 207"),
         (("A. Oze","B. Chicken", "C. Ostrich","D. Crocodile")),
         (("A. 117","B. 115", "C. 120","D. 118")),
         (("A. Nitrogen","B. Hydrogen", "C. Oxygen","D. Carbon_Dioxide")),
         (("A. Earth","B. Venus", "C. Mars","D. Jupiter")))

'We need a tuple to store our correct answers'
answers=("C","C","D","A",'B')

'We need a list to append the user guess'
user_guesses=[]

'We need to initialize the score by zero'
score=0

'We need to initiate the question_num by zero '
option_index=0

for question in questions:
    print("**********************************************")
    print(question)
    for option in options[option_index]:
        print(option)

    user_guess=input("Enter your answer (A,B,C,D): ").upper()
    user_guesses.append(user_guess)
    if user_guess==answers[option_index]:
        print("Correct answer")
        score+=1
    else:
        print("Incorrect")
        print(f'The correct answer is {answers[option_index]}')
    option_index+=1

'Once we complete all questions, we need to display the results'

print('**********************************************')
print('*************** Final Results ****************')
print('**********************************************')

print('correct answer is: ', end='')
for answer in answers:
    print(answer,end=' ')
print('')

print('Your answer is:    ',end='')
for user_guess in user_guesses:
    print(user_guess,end=' ')
print('')

score= float(score/len(questions))*100
print(f'The final score is {score}')
