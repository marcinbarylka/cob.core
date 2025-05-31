"""The button class."""

from pathlib import Path
from typing import Any, ClassVar

import pygame
from pygame.surface import Surface

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.errors.gui_errors import WidgetError
from citadel_of_blood.gui.colors import WidgetColors
from citadel_of_blood.gui.serialization import SerializableFont
from citadel_of_blood.gui.widgets import WidgetStateEnum
from citadel_of_blood.gui.widgets.base import BaseWidget
from citadel_of_blood.gui.widgets.mixins import ClickableMixin


class Button(BaseWidget, ClickableMixin):
    """The button class."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        colors: WidgetColors,
        caption: str = "Click me",
        font: SerializableFont | None = None,
        id: str = "",
    ) -> None:
        """Initialize the Button class.

        Args:
            x: The x-coordinate of the button
            y: The y-coordinate of the button
            width: The width of the button
            height: The height of the button
            colors: The color scheme for the button
            caption: The button text
            font: Custom font for the button text
            id: Unique identifier for the button

        Raises:
            WidgetError: If font initialization fails
        """
        super().__init__(x, y, width, height, colors, id)
        self.caption: str = caption
        try:
            self.font: SerializableFont = (
                font if font else SerializableFont(font_path=PROJECT_ROOT / "assets/fonts/Roboto-Regular.ttf", size=16)
            )
        except Exception as e:
            raise WidgetError("font_initialization_failed", str(e)) from e

    @staticmethod
    def _raise_missing_asset(path: Path) -> None:
        """Raise an error if a required asset is missing.

        Args:
            path: The path to the required asset

        Raises:
            WidgetError: If the asset is missing

        """
        raise WidgetError("missing_asset", f"Required asset not found: {path}")

    def set_font(self, font: SerializableFont) -> None:
        """Set the button font.

        Args:
            font: The new font to use
        """
        self.font = font

    def draw(self) -> None:
        """Draw the button with its current state."""
        self.surface.fill(self._render_colors.background_color)
        try:
            text = self.font.render(caption=self.caption, color=self._render_colors.foreground_color)
            text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
            self.surface.blit(text, text_rect)
        except Exception as e:
            raise WidgetError("text_rendering_failed", str(e)) from e

    def update(self) -> None:
        """Update the button's appearance based on its state."""
        match self.state:
            case WidgetStateEnum.NORMAL:
                self._render_colors = self.colors.normal
            case WidgetStateEnum.HOVER:
                self._render_colors = self.colors.hover
            case WidgetStateEnum.MOUSE_DOWN:
                self._render_colors = self.colors.click or self.colors.hover
            case WidgetStateEnum.MOUSE_UP:
                self._render_colors = self.colors.hover

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle an event."""
        if not self.is_active or not self.is_visible:
            return

        # Delegate click events to mixin method
        super().handle_events(events)
        self.handle_click_events(events)

    def on_mouse_down(self) -> None:
        """Handle mouse down event."""

    def on_mouse_up(self) -> None:
        """Handle mouse up event."""

    def on_click(self) -> None:
        """Handle click event."""
        print(f"Button {self.id} clicked.")

    def on_hover_in(self) -> None:
        """Handle hover in event."""

    def on_hover_out(self) -> None:
        """Handle hover out event."""

    def serialize(self) -> dict[str, Any]:
        """Serialize the button to a dictionary.

        Returns:
            The serialized button data
        """
        data = super().serialize()
        data["caption"] = self.caption
        data["font"] = self.font.serialize()
        return data

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> "Button":
        """Create a button from serialized data.

        Args:
            data: The serialized button data

        Returns:
            The deserialized button instance

        Raises:
            WidgetError: If deserialization fails
        """
        try:
            obj = super().deserialize(data)
            obj.caption = data["caption"]
            obj.font = SerializableFont.deserialize(data["font"])
        except Exception as e:
            raise WidgetError("button_deserialization_failed", str(e)) from e
        else:
            return obj


class GothicButton(Button):
    """Gothic-styled button with custom graphics."""

    # Cache for button graphics
    _BUTTON_ASSETS: ClassVar[dict[str, Surface]] = {}
    _ASSET_PATHS: ClassVar[dict[str, Path]] = {
        "normal_left": PROJECT_ROOT / "assets/gui/button-normal-left.png",
        "normal_right": PROJECT_ROOT / "assets/gui/button-normal-right.png",
        "hover_left": PROJECT_ROOT / "assets/gui/button-hover-left.png",
        "hover_right": PROJECT_ROOT / "assets/gui/button-hover-right.png",
    }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the Gothic button.

        Raises:
            WidgetError: If button assets cannot be loaded
        """
        super().__init__(*args, **kwargs)
        if not self._BUTTON_ASSETS:
            self._load_assets()

    @classmethod
    def _load_assets(cls) -> None:
        """Load and cache button graphics.

        Raises:
            WidgetError: If any asset fails to load
        """
        try:
            for name, path in cls._ASSET_PATHS.items():
                if not path.exists():
                    cls._raise_missing_asset(path)
                cls._BUTTON_ASSETS[name] = pygame.image.load(str(path)).convert_alpha()
        except Exception as e:
            raise WidgetError("asset_loading_failed", str(e)) from e

    def draw(self) -> None:
        """Draw the gothic button with its current state."""
        self.surface.fill((0, 0, 0, 0))  # Clear with transparency

        if self.state in [WidgetStateEnum.HOVER, WidgetStateEnum.MOUSE_DOWN]:
            left_img = self._BUTTON_ASSETS["hover_left"]
            right_img = self._BUTTON_ASSETS["hover_right"]
        else:
            left_img = self._BUTTON_ASSETS["normal_left"]
            right_img = self._BUTTON_ASSETS["normal_right"]

        # Draw button parts
        self.surface.blit(left_img, (0, 0))
        self.surface.blit(right_img, (self.rect.width - right_img.get_width(), 0))

        # Draw text
        try:
            text = self.font.render(caption=self.caption, color=self._render_colors.foreground_color)
            text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
            self.surface.blit(text, text_rect)
        except Exception as e:
            raise WidgetError("text_rendering_failed", str(e)) from e
