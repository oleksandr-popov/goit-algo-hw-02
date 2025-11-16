from collections import deque


def is_palindrome(input_str) -> bool:
    # Normalize string
    letters = "".join(input_str.lower().split())

    # Transofrm str to deque
    letters_deque = deque(letters)

    while len(letters_deque) > 1:
        # Check characters from both side
        if letters_deque.popleft() != letters_deque.pop():
            return False
    return True


# Testing
test_cases = [
    "Intro",
    "Jeronimo",
    "Rotator",
    "Noon",
    "Radar",
    "Ethos",
    "Never Odd or Even",
]

for test_value in test_cases:
    print(f"'{test_value}' is palindrome: {is_palindrome(test_value)}")
