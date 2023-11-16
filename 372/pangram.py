from string import ascii_lowercase


def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """

    sentence_letter_set = set(sentence.lower())
    missing_letters = set(ascii_lowercase) - sentence_letter_set
    return True if len(missing_letters) == 0 else False


if __name__ == "__main__":
    validate_pangram()
