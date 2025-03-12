"""A module for game screens."""

import pygame

from citadel_of_blood.gui.types import GUIColor
from citadel_of_blood.gui.widgets import BaseWidget


class GameScreen:
    """The screen class."""

    def __init__(self, background_color: GUIColor) -> None:
        """Initialize the Screen class."""
        self.background_color: GUIColor = background_color
        self.widgets: list[BaseWidget] = []
        self.surface: pygame.Surface = pygame.Surface((0, 0))

    def add_widget(self, widget) -> None:
        """Add a widget to the screen."""
        self.widgets.append(widget)

    def draw(self, screen) -> None:
        """Draw the screen."""
        screen.fill(self.background_color)
        for widget in self.widgets:
            widget.draw()

    def update(self) -> None:
        """Update the screen."""
        for widget in self.widgets:
            widget.update()

    def handle_event(self, event) -> None:
        """Handle an event."""
        for widget in self.widgets:
            widget.handle_event(event)
