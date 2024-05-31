# -*- coding: utf-8 -*-
"""Bhola_Prog6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HZx9lfG2S7QPivYwlW348a74O1MUDlqY
"""

import random
from IPython.display import display, Image
import ipywidgets as widgets

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game(user_name, user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Display computer's choice
    display(Image(filename=f'images/image{choices.index(computer_choice) + 1}.jpg'))

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Display result
    print(result)

# Main function
def main():
    # Ask user's name
    user_name = input("What do you want to be called in this game? ")

    # Create radio buttons for user to choose
    radio_buttons = widgets.RadioButtons(
        options=['rock', 'paper', 'scissors'],
        description='Choose:',
        disabled=False
    )

    # Create button to start round
    button = widgets.Button(description="Start Round")

    # Function to handle button click event
    def on_button_click(b):
        play_game(user_name, radio_buttons.value)

    # Link button click event with function
    button.on_click(on_button_click)

    # Display widgets
    display(radio_buttons, button)

# Start the game
main()