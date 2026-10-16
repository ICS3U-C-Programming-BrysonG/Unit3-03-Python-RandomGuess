#!/usr/bin/env python3
# Created By: Bryson
# Date: 10 16, 2026
# This program runs a guessing game where
# it asks the user for a number then compares it to
# the randomly generated number.

import random


def main():

    # a number between 1 and
    randomNum = random.randint(1, 10)

    # Get guessed number from the user
    guessed_number = int(input("Enter your guessed number (1 - 10): "))

    # See if the guessed number is equal to the random number
    if guessed_number == randomNum:
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was {}".format(randomNum))


if __name__ == "__main__":
    main()
