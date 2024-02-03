from random import randint
import os

# definition of colour escape sequences
GREEN_LETTER = "\033[1;42m"
YELLOW_LETTER = "\033[1;43m"
GREY_LETTER = "\033[1;49m"
STOP = "\033[0m"

MAX_GUESSES = 6

# calculates the "correctness" of word, prints the coloured result to console
def evaluate(word):
    duplicates = {}
    score = [""] * 5
    for i in range(5):
        letter = word[i]
        if letter == answer[i]:
            score[i] = f"{GREEN_LETTER} {letter} "
            duplicates.setdefault(letter, 0)
            duplicates[letter] += 1

    for i in range(5):
        letter = word[i]
        if GREEN_LETTER in score[i]:
            continue
        duplicates.setdefault(letter, 0)
        duplicates[letter] += 1
        if letter in answer and duplicates[letter] <= answer.count(letter):
            score[i] = f"{YELLOW_LETTER} {letter} "
        else:
            score[i] = f"{GREY_LETTER} {letter} "
    
    history.append("".join(score) + STOP)

    if word == answer:
        return True
    return False

def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("python-wordle by Mike Wang")
        print("==========================")

def print_history():
    for s in history:
        print(s)

if __name__ == '__main__':

    with open("sgb-words.txt", "r") as f:
        words = f.read().splitlines()
        answer = words[randint(0, len(words)-1)].upper()
        words = set(words)

    num_guesses = 1
    history = []
    valid_input = True
    while num_guesses <= MAX_GUESSES:
        clear_screen()
        info_str = f"Guess {num_guesses}/{MAX_GUESSES}"
        if not valid_input:
            info_str += " Invalid input."
        print(info_str)
        print_history()
        guess = input(f"Input: ")
        if guess.isalpha() and guess.lower() in words:
            valid_input = True
            if evaluate(guess.upper()):
                break
            num_guesses += 1
        else:
            valid_input = False
    clear_screen()
    if num_guesses > MAX_GUESSES:
        print(f"Game over! The answer was: {answer}")
    else:
        print(f"Congrats! You guessed it in {num_guesses} tries.")
    print_history()

