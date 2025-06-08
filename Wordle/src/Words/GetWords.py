def getWords(length: int) -> list:
    if length < 1:
        raise ValueError("Length must be greater than or equal to 1.")
    elif length == 5:
        try:
            return [word.strip("\n").upper() for word in open("src/Words/5letterWords.txt", "r").readlines()]
        except FileNotFoundError:
            return [word.strip("\n").upper() for word in open("Words/5letterWords.txt", "r").readlines()]
    else:
        try:
            return [word.strip("\n").upper()
                    for word in open("src/Words/10kMostCommonWords.txt", "r").readlines() if len(word) == length + 1]
        except FileNotFoundError:
            return [word.strip("\n").upper()
                    for word in open("Words/10kMostCommonWords.txt", "r").readlines() if len(word) == length + 1]