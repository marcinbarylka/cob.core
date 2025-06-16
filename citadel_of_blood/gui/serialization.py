"""Helper functions for the GUI module."""

from pathlib import Path
from typing import TypeVar

import pygame

from citadel_of_blood.errors.engine_errors import ColorError
from citadel_of_blood.gui.types import GUIColor

SF = TypeVar("SF", bound="SerializableFont")


class SerializableFont:
    """Serialized font class."""

    def __init__(self, font_path: str | Path, size: int, bold: bool = False, italic: bool = False):
        """Initialize the SerializedFont class."""
        self.font_path = font_path
        self.size = size
        self.bold = bold
        self.italic = italic
        self.font = pygame.font.Font(font_path, size)
        self.font.bold = bold
        self.font.italic = italic

    def render(self, caption: str, antialias: bool = True, color: GUIColor = (0xFF, 0xFF, 0xFF)) -> pygame.Surface:
        """Render the font.

        Args:
            caption (str): The caption to render.
            antialias (bool): Whether to use antialiasing.
            color (GUIColor): The color of the caption.

        Returns:
            pygame.Surface: The rendered caption

        """
        return self.font.render(caption, antialias, color)

    def serialize(self) -> dict:
        """Serialize the font."""
        return {
            "font_path": self.font_path,
            "size": self.size,
            "bold": self.bold,
            "italic": self.italic,
        }

    @classmethod
    def deserialize(cls: type[SF], data: dict) -> SF:
        """Deserialize the font."""
        return cls(
            font_path=data["font_path"],
            size=data["size"],
            bold=data["bold"],
            italic=data["italic"],
        )


def serialize_surface(surface: pygame.Surface) -> dict:
    """Serialize a pygame surface to dict.

    Args:
        surface (pygame.Surface): The surface to serialize.

    Returns:
        dict: The serialized surface.
    """
    return {
        "size": surface.get_size(),
        "flags": surface.get_flags(),
        "depth": surface.get_bitsize(),
    }


def deserialize_surface(surface: dict) -> pygame.Surface:
    """Deserialize a pygame surface from dict.

    Args:
        surface (dict): The serialized surface.

    Returns:
        pygame.Surface: The deserialized surface.

    """
    return pygame.Surface(surface["size"], surface["flags"], surface["depth"])


def serialize_color(color: GUIColor) -> tuple[int, int, int] | str:
    """Converts a GUIColor into a JSON-serializable format.
    If 'color' is a pygame.Color or a tuple, returns a tuple (R, G, B).
    If it is a hex string (e.g., "#rrggbb"), returns it unchanged.
    """
    if isinstance(color, pygame.Color):
        return (
            color.r,
            color.g,
            color.b,
        )
    elif isinstance(color, tuple | str):
        return color
    else:
        msg = f"Unsupported color type: {type(color)}"
        raise ColorError(msg)


def deserialize_color(data: tuple[int, int, int] | str) -> pygame.Color:
    """Reconstructs a pygame.Color from the serialized data.
    If 'data' is a tuple, creates a pygame.Color with that tuple.
    If 'data' is a hex string, creates a pygame.Color from the string.
    """
    if isinstance(data, tuple | list):
        return pygame.Color(*data)
    elif isinstance(data, str):
        return pygame.Color(data)
    else:
        msg = f"Unsupported serialized color type: {type(data)}"
        raise ColorError(msg)
