"""Helper functions for the GUI module."""

from pathlib import Path
from typing import TypeVar

import pygame

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
        """Render the font with the given caption and settings."""

    def serialize(self) -> dict:
        """Convert the font into a dictionary."""

    @classmethod
    def deserialize(cls: type[SF], data: dict) -> SF:
        """Reconstruct a font from the serialized dictionary."""


def serialize_surface(surface: pygame.Surface) -> dict:
    """Convert a pygame surface into a dictionary."""


def deserialize_surface(surface: dict) -> pygame.Surface:
    """Reconstruct a pygame surface from the serialized dictionary."""


def serialize_color(color: GUIColor) -> tuple[int, int, int] | str:
    """Convert a GUIColor into a JSON-serializable format."""


def deserialize_color(data: tuple[int, int, int] | str) -> pygame.Color:
    """Reconstruct a pygame.Color from the serialized data."""
