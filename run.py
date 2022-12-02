# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
import ascii_art
from words import winter_words
from snowman import draw_snowman


def clear_terminal():
    """
    Clear the terminal to display new content.
    Original code from
    https://www.geeksforgeeks.org/clear-screen-python/
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_page():
    """
    Display the title screen for the game.
    Let the player start the game.
    """
    print(ascii_art.TITLE)
    print("Welcome to the Melting Snowman game!")
    while True:
        choice = input("Please presss ENTER to begin!\n")
        if choice == "":
            clear_terminal()
            game_introduction()
            break
        else:
            print(f'You have entered "{choice}". Please try again!\n')


def game_introduction():
    """
    Display game introduction and rules.
    """
    print(ascii_art.RULE)
    print("Welcome to the Melting Snowman game!\n")
    print("This is a word guessing game.")
    print("Suggest a letter at a time to guess the word.")
    print("You can also suggest a word if you think you've figured it out!\n")
    print("You can set the difficulty by selecting the number of lives.")
    print("The snowman will start melting for each failed attempt.")
    print("Let's guess the word and save the snowman before he melts!!")

    main()


def set_number_of_lives():
    """
    Let the player to select the number of lives.
    """
    while True:
        print("\nPlease select the number of lives.")
        choice = input(
            'Enter "6" for 6 lives, "8" for 8 lives or "10" for 10 lives:\n')
        if choice == "6":
            number_of_lives = 6
            return number_of_lives
        elif choice == "8":
            number_of_lives = 8
            return number_of_lives
        elif choice == "10":
            number_of_lives = 10
            return number_of_lives
        else:
            print(f'You have entered "{choice}". Please try again!')


def get_random_word():
    """
    Select a random word from words.py for the player to guess.
    """
    word = random.choice(winter_words)
    return word.upper()


def restart_game():
    """
    Let the player play the game again or return to the welcome page.
    clear the terminal for new content.
    """
    while True:
        print("Would you like to play again?")
        restart = input("Please enter Y or N:\n").upper()
        if restart == "Y":
            clear_terminal()
            main()
            break
        elif restart == "N":
            clear_terminal()
            welcome_page()
            break
        else:
            print(f'You have entered "{restart}". Please enter Y or N.\n')


def play_game(word, number_of_lives):
    """
    Validate the input from the player and give feedback
    to the player if the input is not as expected.
    The input must be one letter at a time or a word containing
    the same number of letters as the word to be guessed.
    Check if the input from the player is in the word or if the input
    matches the word to be guessed and give feedback to the player.
    Display the number of lives left and letters already tried
    so that the player understands the status of the game.
    """
    suggested_letters = []
    suggested_words = []
    word_to_guess = "_" * len(word)

    clear_terminal()
    print("\nLet's play the Melting Snowman game!")
    print(f"The word to guess has {len(word)} letters. Best of luck!")

    draw_snowman(number_of_lives)

    while number_of_lives > 0:
        guess = input("\nPlease enter a letter or word:\n").upper()
        try:
            if not guess.isalpha():
                print(f'You have entered "{guess}".')
                print("Please enter a letter "
                      f"or a word containint {len(word)} letters.")
            elif len(guess) == len(word) and guess.isalpha():
                if guess in suggested_words:
                    print(f'You have already tried "{guess}".')
                    print("Please try again!")
                elif guess != word:
                    suggested_words.append(guess)
                    print(f'"{guess}" is not the word.')
                    number_of_lives -= 1
                else:
                    word_to_guess = word
                    break
            elif len(guess) > 1 and guess.isalpha():
                print(f"You have entered {len(guess)} letters.")
                print("Please enter a letter "
                      f"or a word containint {len(word)} letters.")
            elif len(guess) == 1 and guess.isalpha():
                if guess in suggested_letters:
                    print(f'You have already tried "{guess}".')
                    print("Please try again!")
                elif guess not in word:
                    number_of_lives -= 1
                    suggested_letters.append(guess)
                    print(f'"{guess}" is not in the word.')
                    if number_of_lives > 0:
                        print(f"You have {number_of_lives} live(s) left.")
                else:
                    suggested_letters.append(guess)
                    print(f'Great! "{guess}" is in the word! Well done!')
                    # Code to display correctly guessed letters:
                    # https://www.youtube.com/watch?v=m4nEnsavl6w
                    word_as_list = list(word_to_guess)
                    indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_to_guess = "".join(word_as_list)
                    # End of code from above source
                    if "_" not in word_to_guess:
                        break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            continue

        if number_of_lives > 0:
            print("The word to guess: ", word_to_guess)
        if len(suggested_letters) > 1 and number_of_lives > 0:
            print("Letters already tried: ", sorted(suggested_letters))

        draw_snowman(number_of_lives)

    if word_to_guess == word:
        clear_terminal()
        print(ascii_art.WIN)
        print(f"\nCongratulations! {word} was the correct answer!\n")
    else:
        clear_terminal()
        print(ascii_art.LOSE)
        print(f"\nGood effort! The correct word was {word}.\n")

    restart_game()


def main():
    """
    Call the main functions to run the game.
    """
    random_word = get_random_word()
    lives = set_number_of_lives()
    play_game(random_word, lives)


welcome_page()
