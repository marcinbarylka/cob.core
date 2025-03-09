"""Core module."""

from typing import Any

import pygame

from citadel_of_blood.gui.events import EventsHandler
from citadel_of_blood.gui.settings import Settings


class Game:
    """Game class.

    Attributes
    ----------
        screen (pygame.Surface): The screen.
        fullscreen (bool): Fullscreen mode.
        width (int): The width.
        height (int): The height.
        settings (Any): The settings.
        clock (pygame.time.Clock): The clock.
        running (bool): Running state.

        events_handler (EventsHandler): The events handler.
        is_soundcard (bool): Sound card availability.
        frame (int): Frame counter.

    """

    def __init__(self) -> None:
        """Initialize the Game class.

        This method initializes all the necessary attributes:
        - screen: The Pygame surface for display
        - fullscreen: Boolean indicating fullscreen mode
        - width, height: Dimensions of the game window
        - settings: Game configuration
        - clock: Pygame clock for frame timing
        - running: Game state indicator
        - events_handler: Handler for game events
        - is_soundcard: Boolean indicating sound card availability
        - frame: Frame counter
        """
        self.screen: pygame.Surface | None = None
        self.fullscreen: bool = True
        self.width: int = 0
        self.height: int = 0
        self.settings = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.is_soundcard = True

        self.events_handler: EventsHandler = EventsHandler()
        self.frame: int = 0  # frame counter

    def load_settings(self, toml_file: str) -> Any:
        """Load the settings.

        Args:
        ----
            toml_file (str): The TOML file to load.

        Returns:
        -------
            Any: The settings.

        """
        self.settings = Settings.load(toml_file)
        self.fullscreen = self.settings.gui.fullscreen
        self.width = self.settings.gui.width
        self.height = self.settings.gui.height

    def init_gui(self, toml_file: str = "gui.toml") -> None:
        """Initialize the GUI.

        Args:
        ----
            toml_file (str): The TOML file to load.

        """
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
        print("Screen initialized.")

    def update(self) -> None:
        """Check the state."""
        if not self.events_handler.running:
            self.running = False

    def run(self):
        """Run the GUI."""
        if self.screen is None:
            msg = "Screen is not initialized. Call init_gui() before run()."
            raise ValueError(msg)
        if self.settings is None:
            msg = "Settings are not initialized. Call init_gui() before run()."
            raise ValueError(msg)
        while self.running:
            self.events_handler.handle_events()
            self.update()
            self.screen.fill(pygame.Color(self.settings.gui.colors.background))
            pygame.display.flip()
            self.clock.tick(self.settings.gui.fps)
            self.frame += 1
        pygame.quit()
