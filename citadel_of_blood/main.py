"""Main module for the game."""

import sys
from pathlib import Path

from citadel_of_blood.gui import Game
from citadel_of_blood.gui.screens import DefaultScreen

sys.path.append(str(Path(__file__).resolve().parent))


def run():
    """Run the GUI."""
    g = Game()
    g.init_gui()
    g.open_screen(DefaultScreen())
    g.run()


if __name__ == "__main__":
    run()
