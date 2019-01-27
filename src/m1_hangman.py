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
    while True:
        ans = int(input("Would you like to play a game of hangman? "
                "Please Type 1 for yes or anything other number for no."))
        if ans == 1:
            guess_boolean()
        else:
            print("Goodbye! Thanks for playing!")
            break
    # guess_cycle()
    #word_seq()

def choose_word():
    with open("words.txt") as f:
        f.readline()
        string = f.read()
        words = string.split()
        n = random.randrange(0,len(words))
        return words[n]

def what_length():
    length = int(input("What is the minimum length you would like?"))
    chances = int(input("How many guesses would you like?"))
    word = choose_word()
    while True:
        if len(word) > length:
            # print(word)
            return word, chances
        else:
            word = choose_word()

def get_guess():
    guess = str(input('Guess a letter: '))
    #print(guess)
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
    word, chances = what_length()
    # for k in range(len(word)):
    ans, guess = check_guess(word)
    print(ans)
    seen_word = []
    for k in range(len(word)):
        seen_word = seen_word + ['-']
    stop_boolean = True
    while stop_boolean is True:
        if ans == True:
            print('Correct!, your guess is in the word!')
            print("You have", chances,"lives left")
        else:
            print('Incorrect, your guess is not in the word.')
            chances = chances - 1
            if chances == 0:
                print("You Lose, Too Bad")
                break
            print("You have", chances,"lives left")

        for j in range(len(word)):
            for k in range(len(word)):
                if word[k] is guess:
                    seen_word[k] = guess
        print(seen_word)
        count = 0
        for k in range(len(seen_word)):
            if seen_word[k] == '-':
                count += 1
        if count == 0:
                break
        else:
            ans, guess = check_guess(word)


main()