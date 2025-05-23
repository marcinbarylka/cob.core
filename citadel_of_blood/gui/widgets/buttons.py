"""The button class."""

from typing import Any

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
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
    ):
        """Initialize the Button class."""
        super().__init__(x, y, width, height, colors, id)
        self.caption = caption
        self.font = (
            font if font else SerializableFont(font_path=PROJECT_ROOT / "assets/fonts/Roboto-Regular.ttf", size=16)
        )
        self._pressed: bool = False

    def set_font(self, font: SerializableFont) -> None:
        """Set the font."""
        self.font = font

    def draw(self) -> None:
        """Draw the button."""
        pygame.draw.rect(self.surface, self._render_colors.background_color, self.rect)
        self.surface.fill(self._render_colors.background_color)
        text = self.font.render(caption=self.caption, color=self._render_colors.foreground_color)
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.surface.blit(text, text_rect)

    def update(self) -> None:
        """Update the button."""
        if self.state == WidgetStateEnum.NORMAL:
            self._render_colors = self.colors.normal
        elif self.state == WidgetStateEnum.HOVER:
            self._render_colors = self.colors.hover
        elif self.state == WidgetStateEnum.MOUSE_DOWN:
            self._render_colors = self.colors.click
        elif self.state == WidgetStateEnum.MOUSE_UP:
            self._render_colors = self.colors.hover

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle an event."""
        if not self.is_active or not self.is_visible:
            return

        # Delegate click events to mixin method
        super().handle_events(events)
        self.handle_click_events(events)

    def on_mouse_down(self) -> None:
        """The on mouse down event."""

    def on_mouse_up(self) -> None:
        """The on mouse up event."""

    def on_click(self) -> None:
        """The on click event."""
        print(f"Button {self.id} clicked.")

    def on_hover_in(self) -> None:
        """The on hover in event."""

    def on_hover_out(self) -> None:
        """The on hover out event."""

    def serialize(self) -> dict[str, Any]:
        """Convert the widget to a dictionary.

        Returns:
            dict[str, Any]: The widget as a dictionary.

        """
        data = super().serialize()
        data["caption"] = self.caption
        data["font"] = self.font.serialize()
        return data

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> "Button":
        """Create a widget from a dictionary.

        Args:
            data: dict[str, Any]: The data to create the widget from.

        Returns:
            BaseWidget: The widget.

        """
        obj = super().deserialize(data)
        obj.caption = data["caption"]
        font_data = data["font"]
        obj.font = SerializableFont.deserialize(font_data)
        return obj


class GothicButton(Button):
    """The Gothic button class."""

    def draw(self) -> None:
        """Draw the gothic button."""
