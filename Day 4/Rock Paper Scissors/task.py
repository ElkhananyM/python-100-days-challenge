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

rps_list = [rock, paper, scissors]
player_choice = input("Pick an option between Rock, Paper, or Scissors: ").lower()
cpu_choice = random.choice(["rock", "scissors", "paper"])

if player_choice == "rock" and cpu_choice == "rock":
    print(f"Player chose Rock \n {rock} \n Computer chose Rock \n {rock} \n It's a draw.")

elif player_choice == "scissors" and cpu_choice == "scissors":
    print(f"Player chose Scissors \n {scissors} \n Computer chose Scissors \n {scissors} \n It's a draw.")

elif player_choice == "paper" and cpu_choice == "paper":
    print(f"Player chose Paper \n {paper} \n Computer chose Paper \n {paper} \n It's a draw.")

elif player_choice == "rock" and cpu_choice == "scissors":
    print(f"Player chose Rock \n {rock} \n Computer chose Scissors \n {scissors} \n You win!")

elif player_choice == "rock" and cpu_choice == "paper":
    print(f"Player chose Rock \n {rock} \n Computer chose Paper \n {paper} \n Computer wins!")

elif player_choice == "scissors" and cpu_choice == "rock":
    print(f"Player chose Scissors \n {scissors} \n Computer chose Rock \n {rock} \n Computer win!")

elif player_choice == "scissors" and cpu_choice == "paper":
    print(f"Player chose Scissors \n {scissors} \n Computer chose Paper \n {paper} \n You win!")

elif player_choice == "paper" and cpu_choice == "rock":
    print(f"Player chose Paper \n {paper} \n Computer chose Rock \n {rock} \n You win!")

elif player_choice == "paper" and cpu_choice == "scissors":
    print(f"Player chose Paper \n {paper} \n Computer chose Scissors \n {scissors} \n Computer win!")
else:
    print("Wrong inputs.")
