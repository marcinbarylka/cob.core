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
