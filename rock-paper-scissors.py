import random

user_wins = 0
ai_wins = 0
options = ["rock","paper","scissors"]

while 1 == 1:
    user_pick = input("Pick Rock/Paper/Scissors or Q to quit: ").casefold()
    if user_pick == "q":
        break
    elif user_pick not in options:
        print("Your choice is not vaid!")
        continue    
    else:
        ai_pick = options[random.randint(0,2)]
        print("AI chose",ai_pick)

    if user_pick == ai_pick:
        print("you both picked the same option, try again!")
        continue
    elif user_pick == "rock" and ai_pick == "scissors":
        print("you won!")
        user_wins = int(user_wins) + 1
    elif user_pick == "scissors" and ai_pick == "paper":
        print("you won!")
        user_wins = int(user_wins) + 1
    elif user_pick == "paper" and ai_pick == "rock":
        print("you won!")
        user_wins = int(user_wins) + 1
    else:
        print("You lost!")
        ai_wins = int(ai_wins) + 1

print("You won",user_wins,"rounds")
print("AI won",ai_wins,"rounds")
print("Goodbye!")
