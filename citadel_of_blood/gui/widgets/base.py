"""The base widget class."""

import abc
import dataclasses
import enum
import string
from typing import Any, TypeVar, cast

import pygame
from nanoid import generate
from pygame import Rect
from pygame.surface import Surface

from citadel_of_blood.errors.gui_errors import WidgetError
from citadel_of_blood.gui.colors import ColorPair, WidgetColors
from citadel_of_blood.gui.serialization import deserialize_surface, serialize_surface
from citadel_of_blood.gui.settings import Settings

T = TypeVar("T", bound="BaseWidget")


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
    def on_hover_in(self) -> None:
        """The on hover in event."""

    @abc.abstractmethod
    def on_hover_out(self) -> None:
        """The on hover out event."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        colors: WidgetColors,
        id: str = "",
    ) -> None:
        """Initialize the BaseWidget class.

        Args:
            x: The x-coordinate of the widget.
            y: The y-coordinate of the widget.
            width: The width of the widget.
            height: The height of the widget.
            colors: The colors of the widget.
            id: The ID of the widget.

        Raises:
            WidgetError: If width or height is invalid, or if colors are invalid.
        """
        self.id: str = id or self.create_id()

        self.x: int = x
        self.y: int = y
        if width <= 0 or height <= 0:
            raise WidgetError("invalid_dimensions", f"Width and height must be greater than 0, got {width}x{height}")
        self.width: int = width
        self.height: int = height

        self.colors: WidgetColors = colors
        self._render_colors: ColorPair = self.colors.normal

        self.is_active: bool = True
        self.is_visible: bool = True
        self.surface: Surface = Surface((width, height), pygame.SRCALPHA)
        self.state: WidgetStateEnum = WidgetStateEnum.NORMAL

        self.settings: Settings | None = None

    def create_id(self) -> str:
        """Create a unique ID for the widget."""
        alpha = string.ascii_letters + string.digits
        return f"{self.__class__.__name__}_{generate(alpha, 8)}"

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle pygame events for the widget.

        Args:
            events: The list of Pygame events to handle.
        """
        if not self.is_active or not self.is_visible:
            return

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    if self.state != WidgetStateEnum.HOVER:
                        self.on_hover_in()
                        self.state = WidgetStateEnum.HOVER
                else:
                    if self.state == WidgetStateEnum.HOVER:
                        self.on_hover_out()
                        self.state = WidgetStateEnum.NORMAL

    def serialize(self) -> dict[str, Any]:
        """Convert the widget to a dictionary.

        Returns:
            The widget as a dictionary.
        """
        data = self.__dict__.copy()
        data["colors"] = dataclasses.asdict(data["colors"])
        data["rect"] = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        data["surface"] = serialize_surface(self.surface)
        data["state"] = self.state.value
        return data

    @classmethod
    def deserialize(cls: type[T], data: dict[str, Any]) -> T:
        """Create a widget from a dictionary.

        Args:
            data: The data to create the widget from.

        Returns:
            The deserialized widget instance.

        Raises:
            WidgetError: If deserialization fails.
        """
        try:
            obj = cls(
                x=data["x"],
                y=data["y"],
                width=data["width"],
                height=data["height"],
                colors=WidgetColors(**data["colors"]),
                id=data["id"],
            )
            obj.state = WidgetStateEnum(data["state"])
            obj.is_active = data["is_active"]
            obj.is_visible = data["is_visible"]

            rect_data = data["rect"]
            if rect_data:
                obj.rect = pygame.Rect(*rect_data)

            surface_data = data.get("surface")
            if surface_data:
                try:
                    obj.surface = deserialize_surface(surface_data)
                except Exception as e:
                    raise WidgetError("surface_deserialization_failed", str(e)) from e
            return cast(T, obj)
        except KeyError as e:
            raise WidgetError("missing_required_field", f"Missing field: {e}") from e
        except Exception as e:
            raise WidgetError("deserialization_failed", str(e)) from e

    def __repr__(self) -> str:
        """Return a string representation of the widget."""
        return (
            f"{self.__class__.__name__}(id={self.id}, x={self.x}, y={self.y}, "
            f"width={self.width}, height={self.height})"
        )

    def __str__(self) -> str:
        """Return a string representation of the widget."""
        return self.id

    @property
    def rect(self):
        """Get the rectangle of the widget."""
        return Rect(self.x, self.y, self.width, self.height)

    @rect.setter
    def rect(self, value: Rect) -> None:
        """Set the rectangle of the widget."""
        self.x = value.x
        self.y = value.y
        self.width = value.width
        self.height = value.height
