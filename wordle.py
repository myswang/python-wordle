import os
import random

# definition of colour escape sequences
GREEN_LETTER = "\033[1;42m"
YELLOW_LETTER = "\033[1;43m"
GREY_LETTER = "\033[1;49m"
STOP = "\033[0m"

MAX_GUESSES = 6

# evaluates the "correctness" of word against the answer.
# returns the coloured matches of the word (green/yellow/grey)
def evaluate(word, answer):
    duplicates = {}
    score = [""] * len(word)
    # find exact matches (green)
    for i, letter in enumerate(word):
        if letter == answer[i]:
            score[i] = f"{GREEN_LETTER} {letter} "
            duplicates.setdefault(letter, 0)
            duplicates[letter] += 1

    # find partial matches (yellow)
    for i, letter in enumerate(word):
        if GREEN_LETTER in score[i]: # skip exact matches
            continue
        duplicates.setdefault(letter, 0)
        duplicates[letter] += 1
        # if there are duplicates, only accept some of them
        if letter in answer and duplicates[letter] <= answer.count(letter):
            score[i] = f"{YELLOW_LETTER} {letter} "
        else:
            score[i] = f"{GREY_LETTER} {letter} "
    
    return "".join(score) + STOP

# clear the screen to begin drawing a new frame
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("python-wordle by Mike Wang")
    print("==========================")

# read words file into a set
def read_words_file(fname):
    with open(fname, "r") as f:
        return set([word.upper() for word in f.read().splitlines()])

if __name__ == '__main__':
    # read word dataset (singular only) into a set and pick a random answer
    words_singular = read_words_file("sgb-words-singular.txt")
    answer = random.choice(tuple(words_singular))
    # read (full) word dataset for guesses
    words = read_words_file("sgb-words.txt")
        
    num_guesses = 1
    history = ""
    # loop until we run out of guesses
    while num_guesses <= MAX_GUESSES:
        clear_screen()
        info_str = f"Guess {num_guesses}/{MAX_GUESSES}"
        print(info_str)
        print(history, end="\r")
        guess = input("Input: ").upper()
        # check if word is valid
        if guess not in words:
            continue
        # evaluate the guess (green/yellow/grey)
        history += evaluate(guess, answer) + "\n"
        if guess == answer:
            break
        num_guesses += 1

    clear_screen()
    if num_guesses > MAX_GUESSES:
        print(f"Game over! The answer was: {answer}")
    else:
        print(f"Congrats! You guessed it in {num_guesses} tries.")
    print(history, end="\r")

