from random import randint

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
        print("Congrats, you guessed correctly!")
        return True
    return False


if __name__ == '__main__':

    with open("sgb-words.txt", "r") as f:
        words = f.read().splitlines()
        answer = words[randint(0, len(words)-1)].upper()
        words = set(words)

    num_guesses = 1
    history = []

    while True:
        for s in history:
            print(s)
        guess = input(f"({num_guesses}/6) Guess: ")
        if guess.isalpha() and guess.lower() in words:
            num_guesses += 1
            if evaluate(guess.upper()):
                break
            if num_guesses > MAX_GUESSES:
                print("Out of tries, game over!")
                print(f"The word was {answer}")
                break
        else:
            print("Word not in list. Try again")

