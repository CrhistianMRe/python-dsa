def letter_combinations(digits: str) -> list[str]:
    if(not digits): return []
    result = [""]


    for digit in digits:
        currentLetters = digit_to_letters.get(digit)

        if(currentLetters == None): raise ValueError(f"invalid digit: {digit}")


        newResult = []

        for combo in result:
            for character in currentLetters:
                newResult.append(combo + character)

        result = newResult




    return result



# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

