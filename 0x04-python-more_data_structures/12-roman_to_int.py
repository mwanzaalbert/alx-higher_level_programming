#!/usr/bin/python3

ROMAN_NUMERALS = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}


def roman_to_int(roman_literal):
    if not roman_literal or not isinstance(roman_literal, str):
        return 0  # or raise ValueError

    total = 0
    length = len(roman_literal)

    for index, letter in enumerate(roman_literal):
        # Get the current numeral's value
        current_value = ROMAN_NUMERALS[letter]

        # Check if the current numeral should be subtracted (e.g., IV, IX)
        if index + 1 < length and (
                current_value < ROMAN_NUMERALS[roman_literal[index + 1]]):
            total -= current_value
        else:
            total += current_value

    return total


if __name__ == "__main__":
    test_cases = ["X", "VII", "IX", "LXXXVII", "DCCVII", "CDVII", 'CMLX']

    for roman_number in test_cases:
        print(f"{roman_number} = {roman_to_int(roman_number)}")
