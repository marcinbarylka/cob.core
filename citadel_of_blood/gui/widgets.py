"""Widgets for the GUI."""

import abc
import dataclasses
import uuid
from typing import Any

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.gui.colors import ColorPair, WidgetColors
from citadel_of_blood.gui.serialization import SerializableFont, deserialize_surface, serialize_surface

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

        self.state = "normal"

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


class Button(BaseWidget):
    """The button class."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        colors: WidgetColors,
        caption: str = "Click me",
        id: str = "",
    ):
        """Initialize the Button class."""
        super().__init__(x, y, width, height, colors, id)
        self.caption = caption
        self.font = SerializableFont(
            font_path=PROJECT_ROOT / "assets/fonts/Roboto-Regular.ttf",
            size=36,
        )  # todo: make this configurable

    def draw(self) -> None:
        """Draw the button."""
        pygame.draw.rect(self.surface, self._render_colors.background_color, self.rect)
        self.surface.fill(self._render_colors.background_color)
        text = self.font.render(caption=self.caption, color=self._render_colors.foreground_color)
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.surface.blit(text, text_rect)

    def update(self) -> None:
        """Update the button."""

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle an event."""
        if not self.is_active:
            return

        # hover effect
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.state = "hover"
            self.on_hover_in()
        else:
            self.state = "normal"
            self.on_hover_out()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  # noqa: SIM102
                if self.rect.collidepoint(event.pos):
                    self.state = "mousedown"
                    self.on_mouse_down()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

    def on_mouse_down(self) -> None:
        """The on mouse down event."""
        pass

    def on_mouse_up(self) -> None:
        """The on mouse up event."""
        pass

    def on_click(self) -> None:
        """The on click event."""
        print(f"Button {self.id} clicked.")

    def on_hover_in(self) -> None:
        """The on hover in event."""
        self._render_colors = self.colors.hover

    def on_hover_out(self) -> None:
        """The on hover out event."""
        self._render_colors = self.colors.normal

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
