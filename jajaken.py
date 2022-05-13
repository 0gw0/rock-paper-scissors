rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

elements = [rock,paper,scissors]

choice = int(input("Choose 0 for rock 1 for paper and 2 for scissors\n"))
com_choice = random.randint(0,2)

if (choice not in range(0,3)):
    print("you did not draw in. time, you lose")
else:
    print ('you chose: ' + elements[choice])
    print ('computer chose: ' + elements[com_choice])
    
    if (choice == com_choice - 1 or (choice == 2 and com_choice == 0)):
      print("you lose :(")
    elif (choice == com_choice):
      print("its a draw")
    else:
      print("you win!")
