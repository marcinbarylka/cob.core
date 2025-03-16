"""The base widget class."""

import abc
import dataclasses
import enum
import uuid
from typing import Any

import pygame

from citadel_of_blood.gui.colors import ColorPair, WidgetColors
from citadel_of_blood.gui.serialization import deserialize_surface, serialize_surface


class WidgetStateEnum(enum.Enum):
    """Enum for widget states."""

    NORMAL = "normal"
    HOVER = "hover"
    MOUSE_DOWN = "mouse_down"
    MOUSE_UP = "mouse_up"
    CLICK = "click"


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

    def __init__(self, x, y, width, height, colors: WidgetColors, id: str = ""):
        """Initialize the BaseWidget class.

        Additional Attributes:
            active (bool): Whether the widget is active.
            surface (pygame.Surface): The surface for the widget.
        """
        self.id: str = id or self.create_id()

        self.x: int = x
        self.y: int = y
        if width <= 0 or height <= 0:
            msg = "Width and height must be greater than 0."
            raise ValueError(msg)
        self.width: int = width
        self.height: int = height
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)

        self.colors: WidgetColors = colors
        self._render_colors: ColorPair = self.colors.normal

        self.is_active: bool = True
        self.is_visible: bool = True
        self.surface: pygame.Surface = pygame.Surface((width, height))

        self.state = WidgetStateEnum.NORMAL

    def create_id(self) -> str:
        """Create an ID."""
        return f"{self.__class__.__name__}_{uuid.uuid4()}"

    def serialize(self) -> dict[str, Any]:
        """Convert the widget to a dictionary.

        Returns:
            dict[str, Any]: The widget as a dictionary.

        """
        data = self.__dict__.copy()
        data["colors"] = dataclasses.asdict(data["colors"])
        data["rect"] = self.rect.x, self.rect.y, self.rect.width, self.rect.height
        data["surface"] = serialize_surface(self.surface)
        return data

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> "BaseWidget":
        """Create a widget from a dictionary.

        Args:
            data: dict[str, Any]: The data to create the widget from.

        Returns:
            BaseWidget: The widget.

        """
        obj = cls(
            x=data["x"],
            y=data["y"],
            width=data["width"],
            height=data["height"],
            colors=WidgetColors(**data["colors"]),
            id=data["id"],
        )
        obj.state = data["state"]
        obj.is_active = data["is_active"]
        obj.is_visible = data["is_visible"]

        rect_data = data["rect"]
        if rect_data:
            obj.rect = pygame.Rect(rect_data)

        surface_data = data.get("surface")
        if surface_data:
            obj.surface = deserialize_surface(surface_data)
        else:
            obj.surface = pygame.Surface((obj.width, obj.height))
        return obj
