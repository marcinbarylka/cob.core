"""Color configurations for widgets."""

from dataclasses import dataclass
from typing import Any

import pygame

from citadel_of_blood.gui.serialization import deserialize_color, serialize_color
from citadel_of_blood.gui.types import GUIColor


@dataclass
class ColorPair:
    """Represents a pair of colors.

    Attributes:
        background_color (GUIColor): The background color.
        foreground_color (GUIColor): The foreground color.

    """

    background_color: GUIColor
    foreground_color: GUIColor

    def __repr__(self) -> str:
        """Return the string representation of the ColorPair instance."""
        return f"ColorPair(bg={self.background_color}, fg={self.foreground_color})"

    def serialize(self) -> dict:
        """Convert the ColorPair into a dictionary."""
        return {
            "background_color": serialize_color(self.background_color),
            "foreground_color": serialize_color(self.foreground_color),
        }

    @classmethod
    def deserialize(cls, data: dict) -> "ColorPair":
        """Create a ColorPair instance from a serialized dictionary."""
        return cls(
            background_color=deserialize_color(data["background_color"]),
            foreground_color=deserialize_color(data["foreground_color"]),
        )


@dataclass
class WidgetColors:
    """Represents the color configurations for a widget in different states.

    Attributes:
        normal (ColorPair): Colors for the normal state.
        hover (ColorPair): Colors for the hover state.
        click (ColorPair | None): Colors for the click state (optional).

    """

    normal: ColorPair
    hover: ColorPair | None = None
    click: ColorPair | None = None

    def __repr__(self) -> str:
        """Return the string representation of the WidgetColors instance."""
        return f"WidgetColors(normal={self.normal}, hover={self.hover}, click={self.click})"

    def serialize(self) -> dict:
        """Convert the WidgetColors into a dictionary."""
        return {
            "normal": self.normal.serialize(),
            "hover": self.hover.serialize(),
            "click": self.click.serialize() if self.click is not None else None,
        }

    @classmethod
    def deserialize(cls, data: dict) -> "WidgetColors":
        """Create a WidgetColors instance from a serialized dictionary."""
        return cls(
            normal=ColorPair.deserialize(data["normal"]),
            hover=ColorPair.deserialize(data["hover"]),
            click=(ColorPair.deserialize(data["click"]) if data.get("click") is not None else None),
        )


DEFAULT_WIDGET_COLORS = WidgetColors(
    normal=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
    hover=ColorPair(background_color=(0x11, 0x11, 0x11), foreground_color=(0xFF, 0xFF, 0xFF)),
    click=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
)


def validate_color(value: Any) -> tuple[int, ...]:
    """Ensure the value is a valid color.

    Args:
        value (Any): The value to validate.

    Returns:
        tuple[int, ...]: A tuple representing the color in RGBA format.

    Raises:
        ValueError: If the value is not a valid color.

    """
    if isinstance(value, pygame.Color):
        return value.r, value.g, value.b, value.a
    if isinstance(value, tuple) and len(value) in (3, 4) and all(isinstance(c, int) and 0 <= c <= 255 for c in value):
        return value
    msg = (
        f"Invalid color value: {value!r}. Must be a tuple of 3 or 4 integers (0-255) "
        f"or pygame.Color, got {type(value).__name__}."
    )
    raise ValueError(msg)


def validate_ratio(ratio: float) -> None:
    """Ensure the ratio is between 0 and 1.

    Args:
        ratio (float): The ratio to validate.

    Raises:
        ValueError: If the ratio is invalid.

    """
    if not 0 <= ratio <= 1:
        msg = f"Ratio must be between 0 and 1, got {ratio}."
        raise ValueError(msg)


def dim(color: GUIColor, shadow_ratio: float = 0.5) -> GUIColor:
    """Reduce the brightness of a color by a factor.

    Args:
        color (GUIColor): The color to dim.
        shadow_ratio (float): The ratio to dim by.

    Returns:
        GUIColor: The dimmed color.

    """
    validate_color(color)
    validate_ratio(shadow_ratio)
    return tuple(int(c * shadow_ratio) for c in color)


def tint(color: GUIColor, shadow_ratio: float = 0.5) -> GUIColor:
    """Increase the brightness of a color by a factor.

    Args:
        color (GUIColor): The color to tint.
        shadow_ratio (float): The ratio to tint by.

    Returns:
        GUIColor: The tinted color.

    """
    validate_color(color)
    validate_ratio(shadow_ratio)
    return tuple(int(c + (255 - c) * shadow_ratio) for c in color)


class ColorsEnum:
    """Enum for predefined colors used in the GUI."""

    BLACK: pygame.Color = pygame.Color(0, 0, 0, 0xFF)
    WHITE: pygame.Color = pygame.Color(0xFF, 0xFF, 0xFF, 0xFF)
    GRAY: pygame.Color = pygame.Color(0x55, 0x55, 0x55, 0xFF)
    DEFAULT_BACKGROUND: pygame.Color = pygame.Color(0x20, 0x20, 0x20, 0xFF)
    PIXEL_BUTTON_INSIDE: pygame.Color = pygame.Color(0x34, 0x2A, 0x25, 0xFF)
    PIXEL_BUTTON_TEXT: pygame.Color = pygame.Color(0xFB, 0xE2, 0xBB, 0xFF)
    PIXEL_BUTTON_INSIDE_HOVER: pygame.Color = pygame.Color(0xD6, 0x9D, 0x67, 0x40)
    PANEL_BACKGROUND: pygame.Color = pygame.Color(0x34, 0x2A, 0x25, 0xFF)
    PANEL_FOREGROUND: pygame.Color = pygame.Color(0xFB, 0xE2, 0xBB, 0xFF)
    FADING_BAR: pygame.Color = pygame.Color(0x56, 0x32, 0x26, 0xFF)
    MODAL_BACKGROUND: pygame.Color = pygame.Color(0x34, 0x2A, 0x25, 0x80)
    SEGMENT_BLUE: pygame.Color = pygame.Color(0x60, 0x90, 0xCA, 0xFF)
    MONSTER_RED: pygame.Color = pygame.Color(0xFA, 0x5A, 0x38, 0xFF)

    @classmethod
    def get_color(cls, name: str) -> GUIColor:
        """Retrieve a color by its name.

        Args:
            name (str): The name of the color.

        Returns:
            GUIColor: The corresponding color tuple.

        """
        return getattr(cls, name.upper(), cls.BLACK)
