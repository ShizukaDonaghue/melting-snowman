# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import winter_words
# from snowman import draw_snoman


def game_introduction():
    """
    Displays game introduction and rules.
    """
    print("Welcome to the Melting Snowman game!\n")
    print("This is a word guessing game.")
    print("Suggest a letter at a time to guess the word.")
    print("You can also suggest a word if you think you've figured it out!\n")
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
        choice = input('Enter "7" for 7 lives or "10" for 10 lives: ')
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


def play_game(word, number_of_lives):
    """
    Plays the game. EXPLAIN MORE HERE!!!
    """
    failed_attempts = 0
    suggested_letters = []
    suggested_words = []
    word_to_guess = "_" * len(word)
    print("Let's play the Melting Snowman game!")
    print(f"The word to guess has {len(word)} letters. Best of luck!")
    while number_of_lives > 0:
        guess = input("Please enter a letter or word: ").upper()
        try:
            if not guess.isalpha():
                print(f'You have entered "{guess}".')
                print("Please enter a letter", end=" ")
                print(f"or a word containing {len(word)} letters.")
            elif len(guess) == len(word) and guess.isalpha():
                if guess in suggested_words:
                    print(f'You have already entered "{guess}".')
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
                print("Please enter one letter at a time", end=" ")
                print(f"or a word containing {len(word)} letters.")
            elif len(guess) == 1 and guess.isalpha():
                if guess in suggested_letters:
                    print(f'You have already entered "{guess}".')
                    print("Please try again!")
                elif guess not in word:
                    number_of_lives -= 1
                    failed_attempts += 1
                    suggested_letters.append(guess)
                    print(f'"{guess}" is not in the word.')
                    print(f"You have {number_of_lives} live(s) left.")
                else:
                    suggested_letters.append(guess)
                    print(f'Great! "{guess}" is in the word! Well done!')
                    # Code to display correctly guessed letters
                    # from https://www.youtube.com/watch?v=m4nEnsavl6w
                    word_as_list = list(word_to_guess)
                    indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_to_guess = "".join(word_as_list)
                    if "_" not in word_to_guess:
                        break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue

        if number_of_lives > 0:
            print("The word to guess: ", word_to_guess)
        if len(suggested_letters) > 1:
            print("Letters already entered: ", sorted(suggested_letters))

    if word_to_guess == word:
        print(f"Congratulations! {word} was the correct answer!")
    else:
        print(f"Good effort! The correct word was {word}.")
        print("Let's play again!")


def main():
    """
    Calls the main functions to run the game.
    """
    set_number_of_lives()
    get_random_word()

    random_word = get_random_word()
    lives = set_number_of_lives()
    play_game(random_word, lives)
    while input("Would you like to play again? (Y/N): ").upper() == "Y":
        set_number_of_lives()
        get_random_word()

        random_word = get_random_word()
        lives = set_number_of_lives()
        play_game(random_word, lives)




game_introduction()
