import random as r
from enum import Enum


class Rating(Enum):
    CORRECT = 1
    EXISTS = 0
    WRONG = -1


class Validation(Enum):
    TOO_SHORT = 0
    NOT_A_WORD = 1
    ALLOWED = 2
    NOT_ALLOWED = 3


class Wordle:
    def __init__(self, length=5, hardmode=False):
        self.wordList = getWords(length)
        self.length = length
        self.secretWord = self.chooseRandomWord()
        self.guessCounter = 0
        self.hardMode = hardmode
        self.answerRequirement = ['' for _ in range(length)]
        self.requiredLetters = set()
        print(self.secretWord)

    def chooseRandomWord(self):
        return r.choice(self.wordList)

    def verifyWord(self, word):
        match self.hardMode:
            case False:
                if len(word) != self.length:
                    return Validation.TOO_SHORT
                elif self.length != 5 or word in self.wordList:
                    return Validation.ALLOWED
                else:
                    return Validation.NOT_A_WORD
            case True:
                if len(word) != self.length:
                    return Validation.TOO_SHORT
                if self.length == 5 and word not in self.wordList:
                    return Validation.NOT_A_WORD
                letters = mark_repetitions(word)
                for letter in self.requiredLetters:
                    if letter not in letters:
                        return Validation.NOT_ALLOWED
                for pos in range(self.length):
                    if self.answerRequirement[pos] != '' and self.answerRequirement[pos] != word[pos]:
                        return Validation.NOT_ALLOWED
                return Validation.ALLOWED

    def rateAnswer(self, guess):
        # Mark the correct guesses
        comparator_guess, comparator_answer = check_for_right_letters(guess, self.secretWord)
        # Mark partially correct guesses
        comparator_guess, comparator_answer = mark_repetitions(comparator_guess), mark_repetitions(comparator_answer)
        rating = []
        forHardLetters = mark_repetitions(guess)
        for pos, letter in enumerate(comparator_guess):
            if letter == comparator_answer[pos]:
                rating.append((Rating.CORRECT, guess[pos]))
                self.answerRequirement[pos] = guess[pos]
                self.requiredLetters.add(forHardLetters[pos])
            elif letter in comparator_answer:
                rating.append((Rating.EXISTS, guess[pos]))
                self.requiredLetters.add(forHardLetters[pos])
            else:
                rating.append((Rating.WRONG, guess[pos]))
        self.guessCounter += 1
        print(self.answerRequirement)
        print(self.requiredLetters)
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


def getWords(length: int) -> list:
    if length < 1:
        raise ValueError("Length must be greater than or equal to 1.")
    elif length == 5:
        try:
            return [word.strip("\n").upper() for word in open("src/Text/5letterWords.txt", "r").readlines()]
        except FileNotFoundError:
            return [word.strip("\n").upper() for word in open("Text/5letterWords.txt", "r").readlines()]
    else:
        try:
            return [word.strip("\n").upper()
                    for word in open("src/Text/10kMostCommonWords.txt", "r").readlines() if len(word) == length + 1]
        except FileNotFoundError:
            return [word.strip("\n").upper()
                    for word in open("Text/10kMostCommonWords.txt", "r").readlines() if len(word) == length + 1]
