delimiters = "({["
matches = {")": "(", "]": "[", "}": "{"}


def check_delimiters(
    input_string: str,
    delimiters: list[str] = delimiters,
    delimiter_matching: dict[str, str] = matches,
):
    stack = []
    for char in input_string:
        if char in delimiters:
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if delimiter_matching[char] != top:
                return "Несиметрично"
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


# Testing
test_cases = [
    "( 23 ( 2 - 3);",  # Missing closing parentheses
    "( 11 }",  # Mismatched closing brace
    "[ ( 3 + 2 ) }",  # Square bracket opened, curly closed
    "{ [ 4 ] ( 5 * 6 )",  # Missing closing curly brace
    "( [ { 9 } ]",  # Missing closing parenthesis
    "( { [ 2 + 2 ] }",  # Missing closing parenthesis
    "[ { ( 8 / 4 ) }",  # Missing closing square bracket
    "{ ( [ 3 - 1 ] )",  # Missing closing curly brace
    "( [ 3 + 2 ] )",
    "{ [ 4 ] ( 5 * 6 ) }",
    "( { [ 2 + 2 ] } )",
    "[ { ( 8 / 4 ) } ]",
    "{ ( [ 3 - 1 ] ) }",
    "( [ 7 ] { 8 } )",
    "{ [ ( 1 ) ] ( 2 ) }",
]

for test_value in test_cases:
    result = check_delimiters(test_value)
    print(f"{test_value:>20}: {result}")
