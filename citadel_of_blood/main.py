"""Main module for the game."""

from tileconsole import BDF_FOLDER
from tileconsole.console import FramedConsole
from tileconsole.manager import ConsoleManager

from citadel_of_blood.gui import Game


def run():
    """Run the GUI."""
    game = Game()
    game.init_gui()
    font_path = f"{BDF_FOLDER}/10x20.bdf"
    font_measurements = FramedConsole.measure_bdf(font_path)
    manager = ConsoleManager()
    console1 = manager.create_console(
        type=FramedConsole,
        font=font_path,
        width=1024 // font_measurements[0],
        height=768 // font_measurements[1],
        x=0,
        y=0,
        background=(0xA0, 0xA0, 0xA0),
        foreground=(0x00, 0x00, 0x00),
    )
    console1.print(1, 1, "Hello, Citadel of Blood!")
    manager.render_all(game.surface)
    game.run()


if __name__ == "__main__":
    run()
