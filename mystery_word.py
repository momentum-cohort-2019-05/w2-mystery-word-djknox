# import random module for randomly selecting a word
import random

# import dedent function from textwrap module to fix indentation of multi-line strings
from textwrap import dedent

def print_difficulty_setting_instructions():
    """
    Print the difficulty setting instructions to the user.
    """
    difficulty_setting_instructions = """
    Select a difficulty mode by entering one of the following numbers:

    1 - easy (words with 4-6 characters)
    2 - normal (words with 6-8 characters)
    3 - difficult (words with 8+ characters)

    or enter "x" to quit the game.
    """
    difficulty_setting_instructions = dedent(difficulty_setting_instructions)
    print(difficulty_setting_instructions)

def ask_user_for_difficulty_setting():
    """
    Ask the user to input a difficulty setting or to quit the game and return their choice as a string.
    Continue to ask the user to input a setting until they have entered one of the valid options.
    """
    valid_option = False
    while not valid_option:
        option = input("Choose an option: ").lower()
        if option not in ['1', '2', '3', 'x']:
            print("\nThat wasn't an option! Please try again.")
            print_difficulty_setting_instructions()
        else:
            valid_option = True

    return option

def load_words():
    """
    Load each line from words.txt as an element in a list and return
    """
    words = []
    with open("words.txt", mode="r") as file:
        for line in file.readlines():
            line = line.strip()
            words.append(line)
    return words

def group_words_by_difficulty(a_list_of_words):
    """
    Given a list of words, group the words based on length and return a dictionary of the groups.
        easy: 4-6 characters
        normal: 6-8 characters
        difficult: 8+ characters
    """
    easy_list = [word for word in a_list_of_words if len(word) >= 4 and len(word) <= 6]
    normal_list = [word for word in a_list_of_words if len(word) >= 6 and len(word) <= 8]
    difficult_list = [word for word in a_list_of_words if len(word) >= 8]
    
    return {
        'easy': easy_list,
        'normal': normal_list,
        'difficult': difficult_list
    }

def choose_list_of_words_based_on_difficulty_setting(words_grouped_by_difficulty, difficulty_option):
    """
    Given a user's option for a difficulty setting and a dictionary of words grouped by their difficulty setting, return the chosen list of words.
    """
    if difficulty_option == '1':
        chosen_list = words_grouped_by_difficulty['easy']
    elif difficulty_option == '2':
        chosen_list = words_grouped_by_difficulty['normal']
    elif difficulty_option == '3':
        chosen_list = words_grouped_by_difficulty['difficult']
    
    return chosen_list

def display_num_guesses_remaining(num_guesses_allowed, num_guesses):
    """
    Given an integer for the number of guesses allowed and an integer for the number of guesses made, print out a string telling the user how many guesses they have remaining.
    """
    num_guesses_remaining = num_guesses_allowed - num_guesses
    if num_guesses_remaining > 1:
        print(f"You have {num_guesses_remaining} guesses left.")
    elif num_guesses_remaining == 1:
        print(f"You have {num_guesses_remaining} guess left!")

if __name__ == "__main__":
    replay_game = True
    while replay_game:
        # print greeting and difficulty settings to user
        print('Welcome to the Mystery Word game!')
        print_difficulty_setting_instructions()

        # ask user for difficulty setting or to quit game
        option = ask_user_for_difficulty_setting()

        # exit the loop of user selects 'x'
        if option == 'x':
            print("Quitting game!")
            break

        # load the words from the text file
        words = load_words()

        # sort the words based on their difficulty
        words_grouped_by_difficulty = group_words_by_difficulty(words)
        
        # take the user's choice of difficulty and choose a list based on the user's option
        chosen_list = choose_list_of_words_based_on_difficulty_setting(words_grouped_by_difficulty, option)

        # choose a random word from the chosen list and tell the user its length
        chosen_word = random.choice(chosen_list)
        print(f"The chosen word has {len(chosen_word)} letters.")

        # in order to make letter casing not matter, make chosen_word lowercase
        # will also make all inputted guesses lowercase and check against chosen_word_lowercase
        chosen_word_lowercase = chosen_word.lower()

        # A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
        num_guesses_allowed = 8
        num_guesses = 0
        guesses = []
        letters_left_to_guess = list(chosen_word_lowercase)

        # The game should end when the user constructs the full word or runs out of guesses.
        while num_guesses < num_guesses_allowed and len(letters_left_to_guess) > 0:

            # Display the partially guessed word, as well as letters that have not been guessed.
            print([letter if letter in guesses else "_" for letter in chosen_word_lowercase])

            # Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
            valid_input = False
            while not valid_input:
                # ask user to guess a letter and immediately make their guess lowercase
                guess = input("Guess a letter! ").lower()
                # if guess is more than one letter or not a letter
                if len(guess) > 1 or not guess.isalpha():
                    print("Input invalid. Guess again.")
                else:
                    valid_input = True

            # Let the user know if their guess appears in the computer's word.
            # A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.
            # If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.
            if guess in guesses:
                print("You've already guessed that letter!")
            elif guess in chosen_word_lowercase:
                print("That letter is in the word!")
                # add guess to guesses
                guesses.append(guess)
                # remove all occurrences of correct guess from letters_left_to_guess
                letters_left_to_guess = [letter for letter in letters_left_to_guess if letter != guess]
            elif guess not in chosen_word_lowercase:
                print("That letter is not in the word!")
                num_guesses += 1
                guesses.append(guess)
            
            # tell the user how many guesses they have left
            display_num_guesses_remaining(num_guesses_allowed, num_guesses)
        
        # If the player runs out of guesses, reveal the word to the user when the game ends.
        if len(letters_left_to_guess) == 0:
            print("You won!")
        else:
            print("You lost!")

        print(f"The word was {chosen_word}!")

        # When a game ends, ask the user if they want to play again. The game begins again if they reply positively.
        print("Enter '1' to play again and anything else to quit the game.")
        does_user_want_to_play_again = input("Play again? ")
        if does_user_want_to_play_again == '1':
            print("Let's play again!")
        else:
            print("Thanks for playing!")
            replay_game = False

# TODO (for fun)
# show the user a list of the letters they have already guessed
# format console output so that game is more easily read on the screen (add spacing/line breaks)