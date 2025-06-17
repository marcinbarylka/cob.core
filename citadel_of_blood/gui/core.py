"""Core module."""

from pathlib import Path

import pygame
from pygame import Surface

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.errors.engine_errors import GameScreenError
from citadel_of_blood.gui.events import EventsHandler
from citadel_of_blood.gui.screens import GameScreen
from citadel_of_blood.gui.settings import Settings
from citadel_of_blood.gui.sfx import init_sfx


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
          soundcard_enabled (bool): Whether the sound card is available.
          active_game_screen (GameScreen | None): The active screen.
          events_handler (EventsHandler): The events handler.
          frame (int): The frame counter.
          custom_cursor (pygame.cursors.Cursor | None): Custom cursor object.

    """

    def __init__(self, active_game_screen: GameScreen | None = None) -> None:
        """Initialize the Game class.

        This method initializes all the necessary attributes.
        """
        self.screen: pygame.Surface | None = None
        self.fullscreen: bool = True
        self.width: int = 0
        self.height: int = 0
        self.settings: Settings = Settings.instance()
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
        self.soundcard_enabled: bool = True
        self.custom_cursor: pygame.cursors.Cursor | None = None

        self.active_game_screen: GameScreen | None = active_game_screen
        self.events_handler: EventsHandler = EventsHandler()
        self.frame: int = 0  # frame counter
        self.cursor: Surface | None = None  # Cursor surface for custom cursor

        self.cache_folder: str = ""

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
        self.cache_folder = self.settings.gui.cache_folder

    def init_gui(self, toml_file: str = "") -> None:
        """Initialize the GUI.

        Args:
            toml_file (str): The TOML file to load.

        """
        pygame.init()

        # ensure the cache folder exists
        if not Path(self.settings.gui.cache_folder).exists():
            self.settings.create_cache_folder()
        # Set the cache folder for the settings
        self.settings.gui.cache_folder = self.cache_folder

        # check if sound card is available
        try:
            init_sfx()
        except pygame.error:
            self.soundcard_enabled = False
            # We set the attributes only if they exist
            if hasattr(self.settings, "sfx_enabled"):
                self.settings.sfx_enabled = False
            if hasattr(self.settings, "music_enabled"):
                self.settings.music_enabled = False

        print(f"Initializing screen with width: {self.width}, height: {self.height}, fullscreen: {self.fullscreen}")
        self.screen = (
            pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            if self.fullscreen
            else pygame.display.set_mode((self.width, self.height))
        )
        pygame.display.set_caption(self.settings.gui.caption)
        print(f"Caption set to: {self.settings.gui.caption}")
        cursor_path = PROJECT_ROOT / "assets/gui/cursor.png"
        try:
            self.cursor = pygame.image.load(cursor_path).convert_alpha()
            pygame.mouse.set_visible(False)
        except Exception as e:
            print(f"Failed to load cursor image: {e}")
            self.cursor = None

        print("Screen initialized.")

    def update(self) -> None:
        """Check the state."""
        if not self.events_handler.running:
            self.running = False
        if self.screen and self.active_game_screen:
            self.screen.blit(self.active_game_screen.surface, (0, 0))

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

        while self.running:
            events = pygame.event.get()
            events = self.events_handler.handle_events(events)
            _ = self.active_game_screen.handle_events(events)
            self.active_game_screen.update()
            self.active_game_screen.draw()
            self.update()

            # Draw the cursor if it exists
            if hasattr(self, "cursor") and self.cursor:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.screen.blit(self.cursor, (mouse_x, mouse_y))

            pygame.display.update()
            self.clock.tick(self.settings.gui.fps)
            self.frame += 1
        pygame.quit()
