#!/usr/bin/env python3

# Import what is need to generate a random number
import random

# Generate a random number for the User to guess
randomNumber = random.randint(1, 10)
tries = 1

# The user's name
userName = input("Hello, What is your user name? ")

# Say hello to the user
print("Hello", userName + ".", )

# Ask if the user wants to play
question = input("Would you like to play a game? [Y/N] ")

# Check the user's answer
# =======================
# If the user says no
if question == "n":
    print("Oh...okay. Bye!")

# If the user says yes
if question == "y":
    print("I'm thinking of a number between 1 & 10")
    
    # Get the user's input for the guess
    guess = int(input("Take a guess: "))
    # Check the guess
    if guess > randomNumber:
        print("It's lower")
    if guess < randomNumber:
        print("It's higher")
    if guess == randomNumber:
        print("You are right! It only took you 1 try, good job!")

    # Keep going until the User gets it right
    while guess != randomNumber:
        tries += 1
        guess = int(input("Try again: "))
        
        # Check the guess
        if guess > randomNumber:
            print("It's lower")
        if guess < randomNumber:
            print("It's higher")
        if guess == randomNumber:
            print("You are right! It took you", tries, "tries!")