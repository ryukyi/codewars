"""
https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
"""

import pytest

lookup = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
}


def remove_and(string: str) -> str:
    """
    Remove the word 'and' from the string as it does not affect the numerical value.

    Args:
    string (str): The input string representing the number in words.

    Returns:
    str: The cleaned string without 'and'.
    """
    return string.replace(" and ", " ")


def process_part(part: str, acc: int) -> int:
    """
    Process each part of the string to compute its numerical value based on the lookup.

    Args:
    part (str): A segment of the string representing a number or a multiplier.
    current (int): The current accumulated value before processing this part.

    Returns:
    int: Updated current value after processing the part.
    """
    if part in lookup:
        value = lookup[part]
        if value in (100, 1000, 1000000):
            if acc == 0:
                acc = 1
            acc *= value
        else:
            acc += value
    else:
        # Handle compound numbers like "twenty-one"
        parts = part.split('-')
        for subpart in parts:
            if subpart in lookup:
                acc += lookup[subpart]
    return acc


def parse_int(string: str) -> int:
    """
    Convert a string representation of a number into its integer form.

    Args:
    string (str): The string representation of the number.

    Returns:
    int: The integer value of the number.
    """
    string = remove_and(string)
    parts = string.split()
    total = 0
    current = 0

    for part in parts:
        if part in lookup and lookup[part] in (1000, 1000000):
            current = process_part(part, current)
            total += current
            current = 0
        else:
            current = process_part(part, current)

    total += current
    return total


@pytest.mark.parametrize(
    "string, expected",
    [
        ("one", 1),
        ("twenty", 20),
        ("two hundred forty-six", 246),
        ("seven hundred eighty-three thousand nine hundred and nineteen", 783919),
        ("one hundred eleven thousand nine hundred twenty-one", 111921),
        ("twenty-one", 21),
        ("ninety-nine", 99),
        ("one thousand", 1000),
        ("one million", 1000000),
        ("five hundred thousand one hundred", 500100),
        ("zero", 0),
        ("twelve thousand three hundred forty-five", 12345),
    ],
    ids=[
        "simple number",
        "double digit",
        "complex number with hundred",
        "large number with thousand and hundred",
        "number with hundred and thousand",
        "compound number under hundred",
        "compound number under hundred at limit",
        "round thousand",
        "maximum limit",
        "complex number in hundred thousands",
        "minimum limit",
        "medium complex number",
    ],
)
def test_parse_int(string, expected):
    """
    Test the parse_int function with various number strings to ensure it correctly parses and computes the integer value.
    """
    result = parse_int(string)
    assert result == expected


@pytest.mark.parametrize(
    "part, current, expected",
    [
        # Testing simple numbers
        ("one", 0, 1),
        ("twenty", 0, 20),
        ("ninety-nine", 0, 99),
        # Testing multipliers on their own
        ("hundred", 1, 100),
        ("thousand", 1, 1000),
        ("million", 1, 1000000),
        # Testing multipliers with non-zero current
        ("hundred", 3, 300),
        ("thousand", 2, 2000),
        ("million", 2, 2000000),
        # Testing multipliers following numbers
        ("hundred", 7, 700),
        ("thousand", 783, 783000),
        ("million", 1, 1000000),
        # Testing numbers after multipliers
        ("twenty", 700, 720),  # 700 + 20
        ("nineteen", 783000, 783019),  # 783000 + 19
        ("one", 1000000, 1000001),  # 1000000 + 1
        # Testing compound numbers
        ("twenty-one", 0, 21),
        ("ninety-nine", 1000, 1099),  # 1000 + 99
        # Edge cases
        ("zero", 0, 0),
        ("zero", 1000, 1000),  # 1000 + 0
        ("hundred", 0, 100),  # 0 treated as 1 for multipliers
    ],
    ids=[
        "simple one",
        "simple twenty",
        "simple ninety-nine",
        "multiplier hundred alone",
        "multiplier thousand alone",
        "multiplier million alone",
        "multiplier hundred with base",
        "multiplier thousand with base",
        "multiplier million with base",
        "multiplier hundred after number",
        "multiplier thousand after number",
        "multiplier million after number",
        "number after hundred",
        "number after thousand",
        "number after million",
        "compound twenty-one",
        "compound ninety-nine after thousand",
        "edge zero alone",
        "edge zero after thousand",
        "edge hundred from zero",
    ],
)
def test_process_part(part, current, expected):
    """
    Test the process_part function to ensure it correctly processes individual parts of a number string.
    """
    result = process_part(part, current)
    assert result == expected, f"Failed on part: {part} with current: {current}"
