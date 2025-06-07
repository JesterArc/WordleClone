import random as r
from ..Words import getWords
from enum import Enum


class Rating(Enum):
    CORRECT = 1
    EXISTS = 0
    WRONG = -1


class Validation(Enum):
    TOO_SHORT = 0
    NOT_A_WORD = 1
    ALLOWED = 2


class Wordle:
    def __init__(self, length=5):
        self.wordList = getWords(length)
        self.length = length
        self.secretWord = self.chooseRandomWord()
        self.guessCounter = 0

    def chooseRandomWord(self):
        return r.choice(self.wordList)

    def verifyWord(self, word):
        if len(word) != self.length:
            return Validation.TOO_SHORT
        elif self.length != 5 or word in self.wordList:
            return Validation.ALLOWED
        else:
            return Validation.NOT_A_WORD

    def rateAnswer(self, guess):
        # Mark the correct guesses
        comparator_guess, comparator_answer = check_for_right_letters(guess, self.secretWord)
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
        self.guessCounter += 1
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
