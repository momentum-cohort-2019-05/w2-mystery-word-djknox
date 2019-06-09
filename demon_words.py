# In Evil Hangman, the computer maintains a list of every word in the English language, then continuously pares down the word list to try to dodge the player's guesses as much as possible.
# The computer begins by maintaining a list of all words in the English language of a particular length.
# Whenever the player guesses, the computer partitions the words into "word families" based on the positions of the guessed letters in the words.
# Once the words are partitioned into equivalence classes, the computer can pick the largest of these classes to use as its remaining word list.
# It then reveals the letters in the positions indicated by the word family.


# user guesses a letter
# loop through each word and create word families based on where the guessed letter exists in the word
# word_families = {
#     0: ['art'],
#     1: ['bars', 'cat', 'tart', 'bat'],
#     2: ['crab']
# }
word_list = ['art', 'bars', 'cat', 'crab', 'tart', 'bat', 'touch', 'match', 'matches']

while len(word_list) > 0:
    if len(word_list) == 1:
        # play normal game with new word
        print("now play normal game with", word_list[0])
        break

    # ask user for guess
    guess = input("Guess a letter: ")

    # create word families based on guess
    word_families = {}
    for word in word_list:
        for i in range(0, len(word)):
            if guess == word[i]:
                if i in word_families.keys():
                    word_families[i].append(word)
                else:
                    word_families[i] = [word]

    print(f"Word Families created: {word_families}")

    # loop through word_families and pick the largest family as new word list
    # loop through each key in word_families
    # get the number of elements in the key's value
    # return the key with the most elements in its value
    # return the value with the max number of elements
    word_list_lengths = []
    for key in word_families:
        word_list_lengths.append(len(word_families[key]))

    for word_family in word_families.values():
        if len(word_family) == max(word_list_lengths):
            word_list = word_family

    print(f"New Word list: {word_list}")



