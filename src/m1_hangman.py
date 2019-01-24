"""
Hangman.

Authors: Margaret Luffman and Emily Guajardo.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random



def main():
    # what_length()
    # get_guess()
    # check_guess()
    # guess_boolean()
    # guess_cycle()
    word_seq()

def choose_word():
    with open("words.txt") as f:
        f.readline()
        string = f.read()
        words = string.split()
        n = random.randrange(0,len(words))
        return words[n]

def what_length():
    length = int(input("What is the minimum length you would like?"))
    word = choose_word()
    while True:
        if len(word) > length:
            # print(word)
            return word
        else:
            word = choose_word()

def get_guess():
    guess = str(input('Guess a letter: '))
    print(guess)
    return guess

def check_guess(word):
    count = 0
    correct = False
    while count < len(word):
        guess = get_guess()
        for k in range(len(word)):
            if word[k] is guess:
                correct = True
        break
    return correct,guess

def guess_boolean():
    word = what_length()
    #for k in range(len(word)):
    ans, guess = check_guess(word)
    print(ans)
    if ans == True:
        print('Correct!, your guess is in the word!')
    else:
        print('Incorrect, your guess is not in the word.')
    return word, guess

def word_seq():
    seen_word = []
    word, guess = guess_boolean()
    for k in range(len(word)):
        seen_word = seen_word + ['-']
    for j in range(len(word)):
        for k in range(len(word)):
            if word[k] is guess:
                seen_word[k] = guess
    print(seen_word)


main()