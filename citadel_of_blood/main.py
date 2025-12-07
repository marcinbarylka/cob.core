"""Main module for the game."""

from citadel_of_blood.gui import Game
from citadel_of_blood.gui.screens import DefaultScreen


def run():
    """Run the GUI."""
    g = Game()
    g.init_gui()
    g.run()


if __name__ == "__main__":
    run()
