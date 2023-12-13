import unittest
from connections_parser import validate_input

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
        self.assertTrue(validate_input(valid_input))

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
        self.assertTrue(validate_input(complex_valid_input))

    def test_invalid_structure(self):
        invalid_start = """
        Invalid Puzzle
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        """

        self.assertFalse(validate_input(invalid_start))


    def test_invalid_puzzle_number(self):
        invalid_number = """
        Connections 
        Puzzle #abc
        🟩🟨🟦🟪
        """

        self.assertFalse(validate_input(invalid_number))

    def test_invalid_emoji(self):
        invalid_emoji = """
        Connections 
        Puzzle #123
        🟩🟨🟦🟪
        🟩🟨X🟪
        🟩🟨🟦🟪
        """

        self.assertFalse(validate_input(invalid_emoji))


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
        self.assertFalse(validate_input(too_many_rows_input))

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

        self.assertFalse(validate_input(too_many_emojis_in_row_input))

    def test_empty_input(self):
        self.assertFalse(validate_input(''))

if __name__ == '__main__':
    unittest.main()
