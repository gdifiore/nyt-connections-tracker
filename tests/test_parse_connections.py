import unittest
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

from nyt_connections_tracker.connections_parser import parse_connections_puzzle

class TestValidateInput(unittest.TestCase):

    def test_valid_input(self):
        valid_input = """
        Connections 
        Puzzle #184
        🟩🟩🟩🟩
        🟨🟨🟨🟨
        🟦🟦🟦🟦
        🟪🟪🟪🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(valid_input)
        self.assertEqual(puzzle_number, 184)
        self.assertEqual(guesses, 4)
        self.assertEqual(results, {'Yellow': True, 'Green': True, 'Blue': True, 'Purple': True})

    def test_complex_valid_input(self):
        complex_valid_input = """
        Connections 
        Puzzle #184
        🟩🟨🟨🟨
        🟨🟨🟪🟨
        🟨🟨🟨🟨
        🟦🟪🟦🟩
        🟩🟩🟩🟩
        🟦🟦🟪🟦
        """

        puzzle_number, results, guesses = parse_connections_puzzle(complex_valid_input)
        self.assertEqual(puzzle_number, 184)
        self.assertEqual(guesses, 6)
        self.assertEqual(results, {'Yellow': True, 'Green': True, 'Blue': False, 'Purple': False})

    def test_invalid_structure(self):
        invalid_start = """
        Invalid Puzzle
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(invalid_start)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

    def test_invalid_puzzle_number(self):
        invalid_number = """
        Connections 
        Puzzle #abc
        🟩🟨🟦🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(invalid_number)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

    def test_invalid_emoji(self):
        invalid_emoji = """
        Connections 
        Puzzle #123
        🟩🟨🟦🟪
        🟩🟨X🟪
        🟩🟨🟦🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(invalid_emoji)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

    def test_too_many_rows(self):
        too_many_rows_input = """
        Connections 
        Puzzle #123
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(too_many_rows_input)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

    def test_too_many_emojis_in_row(self):
        too_many_emojis_in_row_input = """
        Connections 
        Puzzle #123
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪🟪
        🟩🟨🟦🟪
        """

        puzzle_number, results, guesses = parse_connections_puzzle(too_many_emojis_in_row_input)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

    def test_empty_input(self):
        empty_input = ""

        puzzle_number, results, guesses = parse_connections_puzzle(empty_input)
        self.assertIsNone(puzzle_number)
        self.assertIsNone(guesses)
        self.assertIsNone(results)

if __name__ == '__main__':
    unittest.main()
