# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import winter_words
# from snowman import draw_snoman


def game_introduction():
    """
    Game introduction and rules.
    """
    print("Welcome to the Melting Snowman game!\n")
    print("This is a word guessing game.")
    print("Suggest a letter at a time to guess the word.")
    print("You can also suggest a word if you think you've figured it out \\('-')/\n")
    print("You can set the difficulty by selecting the number of lives.")
    print("The snowman will start melting for each failed attempt.")
    print("Let's guess the word and save the snowman before he melts!!\n")

    main()


def set_number_of_lives():
    """
    Lets the player to select the number of lives.
    """
    print("Please select the number of lives.")

    player_choice = False
    while not player_choice:
        choice = input("Enter 7 for 7 lives or 10 for 10 lives: ").upper()
        if choice == "7":
            number_of_lives = 7
            return number_of_lives
        elif choice == "10":
            number_of_lives = 10
            return number_of_lives
        else:
            print("Please select the number of lives.")


def get_random_word():
    """
    Selects a random word from words.py for the player to guess.
    """
    word = random.choice(winter_words)
    return word.upper()



# def play_game():


def main():
    set_number_of_lives()
    get_random_word()


game_introduction()
