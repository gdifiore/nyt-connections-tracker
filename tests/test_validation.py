import unittest, textwrap
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
        dedented_valid_input = textwrap.dedent(valid_input)
        self.assertTrue(validate_input(dedented_valid_input))


    def test_invalid_structure(self):
        invalid_start = """
        Invalid Puzzle
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        🟩🟨🟦🟪
        """

        dedented_invalid_structure_input = textwrap.dedent(invalid_start)
        self.assertFalse(validate_input(dedented_invalid_structure_input))


    def test_invalid_puzzle_number(self):
        invalid_number = """
        Connections 
        Puzzle #abc
        🟩🟨🟦🟪
        """

        dedented_invalid_number_input = textwrap.dedent(invalid_number)
        self.assertFalse(validate_input(dedented_invalid_number_input))

    def test_invalid_emoji(self):
        invalid_emoji = """
        Connections 
        Puzzle #123
        🟩🟨🟦🟪
        🟩🟨X🟪
        🟩🟨🟦🟪
        """

        dedented_invalid_emoji_input = textwrap.dedent(invalid_emoji)
        self.assertFalse(validate_input(dedented_invalid_emoji_input))


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
        dedented_too_many_rows_input = textwrap.dedent(too_many_rows_input)
        self.assertFalse(validate_input(dedented_too_many_rows_input))

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

        dedented_too_many_emojis_in_row_input = textwrap.dedent(too_many_emojis_in_row_input)
        self.assertFalse(validate_input(dedented_too_many_emojis_in_row_input))

if __name__ == '__main__':
    unittest.main()
