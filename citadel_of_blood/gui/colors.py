"""Color configurations for widgets."""

from dataclasses import dataclass

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
        """Represents the ColorPair instance as a string.

        Returns:
            str: The string representation of the ColorPair instance
        """
        return f"ColorPair(bg={self.background_color}, fg={self.foreground_color})"

    def serialize(self) -> dict:
        """Serializes the ColorPair into a dictionary.

        Returns:
            dict: The serialized dictionary
        """
        return {
            "background_color": serialize_color(self.background_color),
            "foreground_color": serialize_color(self.foreground_color),
        }

    @classmethod
    def deserialize(cls, data: dict) -> "ColorPair":
        """Creates a ColorPair instance from a serialized dictionary.

        Args:
            data (dict): The serialized dictionary

        Returns:
            ColorPair: The deserialized ColorPair instance

        """
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
    hover: ColorPair
    click: ColorPair | None = None

    def __repr__(self) -> str:
        """Represents the WidgetColors instance as a string.

        Returns:
            str: The string representation of the WidgetColors instance
        """
        return f"WidgetColors(normal={self.normal}, hover={self.hover}, click={self.click})"

    def serialize(self) -> dict:
        """Serializes the WidgetColors into a dictionary.

        Returns:
            dict: The serialized dictionary
        """
        return {
            "normal": self.normal.serialize(),
            "hover": self.hover.serialize(),
            "click": self.click.serialize() if self.click is not None else None,
        }

    @classmethod
    def deserialize(cls, data: dict) -> "WidgetColors":
        """Creates a WidgetColors instance from a serialized dictionary.

        Args:
            data (dict): The serialized dictionary

        Returns:
            WidgetColors: The deserialized WidgetColors instance

        """
        return cls(
            normal=ColorPair.deserialize(data["normal"]),
            hover=ColorPair.deserialize(data["hover"]),
            click=ColorPair.deserialize(data["click"]) if data.get("click") is not None else None,
        )


DEFAULT_WIDGET_COLORS = WidgetColors(
    normal=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
    hover=ColorPair(background_color=(0x11, 0x11, 0x11), foreground_color=(0xFF, 0xFF, 0xFF)),
    click=ColorPair(background_color=(0x55, 0x55, 0x55), foreground_color=(0xFF, 0xFF, 0xFF)),
)


def validate_color(color: GUIColor) -> None:
    """Validate that the color is a valid RGB tuple.

    Args:
        color (GUIColor): The color to validate.

    Raises:
        ValueError: If the color is invalid.
    """
    if not (isinstance(color, tuple) and len(color) == 3):
        msg = f"Color must be a tuple of three integers (R, G, B), got {color}."
        raise ValueError(msg)
    if not all(0 <= c <= 255 for c in color):
        msg = f"Color values must be between 0 and 255, got {color}."
        raise ValueError(msg)


def validate_ratio(ratio: float) -> None:
    """Validate that the ratio is between 0 and 1.

    Args:
        ratio (float): The ratio to validate.

    Raises:
        ValueError: If the ratio is invalid.
    """
    if not 0 <= ratio <= 1:
        msg = f"Ratio must be between 0 and 1, got {ratio}."
        raise ValueError(msg)


def dim(color: GUIColor, shadow_ratio: float = 0.5) -> GUIColor:
    """Dim a color by a factor.

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
    """Tint a color by a factor.

    Args:
        color (GUIColor): The color to tint.
        shadow_ratio (float): The ratio to tint by.

    Returns:
        GUIColor: The tinted color.
    """
    validate_color(color)
    validate_ratio(shadow_ratio)
    return tuple(int(c + (255 - c) * shadow_ratio) for c in color)
