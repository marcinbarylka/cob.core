"""Main module for the game_gui."""

from tileconsole.console import BDFConsole
from tileconsole.manager import ConsoleManager

from citadel_of_blood.engine.segment import GatewayOfEvil
from citadel_of_blood.game_gui.console import SegmentConsole
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
        width=font_measure[0] * 5,
        height=font_measure[1] * 5,
        font=font_file,
    )
    console.print(1, 1, "Starting Citadel of Blood...")

    segment = SegmentConsole(x=10, y=48, font=font_file, segment=GatewayOfEvil())
    manager.add_console(segment)

    manager.render_all(game.surface)

    print(console.width, console.height)

    game.run()


if __name__ == "__main__":
    run()
