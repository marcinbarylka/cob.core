"""Core module."""

from typing import Any

import pygame

from cob_core.gui.events import EventsHandler
from cob_core.gui.settings import Settings


class Game:
    """Game class.

    Parameters
    ----------
        screen (pygame.Surface): The screen.
        fullscreen (bool): Fullscreen mode.
        width (int): The width.
        height (int): The height.
        settings (Any): The settings.
        clock (pygame.time.Clock): The clock.
        running (bool): Running state.

        events_handler (EventsHandler): The events handler.

    """

    def __init__(self) -> None:
        """Initialize the Game class."""
        self.screen: pygame.Surface | None = None
        self.fullscreen: bool = True
        self.width: int = 0
        self.height: int = 0
        self.settings = None
        self.clock = pygame.time.Clock()
        self.running = True

        self.events_handler: EventsHandler = EventsHandler()

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
        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)
        self.screen = (
            pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            if self.fullscreen
            else pygame.display.set_mode((self.width, self.height))
        )
        pygame.display.set_caption(self.settings.gui.caption)

    def update(self) -> None:
        """Check the state."""
        if not self.events_handler.running:
            self.running = False

    def run(self):
        """Run the GUI."""
        while self.running:
            self.events_handler.handle_events()
            self.update()
            self.screen.fill(pygame.Color(self.settings.gui.colors.background))
            pygame.display.flip()
            self.clock.tick(self.settings.gui.fps)
        pygame.quit()
