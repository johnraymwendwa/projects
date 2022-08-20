import random

while 1 == 1:
    rand_num = input('Please input a number: ')
    if rand_num.isdigit():
        rand_num = int(rand_num)
        break
        if rand_num <= 0:
            print("Please type a number larger than 0")
            continue
    else:
        print("Please type a number next time.")
        continue

random = random.randint(1,rand_num)
guesses = int("0")

while 1 == 1:
    guesses = guesses + int("1")
    guess = input("Please make a guess:")
    if guess.isdigit:
        guess = int(guess)
        if guess == random:
            print("You got it in",guesses,"guesses!")
            break
        else:
            if guess < random:
                print("You are cold")
            elif guess > random:
                print("You are warm")
            continue
    else:
        print("Please type a number")


