import re

def validate_input(user_input):
    lines = user_input.splitlines()

    # check if the input has the expected structure
    if len(lines) < 3 or not lines[0].startswith('Connections') or not lines[1].startswith('Puzzle #'):
        print("Invalid input format")
        return False

    # cxtract the puzzle number
    puzzle_number = int(lines[1].split('#')[1])

    # extract the emojis
    emojis = [list(line) for line in lines[2:]]

    # verify emojis, row length, and total number of rows
    valid_emojis = {'🟩', '🟨', '🟪', '🟦'}
    if len(emojis) > 7:
        print("More than 7 rows of emojis")
        return False

    for row in emojis:
        if len(row) > 4:
            print("Row contains more than 4 emojis:", ''.join(row))
            return False
        for emoji in row:
            if emoji not in valid_emojis:
                print("Invalid emoji:", emoji)
                return False

def parse_connections_puzzle(puzzle_text):
    if (validate_input(puzzle_text) == False):
        return None, None # invalid input

    # there was an error with the form input containing \r\n separators instead of \n
    lines = puzzle_text.strip().splitlines()

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