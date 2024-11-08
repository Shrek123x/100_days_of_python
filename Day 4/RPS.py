import random
rounds_to_play = int(input("How many rounds would you liek to play: "))
player_score = 0
computer_scrore = 0

def art(choice):
    if choice == 'rock':
        print(choice)
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif choice == 'paper':
        print(choice)
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif choice == "scissors":
        print(choice)
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

for i in range(rounds_to_play):
    player_choice = str(input("paper, scissors, rock: ").lower())
    choices = ["paper", 'scissors', 'rock']
    computer_choice = random.choice(choices)
    ties = 0
    # if it is a tie
    if (player_choice == "paper" and computer_choice == "paper") or (player_choice == 'rock' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'scissors'):
        print("Computer Picks: ")
        art(computer_choice)
        print('Player Picks: ')
        art(player_choice)
        print("It is a tie")
        ties += 1
        i += 1
    # if computer wins
    elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == 'paper' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'rock'):
        print("Computer Picks: ")
        art(computer_choice)
        print('Player Picks: ')
        art(player_choice)
        computer_scrore += 1
        print(f"Current score for computer: {computer_scrore}")
        i += 1
    # if player wins
    else:
        player_score += 1
        print("Computer Picks: ")
        art(computer_choice)
        print('Player Picks: ')
        art(player_choice)
        print(f"Current score for player: {player_score}")
        i += 1

if computer_scrore > player_score:
    print(f"The computer won {computer_scrore} out of {rounds_to_play}")
    print(f"Player Has scored {player_score} out of {rounds_to_play} rounds")
    print(f"There was {ties} draws")
elif computer_scrore == player_score:
    print(f"It was a tie out of {ties} within {rounds_to_play} rounds")
else:
    print(f"You the player have won {player_score} out of {rounds_to_play}")
    print(f"Computer has scored {computer_scrore} in {rounds_to_play} rounds")
    print(f" There was {ties} draws")
