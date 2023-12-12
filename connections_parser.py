import re

def parse_connections_puzzle(puzzle_text):
    # there was an error with the form input containing \r\n separators instead of \n
    lines = puzzle_text.strip().splitlines()

    # Use regex to extract the puzzle number
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
        # Check if all elements in any row match the emoji
        is_category_correct = any(all(cell == emoji for cell in row) for row in grid)
        results[category] = is_category_correct

    return puzzle_number, results