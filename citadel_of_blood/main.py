"""Main module for the game."""

from tileconsole.manager import ConsoleManager

from citadel_of_blood.gui import Game


def run():
    """Run the GUI."""
    g = Game()
    g.init_gui()

    cm = ConsoleManager()

    g.run()


if __name__ == "__main__":
    run()
