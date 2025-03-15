"""Widgets for the GUI."""

import abc
import uuid

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.gui.types import GUIColor

# TODO: Add widgets for the GUI.


class BaseWidget(abc.ABC):
    """The base widget class."""

    @abc.abstractmethod
    def draw(self) -> None:
        """Draw the widget. This method should be implemented by the subclass."""

    @abc.abstractmethod
    def update(self) -> None:
        """Update the widget. This method should be implemented by the subclass."""

    @abc.abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle an event. This method should be implemented by the subclass.

        Args:
          events: list[pygame.event.Event]: The list of Pygame events to handle.

        """

    def __init__(self, x, y, width, height, background_color, foreground_color, id: str = ""):
        """Initialize the BaseWidget class.

        Additional Attributes:
            active (bool): Whether the widget is active.
            surface (pygame.Surface): The surface for the widget.
        """
        self.id = id or self.create_id()

        self.x = x
        self.y = y
        if width <= 0 or height <= 0:
            msg = "Width and height must be greater than 0."
            raise ValueError(msg)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

        self.background_color: GUIColor | None = background_color
        self.foreground_color: GUIColor | None = foreground_color

        self.is_active: bool = True
        self.surface: pygame.Surface = pygame.Surface((width, height))

        self.state = "normal"
        self.default_background_color = background_color
        self.default_foreground_color = foreground_color

    def create_id(self) -> str:
        """Create an ID."""
        return f"{self.__class__.__name__}_{uuid.uuid4()}"


class Button(BaseWidget):
    """The button class."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        background_color: GUIColor = (0, 0, 0),
        foreground_color: GUIColor = (0xFF, 0xFF, 0xFF),
        hover_background_color: GUIColor = (0xFF, 0xFF, 0xFF),
        hover_foreground_color: GUIColor = (0, 0, 0),
        caption: str = "Click me",
        id: str = "",
    ):
        """Initialize the Button class."""
        super().__init__(x, y, width, height, background_color, foreground_color, id)
        self.caption = caption
        self.font: pygame.font.Font = pygame.font.Font(
            PROJECT_ROOT / "assets/fonts/Roboto-Regular.ttf", 36
        )  # todo: make this configurable
        self.hover_background_color: GUIColor = hover_background_color
        self.hover_foreground_color: GUIColor = hover_foreground_color

    def draw(self) -> None:
        """Draw the button."""
        pygame.draw.rect(self.surface, self.background_color, self.rect)
        self.surface.fill(self.background_color)
        text = self.font.render(self.caption, True, self.foreground_color)
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.surface.blit(text, text_rect)

    def update(self) -> None:
        """Update the button."""

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle an event."""
        if not self.is_active:
            return
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  # noqa: SIM102
                if self.rect.collidepoint(event.pos):
                    self.on_click()
        # hover effect
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.state = "hover"
            self.on_hover_in()
        else:
            self.state = "normal"
            self.on_hover_out()

    def on_click(self) -> None:
        """The on click event."""
        print(f"Button {self.id} clicked.")

    def on_hover_in(self) -> None:
        """The on hover in event."""
        self.background_color = self.hover_background_color
        self.foreground_color = self.hover_foreground_color

    def on_hover_out(self) -> None:
        """The on hover out event."""
        self.background_color = self.default_background_color
        self.foreground_color = self.default_foreground_color
