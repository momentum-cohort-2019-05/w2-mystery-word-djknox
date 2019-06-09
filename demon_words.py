# import random module for randomly selecting a word length
import random

# import get_terminal_size function from os to center console output
from os import get_terminal_size

# import reusable functions from mystery word game
from mystery_word import print_difficulty_setting_instructions, ask_user_for_difficulty_setting, load_words, group_words_by_difficulty, choose_list_of_words_based_on_difficulty_setting, ask_user_to_guess_a_letter, play_round_of_game

# In Evil Hangman, the computer maintains a list of every word in the English language, then continuously pares down the word list to try to dodge the player's guesses as much as possible.
# The computer begins by maintaining a list of all words in the English language of a particular length.
# Whenever the player guesses, the computer partitions the words into "word families" based on the positions of the guessed letters in the words.
# Once the words are partitioned into equivalence classes, the computer can pick the largest of these classes to use as its remaining word list.
# It then reveals the letters in the positions indicated by the word family.
def evil_algorithm(word_list):
    """
    Given a list of words, continuously pare down the list of words into groups based on user letter guesses.
    Groups are based on the position/index of the guessed letter in the words and only the largest group of words will remain for subsequent guesses.
    When the list of words has been pared down to a single word, return that word.
    Return a list of the user's guesses.
    """
    guesses = []
    while len(word_list) > 0:
        if len(word_list) == 1:
            return word_list[0], guesses

        # ask user to guess a letter
        guess = ask_user_to_guess_a_letter()
        guesses.append(guess)

        # loop through each word and create word families based on where the guessed letter exists in the word
        # word_families = {
        #     0: ['art'],                           --> 'a' is in first index
        #     1: ['bars', 'cat', 'tart', 'bat'],    --> 'a' is in second index
        #     2: ['crab']                           --> 'a' is in third index
        # }
        word_families = {}
        for word in word_list:
            for i in range(0, len(word)):
                if guess == word[i]:
                    if i in word_families.keys():
                        word_families[i].append(word)
                    else:
                        word_families[i] = [word]

        # loop through word_families and pick the largest family as new word list
        word_list_lengths = []
        for key in word_families:
            word_list_lengths.append(len(word_families[key]))

        for word_family in word_families.values():
            if len(word_family) == max(word_list_lengths):
                word_list = word_family
        



if __name__ == "__main__":
    replay_game = True
    while replay_game:
        # print centered greeting and difficulty settings to user
        print(f"{'Welcome to the Mystery Word game!':^{get_terminal_size().columns}}")
        print_difficulty_setting_instructions()

        # ask user for difficulty setting or to quit game
        option = ask_user_for_difficulty_setting()

        # exit the loop if user selects 'x'
        if option == 'x':
            print(f"{'Quitting game!':^{get_terminal_size().columns}}")
            break
        
        # load the words from the text file
        words = load_words()

        # sort the words based on their difficulty
        words_grouped_by_difficulty = group_words_by_difficulty(words)

        # take the user's choice of difficulty and choose a list based on the user's option
        chosen_list = choose_list_of_words_based_on_difficulty_setting(words_grouped_by_difficulty, option)

        # take random word length (within the chosen difficulty) and create new list of words with only those lengths
        lengths_of_words_in_chosen_list = [len(word) for word in chosen_list]
        random_word_length = random.choice(lengths_of_words_in_chosen_list)
        chosen_list = [word for word in chosen_list if len(word) == random_word_length]

        # lie to user and tell them a word has been chosen, but be truthful about length of word that will eventually be chosen
        word_length_message = f"The chosen word has {random_word_length} letters."
        print(f"{word_length_message:^{get_terminal_size().columns}}")

        # take the chosen_list and feed into evil algorithm to get word to play with
        # get the user's guesses from the evil algorithm round of guessing
        chosen_word, guesses = evil_algorithm(chosen_list)

        # after evil algorithm chooses a final word, play game normally with variables updated after evil round
        # in order to make letter casing not matter, make chosen_word lowercase
        # will also make all inputted guesses lowercase and check against chosen_word_lowercase
        chosen_word_lowercase = chosen_word.lower()

        # A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
        # initialize the game variables
        num_guesses_allowed = 8
        num_guesses = len(guesses)
        guesses = guesses
        letters_left_to_guess = [letter for letter in list(chosen_word_lowercase) if letter not in guesses]

        # The game should end when the user constructs the full word or runs out of guesses.
        while num_guesses < num_guesses_allowed and len(letters_left_to_guess) > 0:
            # play a round of the game and update variables each time
            num_guesses, guesses, letters_left_to_guess = play_round_of_game(num_guesses, num_guesses_allowed, guesses, letters_left_to_guess, chosen_word_lowercase)

        # If the player runs out of guesses, reveal the word to the user when the game ends.
        if len(letters_left_to_guess) == 0:
            print(f"{'You won!':^{get_terminal_size().columns}}")
        else:
            print(f"{'You lost!':^{get_terminal_size().columns}}")

        chosen_word_message = f"The word was {chosen_word}!"
        print(f"{chosen_word_message:^{get_terminal_size().columns}}")

        # When a game ends, ask the user if they want to play again. The game begins again if they reply positively.
        print("Enter '1' to play again and anything else to quit the game.")
        does_user_want_to_play_again = input("Play again? ")
        if does_user_want_to_play_again == '1':
            print("Let's play again!")
        else:
            print(f"{'Thanks for playing!':^{get_terminal_size().columns}}")
            replay_game = False

# TODO:
# while in evil mode guessing rounds:
# figure out way to display partially guessed "word" each time
# since the word changes with each round, display the correctly guessed letters in their proper indices
# display "_" for the remaining indices