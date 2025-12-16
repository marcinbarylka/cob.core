"""Main module for the game_gui."""

from engine.map import Board
from engine.segment import Room
from tileconsole.console import BDFConsole
from tileconsole.manager import ConsoleManager

from citadel_of_blood import Exit
from citadel_of_blood.game_gui.console import BoardConsole
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

    segment = Room(exits=[Exit.WALL, Exit.ROOM_CLOSED, Exit.WALL, Exit.ROOM])
    segment.randomize_feature()
    board = Board()
    board.map[(0, 1, 0)] = segment
    board_console = BoardConsole(
        x=0, y=100, width=800, height=400, font=font_file, board=board
    )
    manager.add_console(board_console)
    manager.render_all(game.surface)

    game.run()


if __name__ == "__main__":
    run()
