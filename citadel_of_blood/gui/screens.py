"""A module for game screens."""

import pygame

from citadel_of_blood.gui.colors import ColorPair, WidgetColors
from citadel_of_blood.gui.settings import GUISettings
from citadel_of_blood.gui.widgets import BaseWidget, Button


class GameScreen:
    """The screen class. This class is used to create a screen for the game, which can contain widgets."""

    def __init__(self, colors: ColorPair, settings: GUISettings | None = None) -> None:
        """Initialize the Screen class."""
        self.colors: ColorPair = colors
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
        self.surface.fill(self.colors.background_color)
        for widget in self.widgets:
            widget.update()
            widget.draw()
            self.surface.blit(widget.surface, (widget.x, widget.y))

    def update(self) -> None:
        """Update the screen."""
        pass  # todo: implement update method

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
        super().__init__(colors=ColorPair(background_color="0x333333", foreground_color="#ffffff"), settings=settings)
        self.is_active = True
        colors = WidgetColors(
            normal=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
            hover=ColorPair(background_color=(0x11, 0x11, 0x11), foreground_color=(0xFF, 0xFF, 0xFF)),
            click=ColorPair(background_color=(0xFF, 0xFF, 0xFF), foreground_color=(0, 0, 0)),
        )
        self.add_widget(
            Button(
                x=100,
                y=100,
                width=200,
                height=50,
                colors=colors,
                caption="Click me",
            )
        )
