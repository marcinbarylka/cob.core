"""Main module for the game."""

from tileconsole import BDF_FOLDER
from tileconsole.console import FramedConsole
from tileconsole.manager import ConsoleManager

from citadel_of_blood.gui import Game


def run():
    """Run the GUI."""
    game = Game()
    game.init_gui()
    manager = ConsoleManager()
    console1 = manager.create_console(
        type=FramedConsole,
        font=f"{BDF_FOLDER}/iv8x16u.bdf",
        width=1024 // 8,
        height=768 // 16,
        x=0,
        y=0,
        background=(0xa0, 0xa0, 0xa0),
        foreground=(0x00, 0x00, 0x00),
    )
    manager.render_all(game.surface)
    game.run()


if __name__ == "__main__":
    run()
