import random

num = 0;
g = 0;
while (g != 2):

    print("Guess heads by entering 1 or tails by entering 2 for this coin flip.");
    answer = input()
    if (answer == 1):
        print("You guessed heads.")
    else:
        print("you guessed tails.")
    flip = random.choice([1, 2])
    if (flip == 1):
        print("The coin landed on Heads.")
    else:
        print("The coin landed on Tails.")
    if (answer == flip):
        print("Congrats you guessed right.")
    else:
        print("Sorry your guess was wrong.")
    num += 1

    print("You have guessed " + str(num) + " times.")

    print("Would you would like to guess again enter 1 or enter 2 to exit?")
    g = input()
    if (g == 2):
        break
    else:
        continue


