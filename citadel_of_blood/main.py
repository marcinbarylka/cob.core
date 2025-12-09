"""Main module for the game."""

from tileconsole.console import BDFConsole
from tileconsole.manager import ConsoleManager

from citadel_of_blood.gui import Game
from citadel_of_blood.gui.settings import Settings


def run():
    """Run the GUI."""
    game = Game()
    game.init_gui()

    font_path = BDFConsole.get_default_font_path()
    settings = Settings()
    font_file = f"{font_path}/{settings.font}"
    print(f"Using font file: {font_file}")
    font_measure = BDFConsole.measure_bdf(font_file)
    manager = ConsoleManager()
    console = manager.create_console(
        BDFConsole,
        x=0,
        y=0,
        width=settings.width // font_measure[0],
        height=settings.height // font_measure[1],
        font=font_file,
        background=(0, 89, 129),
        foreground=(96, 183, 231),
    )
    console.print(1, 1, "READY")
    console.print(1, 2, " ", background=(96, 183, 231))
    manager.render_all(game.surface)

    game.run()


if __name__ == "__main__":
    run()
