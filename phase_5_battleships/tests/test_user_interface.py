from unittest.mock import Mock
import unittest
from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock

"""
format board formats for one 2 length ship
"""

class TestFormatBoard(unittest.TestCase):
    def test_format_board(self):
        # Create a mock game object
        game_mock = Mock()
        mock_io = Mock()
        game_mock.rows = 10
        game_mock.cols = 10
        game_mock.ship_at.side_effect = lambda row, col: (row, col) in [(2, 3), (3, 3)]

        # Create an instance of the class with the mock game object
        user = UserInterface(mock_io, game_mock)

        # Call the _format_board method
        result = user._format_board()

        # Assert the expected result
        expected_result = "\n".join(['🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵⚫🔵🔵🔵🔵🔵🔵🔵', '🔵🔵⚫🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵', '🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵'])
        assert result == expected_result
        