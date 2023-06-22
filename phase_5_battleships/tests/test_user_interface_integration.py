import unittest
import pytest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    # def test_ship_setup_scenario(self):
    #     io = TerminalInterfaceHelperMock()
    #     interface = UserInterface(io, Game())
    #     io.expect_print("Welcome to the game!")
    #     io.expect_print("Set up your ships first.")
    #     io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    #     io.expect_print("Which do you wish to place?")
    #     io.provide("2")
    #     io.expect_print("Vertical or horizontal? [vh]")
    #     io.provide("v")
    #     io.expect_print("Which row?")
    #     io.provide("3")
    #     io.expect_print("Which column?")
    #     io.provide("2")
    #     io.expect_print("OK.")
    #     io.expect_print("This is your board now:")
    #     io.expect_print("\n".join([
    #         "..........",
    #         "..........",
    #         ".S........",
    #         ".S........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         ".........."
    #     ]))
        
    #     interface.run()

    def test_ship_full_set_up(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("3")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SS.......",
            ".SS.......",
            "..S.......",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("4")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SSS......",
            ".SSS......",
            "..SS......",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SSSS.....",
            ".SSSS.....",
            "..SSS.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            ".SSSSS....",
            ".SSSS.....",
            ".SSSS.....",
            "..SSS.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        io.expect_print("Done, for now!")
        interface.run()


    def test_ship_placement_error(self):
        io = TerminalInterfaceHelperMock()
        game = Game()
        interface = UserInterface(io, game)
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Error, you've already placed that ship!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("3")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SS.......",
            ".SS.......",
            "..S.......",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("4")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SSS......",
            ".SSS......",
            "..SS......",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".SSSS.....",
            ".SSSS.....",
            "..SSS.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            ".SSSSS....",
            ".SSSS.....",
            ".SSSS.....",
            "..SSS.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
        io.expect_print("Done, for now!")
        interface.run()


    
            