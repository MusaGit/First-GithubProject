import math
import random

def get_user_choice(user_input):
    user_input = user_input.lower()
    if user_input == 'bear' or user_input == 'human' or user_input == 'gun':
         return user_input
    else:
        return "enter valid option"

def get_computer_choice ():
    random_number = math.floor(random.uniform(0, 3))
    if random_number == 0:
        return "bear"
    if random_number == 1:
        return "human"
    if random_number:
        return "gun"

def determineWinner(user_choice, computer_choice):
   if user_choice == computer_choice:
       return 'It is a tie'
   if user_choice == 'human':
       if computer_choice == 'bear':
           return 'You have been mauled by a bear'
       else:
           return 'You have disarmed a gun'
   if user_choice == 'bear':
       if computer_choice == 'gun':
           return 'You have been shot by a gun'
       else:
           return 'You have mauled a human'
   if user_choice == 'gun':
     if computer_choice == 'human':
         return 'Your gun has been disarmed'
     else:
         return 'You have shot a bear'

def play_game ():
    prompt_user_choice = input("Choose bear, human or gun ")
    user_choice = get_user_choice(prompt_user_choice)
    computer_choice = get_computer_choice ()
    print(user_choice)
    print(computer_choice)
    print(determineWinner(user_choice, computer_choice))

play_game ()
    
    

  

 
  