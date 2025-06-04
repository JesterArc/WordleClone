import random as r
from enum import Enum


class Rating(Enum):
    CORRECT = 1
    EXISTS = 0
    WRONG = -1


def chooseRandomWord():
    # For testing
    return "BREAD"
#     return r.choice(wordList)


def verifyWord(word):
    return len(word) == 5


def rateAnswer(guess, correct):
    # Mark the correct guesses
    comparator_guess, comparator_answer = check_for_right_letters(guess, correct)
    # Mark partially correct guesses
    comparator_guess, comparator_answer = mark_repetitions(comparator_guess), mark_repetitions(comparator_answer)
    rating = []
    for pos, letter in enumerate(comparator_guess):
        if letter == comparator_answer[pos]:
            rating.append((Rating.CORRECT, guess[pos]))
        elif letter in comparator_answer:
            rating.append((Rating.EXISTS, guess[pos]))
        else:
            rating.append((Rating.WRONG, guess[pos]))
    return rating


def check_for_right_letters(guess, correct):
    guess = list(guess)
    correct = list(correct)
    for i in range(len(guess)):
        if guess[i] == correct[i]:
            guess[i], correct[i] = "-", "-"
    return "".join(guess), "".join(correct)


def mark_repetitions(word) -> list:
    """Marks each repeating letter in word with a number of times it appeared before

    Args:
        word (str): a string of letters

    Returns:
        list : list of letters
    """
    letters = list(word)
    count_repetitions = dict()
    for pos, letter in enumerate(letters):
        if letter == "-":
            pass
        letters[pos] = f"{letter}{count_repetitions.get(letter, '')}"
        if letter not in count_repetitions:
            count_repetitions[letter] = 1
        else:
            count_repetitions[letter] += 1
    return letters
