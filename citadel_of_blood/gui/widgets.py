"""Widgets for the GUI."""

import abc
import uuid

import pygame

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
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle an event. This method should be implemented by the subclass.

        Args:
          event: pygame.event.Event:

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

        self.active: bool = True
        self.surface: pygame.Surface = pygame.Surface((width, height))

    def create_id(self) -> str:
        """Create an ID."""
        return f"{self.__class__.__name__}_{uuid.uuid4()}"


class Button(BaseWidget):
    """The button class."""

    def __init__(self, x, y, width, height, background_color, foreground_color, caption, id: str = ""):
        """Initialize the Button class."""
        super().__init__(x, y, width, height, background_color, foreground_color, id)
        self.caption = caption
        self.font: pygame.font.Font = pygame.font.Font(None, 36)  # todo: make this configurable

    def draw(self) -> None:
        """Draw the button."""
        pygame.draw.rect(self.surface, self.background_color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.caption, True, self.foreground_color)
        text_rect = text.get_rect(center=self.rect.center)
        self.surface.blit(text, text_rect)

    def update(self) -> None:
        """Update the button."""
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle an event."""
        if event.type == pygame.MOUSEBUTTONDOWN:  # noqa: SIM102
            if self.rect.collidepoint(event.pos):
                print(f"Button {self.id} clicked.")
                self.active = False
                self.on_click()
        # hover effect
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.on_hover_in()
        else:
            self.on_hover_out()

    def on_click(self) -> None:
        """The on click event."""
        pass

    def on_hover_in(self) -> None:
        """The on hover in event."""
        pass

    def on_hover_out(self) -> None:
        """The on hover out event."""
        pass
