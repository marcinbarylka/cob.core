"""A module for game screens."""

import pygame

from citadel_of_blood.gui.settings import GUISettings
from citadel_of_blood.gui.types import GUIColor
from citadel_of_blood.gui.widgets import BaseWidget, Button


class GameScreen:
    """The screen class. This class is used to create a screen for the game, which can contain widgets."""

    def __init__(self, background_color: GUIColor, settings: GUISettings | None = None) -> None:
        """Initialize the Screen class."""
        self.background_color: GUIColor = background_color
        self.widgets: list[BaseWidget] = []

        self.surface: pygame.Surface = (
            pygame.Surface(settings.gui.width, settings.gui.height) if settings else pygame.Surface((1920, 1080))
        )
        self.is_active: bool = False
        self.settings: GUISettings | None = settings

    def add_widget(self, widget: BaseWidget) -> None:
        """Add a widget to the screen."""
        self.widgets.append(widget)

    def draw(self) -> None:
        """Draw the screen."""
        self.surface.fill(self.background_color)
        for widget in self.widgets:
            widget.draw()
            self.surface.blit(widget.surface, (widget.x, widget.y))

    def update(self) -> None:
        """Update the screen."""
        self.surface.fill(self.background_color)
        for widget in self.widgets:
            widget.update()
            self.surface.blit(widget.surface, (widget.x, widget.y))

    def handle_events(self, events: list[pygame.event.Event] | None = None) -> list[pygame.event.Event] | None:
        """Handle an event."""
        if not events:
            events = pygame.event.get()
        if not self.is_active:
            return
        for widget in self.widgets:
            widget.handle_events(events)
        return events


class DefaultScreen(GameScreen):
    """The default screen class."""

    def __init__(self, settings: GUISettings | None = None) -> None:
        """Initialize the DefaultScreen class."""
        super().__init__(background_color="#ff0000", settings=settings)
        self.is_active = True
        self.add_widget(
            Button(
                x=100,
                y=100,
                width=200,
                height=50,
                background_color="#ffffff",
                foreground_color="#000000",
                caption="Click me",
            )
        )
