"""Widgets for the GUI."""

import abc

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
    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle an event. This method should be implemented by the subclass.

        Args:
          event: pygame.event.Event: 

        Returns:

        """

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        foreground_color: GUIColor | None,
        background_color: GUIColor | None,
        id: str | None = None,
    ):
        """Initialize the BaseWidget class.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            width (int): The width.
            height (int): The height.
            foreground_color (GUIColor | None): The foreground color.
            background_color (GUIColor | None): The background color.
            id (str | None): The ID.

        """
    def __init__(self, id, x, y, width, height, background_color, foreground_color):
        """Initialize the BaseWidget class.

        Additional Attributes:
            active (bool): Określa, czy widżet jest aktywny.
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

import uuid

    def create_id(self) -> str:
        """Create an ID."""
        return f"{self.__class__.__name__}_{uuid.uuid4()}"

