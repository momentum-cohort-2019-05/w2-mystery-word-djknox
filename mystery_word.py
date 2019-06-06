# import random library for randomly selecting a word
import random

# load words from words.txt
# return a list of the words
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

# separate words from words.txt into three separate lists based on word length:
# 4-6chars, 6-8chars, and 8+chars
# return a dictionary of the three difficulties and their corresponding lists
def sort_words_by_difficulty(a_list_of_words):
    """
    Given a list of words, group the words based on length and return a dictionary of the groups.
        easy: 4-5 characters
        normal: 6-8 characters
        difficult: >8 characters
    """
    easy_list = [word for word in a_list_of_words if len(word) >= 4 and len(word) < 6]
    normal_list = [word for word in a_list_of_words if len(word) >= 6 and len(word) <= 8]
    difficult_list = [word for word in a_list_of_words if len(word) > 8]
    
    return {
        'easy': easy_list,
        'normal': normal_list,
        'difficult': difficult_list
    }

if __name__ == "__main__":
    while True:
        print("""Welcome to the game of Mystery Word!

Select a difficulty mode by entering one of the following numbers:
1 - easy (words with 4-6 characters)
2 - normal (words with 6-8 characters)
3 - difficult (words with 8+ characters)

or enter "x" to quit the game.""")

        option = input("Choose an option: ")

        # load the words from the text file
        words = load_words()
        # sort the words based on their difficulty
        words_sorted_by_difficulty = sort_words_by_difficulty(words)
        # take the user's choice of difficulty and choose a list
        if option == '1':
            chosen_list = words_sorted_by_difficulty['easy']
        elif option == '2':
            chosen_list = words_sorted_by_difficulty['normal']
        elif option == '3':
            chosen_list = words_sorted_by_difficulty['difficult']
        elif option == 'X' or option == 'x':
            break
        else:
            print("\nthat wasn't an option!\n")

        # choose a random word from the chosen list and tell the user its length
        chosen_word = random.choice(chosen_list)
        print(f"The chosen word has {len(chosen_word)} letters.")

        # Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
        valid_input = False
        while not valid_input:
            guess = input("Guess a letter! ")
            # if guess is more than one letter or not a letter
            if len(guess) > 1 or not guess.isalpha():
                print("Input invalid. Guess again.")
            else:
                valid_input = True

        # Let the user know if their guess appears in the computer's word.
        if guess in chosen_word:
            print("That letter is in the word!")
        else:
            print("That letter is not in the word!")
        
