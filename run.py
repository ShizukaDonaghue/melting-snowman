# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import winter_words
# from snowman import draw_snoman


def game_introduction():
    print("Welcome to the Melting Snowman game!\n")
    print("This is a word guessing game.")
    print("Suggest a letter at a time to guess the word.")
    print("You can also suggest a word if you think you've figured it out!\n")
    print("You can set the difficulty by selecting the number of lives.")
    print("Snowman will start melting for each failed attempt.")
    print("Let's save the snowman before he melts!!\n")

    main()


# def set_number_of_lives():


def get_random_word():
    """
    Selects a random word from words.py for the player to guess.
    """
    word = random.choice(winter_words)
    return word.upper()



# def play_game():


def main():
    get_random_word()


game_introduction()
