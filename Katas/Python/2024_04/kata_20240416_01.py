"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""

def fake_bin(digits):
    binary_digits = ""
    for digit in digits:
        binary_digits += "0" if int(digit) < 5 else "1"
    return binary_digits