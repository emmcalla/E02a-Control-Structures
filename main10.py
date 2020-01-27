#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
# This line prints the words 'Greetings!' on the terminal's display.
colors = ['red','orange','yellow','green','blue','violet','purple']
# This line creates the variable 'colors' and generates a list of values for it.
play_again = ''
# Creates a variable and assigns a value to it. Allows player to play again.
best_count = sys.maxsize            # the biggest number
# Creates a variable and assigns a value to it. Allows the player to see high scores.
while (play_again != 'n' and play_again != 'no'):
    # This creates the no option for the player when asked if they want to play again.
    match_color = random.choice(colors)
    # This choses a random color from the list of colors and asks the player to input the randomly chosen color.
    count = 0
    # This keeps track of how many times the player has tried to guess the color.
    color = ''
    # This creates a variable, the color that will be guessed.
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count))

    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing!')