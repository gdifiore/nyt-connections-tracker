import re, textwrap

def validate_input(user_input):
    """
    Validates the format and content of the user input for a Connections puzzle.

    Args:
        user_input (str): The user-provided text input for the puzzle.

    Returns:
        bool: True if the input is valid, False otherwise.

    Prints error messages for specific validation failures.

    Validation Criteria:
    - The input must have at least 6 lines.
    - The first line must start with 'Connections'.
    - The second line must start with 'Puzzle #'.
    - Extracted puzzle number must be a valid integer.
    - Emojis must be in the set {'🟩', '🟨', '🟪', '🟦'}.
    - There should be no more than 7 rows of emojis.
    - Each row must contain no more than 4 emojis.

    If any of these criteria are not met, corresponding error messages are printed,
    and the function returns False, indicating invalid input.
    """
    if (user_input == ''):
        return False

    dedented_user_input = textwrap.dedent(user_input)

    lines = dedented_user_input.splitlines()

    if (lines[0] == ''):
        lines = lines[1:]

    # check if the input has the expected structure
    if len(lines) < 6 or not lines[0].startswith('Connections') or not lines[1].startswith('Puzzle #'):
        #print("Invalid start format")
        return False

    # cxtract the puzzle number
    if lines[1].split('#')[1].isdigit() == False:
        #print("Invalid puzzle number")
        return False


    # extract the emojis
    emojis = [list(line) for line in lines[2:]]

    # verify emojis, row length, and total number of rows
    valid_emojis = {'🟩', '🟨', '🟪', '🟦'}
    if len(emojis) > 7:
        #print("More than 7 rows of emojis")
        return False

    for row in emojis:
        if len(row) > 4:
            #print("Row contains more than 4 emojis:", ''.join(row))
            return False
        for emoji in row:
            if emoji not in valid_emojis:
                #print("Invalid emoji:", emoji)
                return False
    return True

def parse_connections_puzzle(puzzle_text):
    """
    Parses a Connections puzzle from the provided puzzle_text.

    Args:
        puzzle_text (str): The text representation of the Connections puzzle.

    Returns:
        tuple: A tuple containing the puzzle number and results.
               - If the input is invalid, returns (None, None).
               - Otherwise, returns (puzzle_number, results) where:
                 - puzzle_number (int): The puzzle number extracted from the input.
                 - results (dict): A dictionary mapping puzzle categories to correctness.
                   - Categories include 'Yellow' (Easiest), 'Green', 'Blue', and 'Purple' (Hardest).
                   - Each category is associated with a boolean indicating correctness.
    """
    if (validate_input(puzzle_text) == False):
        return None, None # invalid input

    dedented_puzzle_text = textwrap.dedent(puzzle_text)

    # there was an error with the form input containing \r\n separators instead of \n
    lines = dedented_puzzle_text.strip().splitlines()

    # use regex to extract the puzzle number
    puzzle_number_match = re.search(r"Puzzle #(\d+)", lines[1])
    puzzle_number = int(puzzle_number_match.group(1))

    grid = [list(line) for line in lines[2:]]

    categories = {
        '🟨': 'Yellow', # Easiest
        '🟩': 'Green',
        '🟦': 'Blue',
        '🟪': 'Purple', # Hardest
    }

    results = {}

    for emoji, category in categories.items():
        # check if all elements in any row match the emoji
        is_category_correct = any(all(cell == emoji for cell in row) for row in grid)
        results[category] = is_category_correct

    return puzzle_number, results