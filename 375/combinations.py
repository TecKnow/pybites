from itertools import product

T9: dict[str, list[str]] = {"2": list("ABC"),
                            "3": list("DEF"),
                            "4": list("GHI"),
                            "5": list("KJL"),
                            "6": list("MNO"),
                            "7": list("PQRS"),
                            "8": list("TUV"),
                            "9": list("WXYZ")}


def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    if len(digits) > 4:
        raise ValueError("A maximum of 4 digits is supported")
    elif (forbidden := set(digits) - set(T9.keys())):
        raise ValueError(
            f"The symbols {forbidden} cannot be converted into T9.")
    factors: list[list[str]] = [T9[digit] for digit in digits]
    return [''.join(T9_word).casefold() for T9_word in product(*factors)]


if __name__ == "__main__":
    print(generate_letter_combinations("23"))
