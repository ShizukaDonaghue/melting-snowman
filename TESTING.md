# Testing for Melting Snowman

Return to [README](https://github.com/ShizukaDonaghue/melting-snowman/blob/main/README.md)

## Code Validation
The application has been fully validated to ensure there were no syntax errors. [CI Python Linter](https://pep8ci.herokuapp.com/) was used for the validation and no errors were found.

<details>
  <summary>Validation Results for run.py</summary>

  <img src="docs/python-linter-run.png" width="800">
</details>

<details>
  <summary>Validation Results for snowman.py</summary>

  <img src="docs/python-linter-snowman.png" width="800">
</details>

<details>
  <summary>Validation Results for ascii_art.py</summary>

  <img src="docs/python-linter-ascii-art.png" width="800">
</details>

<details>
  <summary>Validation Results for words.py</summary>

  <img src="docs/python-linter-words.png" width="800">
</details>

<details>
  <summary>Validation Results for font_styles.py</summary>

  <img src="docs/python-linter-font-styles.png" width="800">
</details>


## Manual Testing
Manual testing was conducted on the following elements in the game to verify that all the features functioned as expected and no issues were found.

### Welcome Screen
 | Step | Description        | Expected Result | Actual Result | Pass/Fail |
 |------|--------------------|-----------------|---------------|-----------|
 | 1    | Deployed Website   | Welcome Screen loads without any issues | Welcome Screen loaded as expected  | Pass |
 |2 | The Title of the Game  | The title of the game is displayed with ASCII art | ASCII art loaded as expected | Pass |
| 3 | Font Styles | The font styles are displayed correctly | The font styles displayed as expected | Pass |
 4 | Player Input      | Once the player presses ENTER, the terminal is cleared and the Rules Screen is displayed | The terminal cleared and the Rules displayed as expected | Pass|

### Rules Screen
| Step | Description        | Expected Result | Actual Result | Pass/Fail |
|------|--------------------|-----------------|---------------|-----------|                
| 1 | Rules Screen | Rules Screen loads without any issues | Rules Screen loaded as expected | pass |
| 2 | The Title of the Page | The title of the page is displayed with ASCII art | ASCII art loaded as expected | Pass |
| 3 | Font Styles | The font styles are displayed correctly | The font styles displayed as expected | Pass |
| 4 | Player Input | Only "6", "8" or "10" are accepted | Input validated as expected | Pass |
| 5 | Player Input | If the input is invalid, displays an error message | Error message displayed as expected | Pass |
| 6 | Player Input | Continues to request an input until a valid input is provided | Loop functioned as expected | Pass |
| 7 | Player Input | Once the player enters a valid input, the terminal is cleared and the Game Screen is displayed | The terminal cleared and the Game Screen displayed as expected | Pass |

The GIF image below shows the input validation. If the input from the player is invalid, the error message is displayed in yellow and the player is asked to select the number of lives until a valid input is provided.  
Please click on the image to watch the GIF as auto looping is turned off to minimise distraction.   

<img src="docs/rules-user-input-validation.gif" width="700">

### Game Screen
| Step | Description        | Expected Result | Actual Result | Pass/Fail |
|------|--------------------|-----------------|---------------|-----------|  
| 1 | Game Screen | Game Screen loads without any issues | Game Screen loaded as expected | Pass |
| 2 | Font Styles | The font styles are displayed correctly | The font styles displayed as expected | Pass |
| 3 | The Number of Letters in the Word | In the first screen, the number of letters in the word is displayed | The number of letters displayed as expected | Pass |
| 4 | Initial Snowman Drawing | Snowman ASCII art is displayed based on the number of lives selected | Snowman displayed as expected | Pass | 
| 5 | Player Input | If the input is not in the alphabet, displays an error message | Error message displayed as expected | Pass |
| 6 | Player Input | If the input contains the same number of letters as the word to be guessed, checks if the word has been tried already and if it is, gives feedback | If the input was already tried, gave an error message as expected | Pass |
| 7 | Player Input | If the input contains the same number of letters as the word to be guessed and not tried already, checks if it is the correct word and gives feedback | Feedback on whether the input was correct displayed as expected | Pass |
| 8 | Player Input | If the word suggested is correct, the game finishes and the player is brought to the correct End of Game Screen with the "Snowman Saved!" message. If not, the player loses a life and the suggested word is stored to check against future tries and moves on to the next try. If they have no life left, they are brought to the correct End of Game Screen with the "Game Over" message. | If the word suggested was correct, the game finished and the correct End of Game Screen displayed as expected. If the word suggested was incorrect, the player lost a life as expected and moved on to the next try if they had lives left | Pass |
| 9 | Snowman Drawing | If the word suggested is incorrect and the player loses a life but has more lives left, the snowman ASCII art changes based on the number of remaining lives | Snowman drawing changed as expected | Pass |
| 10 | Player Input | If the input contains more than one letter, but not the same length as the word to be guessed, displays an error message | Error message displayed as expected | Pass |
| 11 | Player Input | If the input contains one letter, checks if the input has been tried already and if it is, gives feedback | If the input was already tried, gave an error message as expected | Pass |
| 12 | Player Input | If the input contains one letter and not tried already, checks if it is in the word to be guessed and gives feedback | Feedback on whether the input was in the word displayed as expected | Pass |
| 13 | Word to guess field | If the input is in the word and the word is not guessed yet, displays the letter in the "Word to guess" field and moves on to the next try. If not, the player loses a life and the letter suggested is stored to check against future tries and moves on to the next try. If they have no life left, they are brought to the correct End of Game Screen with the "Game Over" message | If the letter was correct, the letter displayed in the field as expected and moved on to the next try, if not, the player lost a life as expected and moved on to the next try if they had lives left | Pass |
| 14 | Snowman Drawing | If the letter is incorrect and the player loses a life but has more lives left, the snowman ASCII art changes based on the number of remaining lives | Snowman drawing changed as expected | Pass |
| 15 | The Number of Lives Left | If the letter or word suggested is incorrect, reduces the number of lives by one and displays the remaining number of lives if they have more left. If the player has no more lives left, the game finishes. | The number of lives displayed as expected unless the player had no lives left | Pass |
| 16 | Letters Already Tried | The letters already tried are stored and alphabetically displayed if there are more than one | Letters tried were displayed as expected | Pass |
| 17 | Loop | The game continues the same sequence until the word is guessed correctly or the player has no more lives left | Loop functioned as expected | Pass |
| 18 | Clear Terminal | The terminal is cleared for each try | The terminal cleared as expected | Pass | 

The GIF image below shows the input validation. If the input from the player is invalid, the error message is displayed in yellow and the player is asked to suggest a letter or a word containing the same number of letters as the word to be guessed until a valid input is provided.  
Please click on the image to watch the GIF as auto looping is turned off to minimise distraction.  

<img src="docs/game-input-validation.gif" width="700">

### End of Game Screen
| Step | Description        | Expected Result | Actual Result | Pass/Fail |
|------|--------------------|-----------------|---------------|-----------|  
| 1 | End of Game Screen | End of Game Screen loads without any issues | End of Game Screen loaded as expected | Pass |
| 2 | The Title of the Page | The title of the page is displayed with ASCII art in both "Snowman Saved!" and "Game Over" screens | ASCII art loaded in both screens as expected | Pass |
| 3 | Font Styles | The font styles are displayed correctly | The font styles displayed as expected | Pass |
| 4 | The Correct Word | The correct word is displayed and if the player has won, it is in green and if not, it is in yellow | The correct word displayed as expected | Pass |
| 5 | Play Again | The play again message is displayed in both screens | The message is displayed in both screens as expected | Pass |
| 6 | Player Input | Only "Y" or "N" is accepted | Input validated as expected | Pass |
| 7 | Player Input | If the input is invalid, displays an error message | Error message displayed as expected | Pass |
| 8 | Player Input | Continues to request an input until a valid input is provided | Loop functioned as expected | Pass |
| 9 | Player Input | Once the player enters a valid input, the terminal is cleared and if "Y" is selected, the player is asked to select the number of lives to start another game, or otherwise the player is brought to the Welcome Screen | The terminal cleared and the player was brought to the correct screens as expected | Pass |

The GIF image below shows the input validation. If the input from the player is invalid, the error message is displayed in yellow and the player is asked to select either "Y" or "N" until a valid input is provided.  
Please click on the image to watch the GIF as auto looping is turned off to minimise distraction.  

<img src="docs/end-of-game-input-validation.gif" width="700">

## User Stories Testing
User stories were tested and addressed as follows:
  
*I would like to understand how to play the game with ease.*    
 * The Rules Screen explains the rule clearly, including what inputs are expected.  
    <details>
      <summary>Supporting image</summary>
      <img src="docs/rules.png" width="700">
    </details>

*I would like to be able to set the difficulty to suit my level.*  
 * The player can select the number of lives from "6", "8" or "10" to adjust the difficulty from the Rules Screen above.

*I would like feedback on each guess while playing the game.*  
 * Each valid input is checked to see if it is in the word or is the actual word and feedback is given.   
    If the input is correct, the message is shown in green.
    <details>
      <summary>Supporting image</summary>
      <img src="docs/correct-guess-testing.png" width="700">
    </details>    
    If the input is incorrect, the feedback is displayed as well as the number of lives left.    
    <details>
      <summary>Supporting image</summary>
      <img src="docs/wrong-guess.png" width="700">
    </details>
 
*I would like to see an error message if my guess is invalid and understand why.*  
 * If the input is invalid, an error message is displayed so that the player knows what input is expected. This is also explained in the Game Screen section with the GIF image.
    <details>
      <summary>Supporting image</summary>
      <img src="docs/error-message.png" width="700">
    </details>

*I would like to see the letters already tried so that I would not suggest the same again.*  
 * The letters already tried are displayed from the second try, so the player can keep track of them. 
    <details>
      <summary>Supporting image</summary>
      <img src="docs/already-tried.png" width="700">
    </details>

*I would like to know the progress of the game while playing the game.*  
 * The "Word to guess" field reveals the letters once they have been guessed correctly and displays the remaining to be guessed with underscores. If the input from the player is incorrect, the number of lives remaining is displayed so that the player can keep track of the progress.
    <details>
      <summary>Supporting image</summary>
      <img src="docs/game-progress.png" width="700">
    </details>

*I would like to have the option to play again or finish the game after each game.*  
 * When the game finishes, the player is asked if they would like to play another game or finish the game regardless of whether the player has succeeded in saving the snowman.
    <details>
      <summary>Supporting image</summary>
      <img src="docs/player-win.png" width="700">
    </details>


## Resolved Bug
When font styles were added to `word_to_guess` variable, underscores for the letters which were yet to be guessed did not print in the terminal of the deployed website. The issue was not seen in Gitpod. Various methods were tested and found that the underscores did not print in the deployed website if the font style was bold unless a background colour was added.

The image below shows how `word_to_guess` variable was printed in Gitpod. Underscores were printed in all font styles:  

<img src="docs/print-statements-gitpod.png">

The image below shows how `word_to_guess` variable was printed in the terminal of the deployed website using the same codes (but a different word as the word was randomly chosen). Underscores did not print if the font style was bold, or if it is bold, a background colour needed to be added for the underscores to print in the deployed website:  

<img src="docs/print-statements-deployed-site.png">

Since coloured letters are difficult to read without bold font style in the terminal of the deployed website, font styles have been removed from the variable so that the underscores are printed clearly in white for the letters which are yet to be guessed.

## Unresolved Bug
`os.system("cls" if os.name == "nt" else "clear")` is used to clear the terminal for new contents during the game. However, this only clears the contents that are visible in the terminal of the deployed website and if there are any contents above that, they can still be seen when scrolled up after the terminal has been cleared. This issue is not seen in Gitpod. 

The GIF image below shows the visible area of the terminal in the deployed website is cleared for new contents (in this case, the "Game Over" message), but the contents above the visible area can still be seen when scrolled up. Please click on the image to watch the GIF as auto looping is turned off to minimise distraction.   

<img src="docs/clear-terminal-bug.gif" width="700">

Methods tried to fix this issue:
1. `import subprocess` `subprocess.call('reset')`  
    This is to clear history and it works as expected in Gitpod, however, it actually did not clear the terminal of the deployed website.
2. `print("\n" * 150)` 
    This does clear the terminal in Gitpod, but it still did not clear the terminal of the deployed website. This method was also tried with `os.system("cls" if os.name == "nt" else "clear")`, however, it still did not clear the contents above the visible area of the terminal in the deployed website. 

While this issue was not resolved, it should not affect the user experience during the game as the visible area of the terminal is cleared for new contents, which still provides a cleaner and more pleasant experience for the player.


Return to [README](https://github.com/ShizukaDonaghue/melting-snowman/blob/main/README.md)