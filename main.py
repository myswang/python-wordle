from random import randint

# definition of colour escape sequences
GREEN_LETTER = "\033[1;42m "
YELLOW_LETTER = "\033[1;43m "
GREY_LETTER = "\033[1;49m "
STOP = "\033[0m"

MAX_GUESSES = 6

def invalid_input(word):
    if word.isalpha():
        return False if len(word) == 5 and word.lower() in words else True
    return True


# calculates the "correctness" of word, prints the coloured result to console
def evaluate(word):
    duplicates = {}
    score = [None, None, None, None, None]
    for i in range(5):
        letter = word[i]
        if letter == answer[i]:
            score[i] = GREEN_LETTER + letter
            duplicates.setdefault(letter, 0)
            duplicates[letter] += 1
        else:
            score[i] = ""

    for i in range(5):
        letter = word[i]
        if GREEN_LETTER in score[i]:
            continue
        duplicates.setdefault(letter, 0)
        duplicates[letter] += 1
        if letter in answer and duplicates[letter] <= answer.count(letter):
            score[i] = YELLOW_LETTER + letter
        else:
            score[i] = GREY_LETTER + letter

    for i in score:
        print(i + " ", end="")
    print(STOP)

    if word == answer:
        print("Congrats, you guessed correctly!")
        return True
    return False


if __name__ == '__main__':

    with open("sgb-words.txt", "r") as f:
        words = f.read().splitlines()
        answer_idx = randint(0, len(words) - 1)
        answer = words[answer_idx].upper()
        words = set(words)

    guess = ""
    num_guesses = 1

    while True:
        guess = input(f"({num_guesses}/6) Guess: ").upper()
        if invalid_input(guess):
            print("Word not in list. Try again")
            continue
        else:
            num_guesses += 1
            if evaluate(guess):
                break
            if num_guesses > MAX_GUESSES:
                print("Out of tries, game over!")
                print(f"The word was {answer}")
                break
