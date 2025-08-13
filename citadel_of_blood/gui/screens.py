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
from citadel_of_blood.gui.widgets.buttons import ExitButton, PixelButton
from citadel_of_blood.gui.widgets.modal import Modal
from citadel_of_blood.gui.widgets.panels import Panel


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
        self.settings: Settings | None = Settings.instance()
        self.modal: Modal | None = None

        if settings:
            self.surface = pygame.Surface((settings.gui.width, settings.gui.height))
        else:
            self.surface = pygame.Surface((1920, 1080))

        Settings.set_active_screen(self)  # Set the active screen

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
        for widget in self.widgets:
            if self.settings:
                widget.settings = self.settings
            widget.update()

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

        # If a modal is visible, let only the topmost modal handle events
        top_modal: Modal | None = None
        for widget in reversed(self.widgets):
            if isinstance(widget, Modal) and widget.is_visible:
                top_modal = widget
                break

        if top_modal is not None:
            top_modal.handle_events(events)
            return events

        # Otherwise, dispatch to all widgets as usual
        for widget in self.widgets:
            widget.handle_events(events)
        return events

    def find_widget_by_id(self, widget_id: str) -> BaseWidget | None:
        """Find a widget by its ID.

        Args:
            widget_id (str): The ID of the widget to find

        Returns:
            BaseWidget | None: The found widget or None if not found

        """
        for widget in self.widgets:
            if widget.id == widget_id:
                return widget
        return None

    def find_widgets_by_type(self, widget_type: type[BaseWidget]) -> list[BaseWidget]:
        """Find all widgets of a specific type.

        Args:
            widget_type (type[BaseWidget]): The type of widgets to find

        Returns:
            list[BaseWidget]: List of widgets of the specified type

        """
        return [widget for widget in self.widgets if isinstance(widget, widget_type)]

    def remove_widget(self, widget: BaseWidget) -> None:
        """Remove a widget from the screen.

        Args:
            widget (BaseWidget): The widget to remove

        """
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            msg = f"Widget with ID {widget.id} not found in screen."
            raise ScreenError("widget_not_found", msg)

    def show_modal(self, modal: Modal) -> None:
        """Show the given modal and ensure it's the only visible modal.

        This removes any other Modal instances from the widget list,
        assigns self.modal, and moves the shown modal to the top.
        """
        # Hide and remove any other modals
        for w in list(self.widgets):
            if isinstance(w, Modal) and w is not modal:
                w.hide()
                self.widgets.remove(w)

        # Ensure the modal is in widgets and on top
        if modal in self.widgets:
            self.widgets.remove(modal)
        self.widgets.append(modal)

        self.modal = modal
        modal.show()


class DefaultScreen(GameScreen):
    """Default implementation of a game screen.

    This screen provides a basic setup with a sample button widget.
    It serves as an example of how to create custom screen classes.
    """

    DEFAULT_COLORS = ColorPair(background_color=ColorsEnum.DEFAULT_BACKGROUND, foreground_color=ColorsEnum.WHITE)

    DEFAULT_WIDGET_COLORS = WidgetColors(
        normal=ColorPair(background_color=ColorsEnum.GRAY, foreground_color=ColorsEnum.WHITE),
        hover=ColorPair(background_color=(0x11, 0x11, 0x11, 0xFF), foreground_color=ColorsEnum.WHITE),
        click=ColorPair(background_color=ColorsEnum.WHITE, foreground_color=ColorsEnum.BLACK),
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
                size=20,
            )
            modal = Modal(
                title="Welcome",
                message="This is a sample modal dialog.",
                width=400,
                height=200,
                buttons=["OK", "Cancel"],
            )
            self.add_widget(
                Panel(
                    x=10,
                    y=10,
                    width=600,
                    height=400,
                )
            )
            self.add_widget(
                PixelButton(
                    x=100,
                    y=100,
                    width=200,
                    caption="Disabled",
                    font=font,
                    play_sfx=True,
                    enabled=False,
                )
            )
            self.add_widget(
                OpenModalButton(
                    x=350,
                    y=100,
                    width=200,
                    caption="Open modal",
                    font=font,
                    play_sfx=True,
                    modal=modal,
                )
            )
            self.add_widget(
                ExitButton(
                    x=100,
                    y=200,
                    font=font,
                    play_sfx=True,
                )
            )

        except (FileNotFoundError, pygame.error) as e:
            raise ScreenError("widget_initialization_failed", e) from e


class OpenModalButton(PixelButton):
    """A button that opens a modal dialog when clicked."""

    def __init__(
        self,
        modal: Modal,
        x: int,
        y: int,
        width: int,
        caption: str,
        font: SerializableFont,
        play_sfx: bool = True,
    ) -> None:
        """Initialize the OpenModalButton."""
        super().__init__(x=x, y=y, width=width, caption=caption, font=font, play_sfx=play_sfx)
        self.modal = modal

    def on_click(self) -> None:
        """Open a modal dialog when the button is clicked."""
        print("Opening modal dialog...")
        active_screen = Settings.get_active_screen()  # Get the active screen
        if active_screen:
            active_screen.show_modal(self.modal)
        else:
            print("No active screen found.")
