"""Core module."""

import pygame

from citadel_of_blood.errors import GameScreenError
from citadel_of_blood.gui.constants import SETTINGS_FILENAME
from citadel_of_blood.gui.events import EventsHandler
from citadel_of_blood.gui.screens import GameScreen
from citadel_of_blood.gui.settings import GUIColors, GUISettings, Settings


class Game:
    """Game class.

    Attributes:
          screen (pygame.Surface | None): The screen.
          fullscreen (bool): Whether the screen is fullscreen.
          width (int): The width of the screen.
          height (int): The height of the screen.
          settings (Settings): The settings.
          clock (pygame.time.Clock): The clock.
          running (bool): Whether the game is running.
          is_soundcard (bool): Whether the sound card is available.
          active_game_screen (GameScreen | None): The active screen.
          events_handler (EventsHandler): The events handler.
          frame (int): The frame counter.

    """

    def __init__(self, active_game_screen: GameScreen | None = None) -> None:
        """Initialize the Game class.

        This method initializes all the necessary attributes.
        """
        self.screen: pygame.Surface | None = None
        self.fullscreen: bool = True
        self.width: int = 0
        self.height: int = 0
        self.settings: Settings = Settings(gui=GUISettings(colors=GUIColors()))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.is_soundcard: bool = True

        self.active_game_screen: GameScreen | None = active_game_screen
        self.events_handler: EventsHandler = EventsHandler()
        self.frame: int = 0  # frame counter

    def load_settings(self, toml_file: str) -> None:
        """Load the settings.

        Args:
            toml_file (str): The TOML file to load.

        Returns:
            Settings: The settings object.

        """
        self.settings = Settings.load(toml_file)
        self.fullscreen = self.settings.gui.fullscreen
        self.width = self.settings.gui.width
        self.height = self.settings.gui.height

    def init_gui(self, toml_file: str = "") -> None:
        """Initialize the GUI.

        Args:
            toml_file (str): The TOML file to load.

        """
        if not toml_file:
            toml_file = SETTINGS_FILENAME
        self.load_settings(toml_file)
        pygame.init()

        # check if sound card is available
        try:
            pygame.mixer.init()
        except pygame.error:
            self.is_soundcard = False
        if self.is_soundcard:
            pygame.mixer.set_num_channels(8)

        print(f"Initializing screen with width: {self.width}, height: {self.height}, fullscreen: {self.fullscreen}")
        self.screen = (
            pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            if self.fullscreen
            else pygame.display.set_mode((self.width, self.height))
        )
        pygame.display.set_caption(self.settings.gui.caption)
        print(f"Caption set to: {self.settings.gui.caption}")
        print("Screen initialized.")

    def update(self) -> None:
        """Check the state."""
        if not self.events_handler.running:
            self.running = False

    def open_screen(self, screen: GameScreen) -> None:
        """Add a screen."""
        screen.settings = self.settings
        self.active_game_screen = screen

    def run(self) -> None:
        """Run the GUI."""
        if self.screen is None:
            msg = "Screen is not initialized. Call init_gui() before run()."
            raise ValueError(msg)
        if self.settings is None:
            msg = "Settings are not initialized. Call init_gui() before run()."
            raise ValueError(msg)
        if self.active_game_screen is None:
            msg = "Active screen is not set. Set an active game screen before run()."
            raise GameScreenError(msg)

        self.active_game_screen.draw()
        while self.running:
            events = pygame.event.get()
            events = self.events_handler.handle_events(events)
            _ = self.active_game_screen.handle_events(events)
            self.active_game_screen.update()
            self.update()
            pygame.display.update()
            self.clock.tick(self.settings.gui.fps)
            self.frame += 1
        pygame.quit()
