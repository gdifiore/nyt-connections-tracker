import re

def parse_connections_puzzle(puzzle_text):
    # there was an error with the form input containing \r\n separators instead of \n
    lines = puzzle_text.strip().splitlines()
    #print(lines)

    # Use regex to extract the puzzle number
    puzzle_number_match = re.search(r"Puzzle #(\d+)", lines[1])
    puzzle_number = int(puzzle_number_match.group(1))
    #print(puzzle_number)

    grid = [list(line) for line in lines[2:]]
    #print(grid)

    categories = {
        '🟨': 'Yellow',
        '🟩': 'Green',
        '🟪': 'Blue',
        '🟦': 'Purple',
    }

    results = {}

    for emoji, category in categories.items():
        # Check if all elements in any row match the emoji
        is_category_correct = any(all(cell == emoji for cell in row) for row in grid)
        results[category] = is_category_correct

    return puzzle_number, results

''' sample usage
puzzle_number, results = parse_connections_puzzle(puzzle_text)

print(f"Puzzle #{puzzle_number} Results:")
for category, is_correct in results.items():
    print(f"{category}: {'Correct' if is_correct else 'Incorrect'}")
'''