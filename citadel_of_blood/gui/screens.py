"""A module for game screens.

This module provides base classes for creating and managing game screens.
Each screen can contain multiple widgets and handle their rendering and events.
"""

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.errors.gui_errors import ScreenError
from citadel_of_blood.gui.colors import ColorPair, ColorsEnum, WidgetColors
from citadel_of_blood.gui.serialization import SerializableFont
from citadel_of_blood.gui.settings import Settings
from citadel_of_blood.gui.widgets import BaseWidget
from citadel_of_blood.gui.widgets.buttons import PixelButton


class GameScreen:
    """Base class for game screens.

    This class provides core functionality for creating screens that can contain
    and manage multiple widgets, handle events, and perform rendering.

    Attributes:
        colors (ColorPair): The color scheme for the screen
        widgets (list[BaseWidget]): List of widgets contained in the screen
        surface (pygame.Surface): The screen's drawing surface
        is_active (bool): Whether the screen is currently active
        settings (Settings | None): GUI settings for the screen
    """

    def __init__(self, colors: ColorPair, settings: Settings | None = None) -> None:
        """Initialize a new game screen.

        Args:
            colors (ColorPair): The color scheme for the screen
            settings (Settings | None, optional): GUI settings. Defaults to None.
        """
        self.colors: ColorPair = colors
        self.widgets: list[BaseWidget] = []
        self.is_active: bool = False
        self.settings: Settings | None = settings

        if settings:
            self.surface = pygame.Surface((settings.gui.width, settings.gui.height))
        else:
            self.surface = pygame.Surface((1920, 1080))

    def add_widget(self, widget: BaseWidget) -> None:
        """Add a widget to the screen.

        Args:
            widget (BaseWidget): The widget to add
        """
        self.widgets.append(widget)

    def draw(self) -> None:
        """Draw the screen and all its widgets.

        This method fills the screen with the background color and then
        draws all widgets in their current state.
        """
        self.surface.fill(self.colors.background_color)
        for widget in self.widgets:
            widget.update()
            widget.draw()
            self.surface.blit(widget.surface, (widget.x, widget.y))

    def update(self) -> None:
        """Update the screen state.

        This method should be overridden by subclasses to implement
        screen-specific update logic.
        """
        pass

    def handle_events(self, events: list[pygame.event.Event] | None = None) -> list[pygame.event.Event] | None:
        """Handle pygame events for the screen and its widgets.

        Args:
            events (list[pygame.event.Event] | None, optional): List of events to handle.
                If None, gets current events. Defaults to None.

        Returns:
            list[pygame.event.Event] | None: The processed events
        """
        if not events:
            events = pygame.event.get()
        if not self.is_active:
            return events
        for widget in self.widgets:
            widget.handle_events(events)
        return events


class DefaultScreen(GameScreen):
    """Default implementation of a game screen.

    This screen provides a basic setup with a sample button widget.
    It serves as an example of how to create custom screen classes.
    """

    DEFAULT_COLORS = ColorPair(background_color=ColorsEnum.DEFAULT_BACKGROUND, foreground_color=ColorsEnum.WHITE)

    DEFAULT_WIDGET_COLORS = WidgetColors(
        normal=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
        hover=ColorPair(background_color=(0x11, 0x11, 0x11), foreground_color=(0xFF, 0xFF, 0xFF)),
        click=ColorPair(background_color=(0xFF, 0xFF, 0xFF), foreground_color=(0, 0, 0)),
    )

    def __init__(self, settings: Settings | None = None) -> None:
        """Initialize the default screen.

        Args:
            settings (Settings | None, optional): GUI settings. Defaults to None.
        """
        super().__init__(colors=self.DEFAULT_COLORS, settings=settings)
        self.is_active = True
        self._setup_widgets()

    def _setup_widgets(self) -> None:
        """Set up the default widgets for this screen."""
        try:
            font = SerializableFont(
                font_path=PROJECT_ROOT / "assets/fonts/alagard.ttf",
                size=16,
            )
            self.add_widget(
                PixelButton(
                    x=100,
                    y=100,
                    width=200,
                    caption="Click me",
                    font=font,
                )
            )
        except (FileNotFoundError, pygame.error) as e:
            raise ScreenError("widget_initialization_failed", e) from e
