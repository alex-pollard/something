import random
# choices=['rock','paper','scissors']
# #           1,     2,      3
# computerChoice=choices.index(choices[random.randint(0,2)])
# playerChoice=choices.index(input('Enter your choice').lower())
# if (playerChoice-computerChoice == 1 or playerChoice-computerChoice== -2):
#     print('you win')

playerChoice = input("Rock paper scissors! Enter your choice: ")
if (playerChoice.lower()=='rock' or playerChoice.lower()=='scissors' or playerChoice.lower()=='paper'):
    choices=['you win','you lose','you tied']
    print(choices[random.randint(0,2)])
else:
    print("incorrect usage")