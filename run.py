# Import random to choose a word randomly from words.py for each game
import random

# Import os to interact with the operating system to clear the terminal
import os

import ascii_art
from words import winter_words
from snowman import draw_snowman
from font_styles import styles


def clear_terminal():
    """
    Clears the terminal to display new content.
    Original code from
    https://www.geeksforgeeks.org/clear-screen-python/
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_page():
    """
    Displays the title screen for the game.
    Prompts the player for keyboard input to start the game.
    """
    print(ascii_art.TITLE)
    print(styles.CYANBOLD + "Welcome to the Melting Snowman game!" +
          styles.END)

    input("Please presss ENTER to begin!\n")
    clear_terminal()
    game_introduction()


def game_introduction():
    """
    Displays game introduction and rules.
    """
    print(ascii_art.RULE)
    print(styles.BOLD + "Here is how to play!\n" + styles.END)
    print("This is a word guessing game.")
    print(styles.CYANBOLD + "  1. Suggest " + styles.UNDERLINE +
          "a letter at a time" + styles.RESETUNDERLINE +
          " to guess the word, or ")
    print("  2. Suggest " + styles.UNDERLINE + "a word" +
          styles.RESETUNDERLINE + " if you think you've figured it out!\n" +
          styles.END)
    print("You can set the difficulty by selecting the number of lives.")
    print("The snowman will start melting for each failed attempt.")
    print("Let's guess the word and save the snowman before he melts!!")

    main()


def set_number_of_lives():
    """
    Requests the player to select the number of lives to set the
    difficulty. The loop continues until a valid input is provided.
    """
    while True:
        print("\nPlease select the number of lives.")
        choice = input(styles.CYANBOLD +
                       'Enter "6" for 6 lives, "8" for 8 lives'
                       ' or "10" for 10 lives:\n' + styles.END)
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
            print(styles.YELLOWBOLD +
                  f'Invalid input: you have entered "{choice}".'
                  " Please try again!" + styles.END)


def get_random_word():
    """
    Chooses a winter-themed word randomly from words.py
    for the player to guess.
    """
    word = random.choice(winter_words)
    return word.upper()


def restart_game():
    """
    Asks the player if they would like to play the game again.
    If yes, clears the terminal and calls the main function to restart
    the game. If no, clears the terminal and calls the welcome_page
    function. The loop continues until a valid input is provided.
    """
    while True:
        print(styles.CYANBOLD + "Would you like to play again?" + styles.END)
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
            print(styles.YELLOWBOLD +
                  f'Invalid input: you have entered "{restart}".'
                  " Please enter Y or N.\n" + styles.END)


def play_game(word, number_of_lives):
    """
    Lets the player know how many letters are in the word
    to be guessed at the start of the game.
    Requests the player to enter a letter or word.
    Validates the input from the player and gives feedback
    to the player, if the input is not as expected.
    The input must be one letter at a time or a word containing
    the same number of letters as the word to be guessed.
    Checks if the input from the player is in the word or if the input
    matches the word to be guessed and gives feedback to the player.
    Displays the number of lives left and letters already tried
    so that the player can track the progress of the game.
    Clears the terminal each time a letter or word is suggested
    so that it is easier and cleaner to read the terminal.
    The loops continues until the word is correctly guessed or
    until the number of lives reduces to zero.
    """
    suggested_letters = []
    suggested_words = []
    word_to_guess = "_" * len(word)

    clear_terminal()
    print(styles.BOLD + "\nLet's play the Melting Snowman game!\n" +
          styles.END)
    print("The word to guess has " + styles.CYANBOLD +
          f"{len(word)} letters" + styles.END + ".")
    print("Best of luck!")

    draw_snowman(number_of_lives)

    while number_of_lives > 0:
        guess = input("Please enter a letter or word:\n").upper()
        clear_terminal()
        try:
            if not guess.isalpha():
                print(styles.YELLOWBOLD +
                      f'Invalid input: you have entered "{guess}".')
                print("Please enter a letter "
                      f"or a word containing {len(word)} letters." +
                      styles.END)
            elif len(guess) == len(word) and guess.isalpha():
                if guess in suggested_words:
                    print(styles.YELLOWBOLD +
                          f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)
                elif guess != word:
                    suggested_words.append(guess)
                    print(styles.BOLD +
                          f'Sorry, "{guess}" is not the word.\n' + styles.END)
                    number_of_lives -= 1
                else:
                    word_to_guess = word
                    break
            elif len(guess) > 1 and guess.isalpha():
                print(styles.YELLOWBOLD +
                      f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter "
                      f"or a word containing {len(word)} letters." +
                      styles.END)
            elif len(guess) == 1 and guess.isalpha():
                if guess in suggested_letters:
                    print(styles.YELLOWBOLD +
                          f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)
                elif guess not in word:
                    number_of_lives -= 1
                    suggested_letters.append(guess)
                    print(styles.BOLD +
                          f'Sorry, "{guess}" is not in the word.' + styles.END)
                    if number_of_lives > 0:
                        print(f"You have {number_of_lives} live(s) left.")
                else:
                    suggested_letters.append(guess)
                    print(styles.GREENBOLD +
                          f'Great! "{guess}" is in the word!')
                    print("Well done!" + styles.END)
                    # Code to display correctly guessed letters:
                    # https://www.youtube.com/watch?v=m4nEnsavl6w
                    word_as_list = list(word_to_guess)
                    indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_to_guess = "".join(word_as_list)
                    # End of code from the above source
                    if "_" not in word_to_guess:
                        break
        except ValueError as error:
            print(styles.YELLOWBOLD +
                  f"Invalid data: {error}, please try again.\n" + styles.END)
            continue

        if len(suggested_letters) <= 1 and number_of_lives > 0:
            print(styles.CYANBOLD + "\nThe word to guess: " + styles.END +
                  word_to_guess)
            print()
        elif number_of_lives > 0:
            print(styles.CYANBOLD + "\nThe word to guess: " + styles.END +
                  word_to_guess)
            print("Letters already tried: ", sorted(suggested_letters))

        draw_snowman(number_of_lives)

    if word_to_guess == word:
        clear_terminal()
        print(ascii_art.WIN)
        print(styles.BOLD + "\nCongratulations! " + styles.GREEN +
              f"{word}" + styles.END + styles.BOLD +
              " was the correct answer!\n" + styles.END)
    else:
        clear_terminal()
        print(ascii_art.LOSE)
        print(styles.BOLD + "\nGood effort! The correct word was " +
              styles.YELLOW + f"{word}" + styles.END + styles.BOLD +
              ".\n" + styles.END)
        print("Thank you for playing the Melting Snowman game!\n")

    restart_game()


def main():
    """
    Calls the main functions to run the game.
    """
    lives = set_number_of_lives()
    random_word = get_random_word()
    play_game(random_word, lives)


welcome_page()
