import re
import textwrap

def validate_input(user_input):
    """Validate NYT Connections puzzle format."""
    if user_input == '':
        return False

    dedented_user_input = textwrap.dedent(user_input)

    lines = dedented_user_input.splitlines()

    if lines[0] == '':
        lines = lines[1:]

    if len(lines) < 6 or not lines[0].startswith('Connections') or not lines[1].startswith('Puzzle #'):
        return False

    if not lines[1].split('#')[1].isdigit():
        return False


    emojis = [list(line) for line in lines[2:]]

    valid_emojis = {'🟩', '🟨', '🟪', '🟦'}
    if len(emojis) > 7:
        return False

    for row in emojis:
        if len(row) > 4:
            return False
        for emoji in row:
            if emoji not in valid_emojis:
                return False
    return True

def parse_connections_puzzle(puzzle_text):
    """Parse puzzle text and return (puzzle_number, results_dict, guesses)."""
    if not validate_input(puzzle_text):
        return None, None, None

    dedented_puzzle_text = textwrap.dedent(puzzle_text)
    lines = dedented_puzzle_text.strip().splitlines()
    puzzle_number_match = re.search(r"Puzzle #(\d+)", lines[1])
    puzzle_number = int(puzzle_number_match.group(1))

    grid = [list(line) for line in lines[2:]]

    categories = {
        '🟨': 'Yellow',
        '🟩': 'Green',
        '🟦': 'Blue',
        '🟪': 'Purple',
    }

    results = {}

    for emoji, category in categories.items():
        is_category_correct = any(all(cell == emoji for cell in row) for row in grid)
        results[category] = is_category_correct

    return puzzle_number, results, len(lines[2:])
