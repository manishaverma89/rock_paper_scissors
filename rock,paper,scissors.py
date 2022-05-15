import random    # import random module
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


game_images = [rock, paper, scissors] 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you loose!")
else:  
  print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You loose!")
elif computer_choice > user_choice:
  print("You loose!")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw!")

  
  

