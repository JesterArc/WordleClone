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
    def __init__(self, length=5, hardMode=False):
        """Provides the logic for the game

        On creation, the class:\n
        - Generates a word list of words of provided length
        - Chooses the secret word for the player to guess
        - Sets whether the game is in normal mode or hard mode

        Args:
            length (int): The length of the word
            hardMode (bool): If the game is played in hard mode or normal mode
        """
        self.wordList = getWords(length)
        self.length = length
        self.secretWord = self.chooseRandomWord()
        self.guessCounter = 0
        self.hardMode = hardMode
        self.answerRequirement = ['' for _ in range(length)]
        self.requiredLetters = set()

    def chooseRandomWord(self):
        return r.choice(self.wordList)

    def verifyWord(self, word: str) -> Validation:
        """Checks if the provided word is valid:\n
        - If the word has length equal to 5, we check if the word is in the list of words,
        - If the word is too short, we return "TOO_SHORT"\n

        In Hard mode, we add extra checks:\n
        - If the word doesn't contain all letters in required letters, we return "NOT_ALLOWED"
        - If the word doesn't match the answer requirement, we return "NOT_ALLOWED"

        Otherwise, we return "ALLOWED"


        Args:
            word (str): a word provided by the player

        Returns:
            Validation: returns the validation of the word
        """
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

    def rateAnswer(self, guess: str) -> list[tuple[Rating, str]]:
        """Rates each letter in the answer:\n
        - If it is in the right spot, it gets the "Correct" rating
        - Else if the letter is in the word but not here, it gets the "Exists" rating
        - Else it gets the "Wrong" rating

        "Correct" letters get added to the answer requirements\n
        "Correct" or "Exists" letters get added to required letters

        Args:
            guess (str): a word provided by the player

        Returns:
            list[tuple[Rating, str]] : a list of tuples with a rating of the letter and the letter itself
        """
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
        return rating


def check_for_right_letters(guess, correct) -> tuple[str, str]:
    """Marks where words contain the exact same letter with "-"

    Args:
        guess (str): a word provided by the player
        correct (str): the word the player is trying to guess

    Returns:
        tuple[str, str] : a tuple of strings
    """
    guess = list(guess)
    correct = list(correct)
    for i in range(len(guess)):
        if guess[i] == correct[i]:
            guess[i], correct[i] = "-", "-"
    return "".join(guess), "".join(correct)


def mark_repetitions(word: str) -> list[str]:
    """Marks each repeating letter in word with a number of times it appeared before

    Args:
        word (str): a string of letters

    Returns:
        list[str] : list of letters
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


def getWords(length: int) -> list[str]:
    """Returns a list of words of the provided length

    Args:
        length (int): desired length of the words

    Returns:
        list : list of letters with x length

    Raises:
        ValueError: If length is less than 1
    """
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
